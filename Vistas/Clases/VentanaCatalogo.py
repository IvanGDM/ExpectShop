import os
from Main import BASE_DIR
from Vistas.Clases.VentanaVerComentarios import *
from Conexiones import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import *

class ventanaCatalogo(QWidget):
    def __init__(self):
        super().__init__()

        self.catalogo = obtener_catalogo()

        ruta_ui = os.path.join(BASE_DIR, "Vistas", "Ventanas", "comprar_widget.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        self.tablaJuegos.setSelectionMode(QAbstractItemView.NoSelection)
        self.tablaJuegos.horizontalHeader().setHighlightSections(False)
        self.tablaJuegos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tablaJuegos.verticalHeader().setVisible(False)
        self.tablaJuegos.setRowCount(len(self.catalogo))

        self.rellenar_catalogo()

    def rellenar_catalogo(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        fila = 0

        for juego in self.catalogo:
            self.tablaJuegos.setItem(fila,0,QTableWidgetItem(juego["Nombre"]))
            self.tablaJuegos.setItem(fila,1,QTableWidgetItem(juego["Autor"]))
            self.tablaJuegos.setItem(fila,2,QTableWidgetItem(juego["Generos"]))
            self.tablaJuegos.setItem(fila,3,QTableWidgetItem(str(juego["Precio"])+"€"))
            boton_jugar = QPushButton(textos.get("btnComprar"))
            self.tablaJuegos.setCellWidget(fila,4,boton_jugar)
            boton_comentarios = QPushButton(textos.get("btnComentarios"))
            self.tablaJuegos.setCellWidget(fila,5,boton_comentarios)

            boton_jugar.clicked.connect(lambda _,j = juego["Nombre"],pre =juego["Precio"]:self.comprar(j,pre))
            boton_comentarios.clicked.connect(lambda _,j = juego["Nombre"]:self.ver_comentarios(j))
            fila += 1

    def comprar(self,juego,precio):
        usuario_actual = Usuario_loged()
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        estaono = comprobarBiblio(juego)
        if estaono:
            QMessageBox.critical(self,textos.get("tituloError"),textos.get("textoErrorCompra"))
        else:
            if usuario_actual.Saldo < precio:
                QMessageBox.information(self,textos.get("tituloError"),textos.get("textoErrorSaldoCompra"))
            else:
                comprar_juego(juego,precio)
                QMessageBox.information(self,textos.get("tituloExito"),textos.get("textoExitoCompra")+juego)

    def ver_comentarios(self,juego):
        self.ventana_comentarios = ventanaVerComentarios(juego)

        self.ventana_comentarios.exec_()

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]
            
        self.lblTitulo.setText(textos.get("labelCatalogo"))

        columnas = textos.get("cabecerasCatalogo")
        self.tablaJuegos.setHorizontalHeaderLabels(columnas)

