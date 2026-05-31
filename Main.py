import sys
import os
from Conexiones import *
from Vistas.Clases.VentanaInicioSesion import *
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Estilos.Idiomas.En import textos as textos_en
from Estilos.Idiomas.Es import textos as textos_es
from Estilos.Tamanio.Tamanio import tamanios as tamanios_base

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.join(os.path.dirname(sys.executable),"_internal")
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def cargar_estilos(app):

    ruta_qss = os.path.join(BASE_DIR,"Estilos","Temas",app.configuracion_aplicada["Tema"]+".qss")
    ruta_logotipo = os.path.join(BASE_DIR,"Assets","logotipo.png")
    icono = QIcon(ruta_logotipo)
    
    with open(ruta_qss, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

        var = app.configuracion_aplicada["Fuente"]
        contenido = contenido.replace("{{label}}",f"{tamanios_base['label']+var}px")
        contenido = contenido.replace("{{titulo}}",f"{tamanios_base['titulo']+var}px")
        contenido = contenido.replace("{{button}}",f"{tamanios_base['button']+var}px")
        contenido = contenido.replace("{{menu}}",f"{tamanios_base['menu']+var}px")

        app.setStyleSheet(contenido)
        app.setWindowIcon(icono)

app = QApplication(sys.argv)
app.diccionario_idiomas = {"Es":textos_es, "En":textos_en}
app.configuracion_aplicada = obtener_estilo()
app.configuracion_inicial = app.configuracion_aplicada.copy()
cargar_estilos(app)
ventanaInicio = ventanaInicioSesion()
ventanaInicio.show()
sys.exit(app.exec_())