from pymongo import MongoClient
import bcrypt
from Modelos.Usuario_loged import *
Mongo = MongoClient("mongodb+srv://IvanRoot:root@clusterpythonproyecto.hell1yw.mongodb.net/")
BBDD = Mongo["BaseExpectShop"]
usuarios = BBDD.get_collection("Usuarios")
juegos = BBDD.get_collection("Juegos")
bibliotecas = BBDD.get_collection("Bibliotecas")
comentarios = BBDD.get_collection("Comentarios")
config = BBDD.get_collection("Config")

def iniciarSesion(nickname,contra):
    posibleUser = usuarios.find_one({"Nickname":nickname})
    if not posibleUser:
        return False
    
    if not bcrypt.checkpw(contra.encode("utf-8"), posibleUser["Contrasenia"]):
        return False
    
    usuario_sesion = Usuario_loged()
    if posibleUser["Rol"] == "Creator":
        usuario_sesion.guardarCreador(posibleUser["Nickname"],posibleUser["Saldo"],posibleUser["Rol"],posibleUser["Ventas"])
    else:
        usuario_sesion.guardarUsuario(posibleUser["Nickname"],posibleUser["Saldo"],posibleUser["Rol"])
    return True   


def actualizarDatosUsuario():
    usuario_actual = Usuario_loged()
    filtro = {"Nickname":usuario_actual.Nickname}
    operacion = None
    if usuario_actual.Rol == "User":
        operacion = {"$set":{"Saldo":usuario_actual.Saldo}}
    elif usuario_actual.Rol == "Creator":
        operacion = {"$set":{"Saldo":usuario_actual.Saldo,"Ventas":usuario_actual.Ventas}}
    usuarios.update_one(filtro,operacion)


def obtener_biblioteca():
    usuario_actual = Usuario_loged()

    busqueda = bibliotecas.find({"Nickname":usuario_actual.Nickname},{"_id":0,"Nickname":0})
    listado = list(busqueda)
    lista_juegos = []

    for i in listado:
        juego = juegos.find_one({"Nombre":i["Nombre"]},{"_id":0})
        lista_juegos.append(juego)

    return lista_juegos

def obtener_catalogo():
    busqueda = juegos.find({},{"_id":0})
    listado = list(busqueda)

    return listado

def obtener_comentarios(juego):
    busqueda = comentarios.find({"Juego":juego},{"_id":0})
    listado = list(busqueda)
    
    return listado

def registrar_usuario(Nick,Contra,Rol):

    hash_contra = bcrypt.hashpw(Contra.encode("utf-8"),bcrypt.gensalt())

    if Rol == "User":
        usuarios.insert_one({"Nickname":Nick,"Contrasenia":hash_contra,"Saldo":0,"Rol":Rol})
    else:
        usuarios.insert_one({"Nickname":Nick,"Contrasenia":hash_contra,"Saldo":0,"Rol":Rol,"Ventas":0})

def comprobarBiblio(juego):
    usuario_actual = Usuario_loged()
    result = bibliotecas.find_one({"Nickname":usuario_actual.Nickname,"Nombre":juego})
    if result:
        return True
    return False

def comprobarCatalogo(juego):
    result = juegos.find_one({"Nombre":juego})
    if result:
        return True
    return False

def comprar_juego(juego,dinero):
    usuario_actual = Usuario_loged()
    bibliotecas.insert_one({"Nombre":juego,"Nickname":usuario_actual.Nickname})
    usuario_actual.Saldo -= dinero
    comprobar_creador(juego)
    actualizarDatosUsuario()

def reembolsar_juego(juego,dinero):
    usuario_actual = Usuario_loged()
    bibliotecas.delete_one({"Nickname":usuario_actual.Nickname,"Nombre":juego})
    usuario_actual.Saldo += dinero
    actualizarDatosUsuario()

def subir_comentario(juego,valor,com):
    usuario_actual = Usuario_loged()
    filtro = {"Nickname":usuario_actual.Nickname,"Juego":juego}
    operacion = {"$set" : {"Valoracion":valor,"Comentario":com}}
    comentarios.update_one(filtro,operacion,upsert = True)

def comprobar_creador(juego):
    juego_catalogo = juegos.find_one({"Nombre":juego},{"_id":0})

    autor_juego = juego_catalogo["Autor"]

    busqueda_creador = usuarios.find_one({"Nickname":autor_juego},{"_id":0})

    if busqueda_creador:
        filtro = {"Nickname":busqueda_creador["Nickname"]}
        operacion = {"$inc":{"Ventas":1,"Saldo":juego_catalogo["Precio"]}}
        usuarios.update_one(filtro,operacion)


def subir_juego(nombre,generos,precio):
    usuario_actual = Usuario_loged()

    juegos.insert_one({"Nombre":nombre,"Autor":usuario_actual.Nickname,"Generos":generos,"Precio":precio})


def obtener_datos():
    datos = {}

    todos_los_juegos = list(juegos.find({},{"_id":0}))

    nombres = []

    for juego in todos_los_juegos:
        nombres.append(juego["Nombre"])

    for nombre in nombres:
        datos[nombre] = bibliotecas.count_documents({"Nombre":nombre})

    return datos

def obtener_estilo():
    estilos = config.find_one({},{"_id":0})
    return estilos

def guardar_estilo(tema,fuente,idiom):
    
    config.update_one({},{"$set":{"Tema":tema,"Fuente":fuente,"Idioma":idiom}})