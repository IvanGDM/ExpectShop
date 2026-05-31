import os
from Conexiones import *
from Main import BASE_DIR
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *
from PyQt5.QtCore import *

class ventanaAnadirJuego(QWidget):
    def __init__(self):
        super().__init__()

        ruta_ui = os.path.join(BASE_DIR, "Vistas", "Ventanas", "anadir_juego_widget.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        self.btnSubirJuego.clicked.connect(self.crear_juego)

    def crear_juego(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        nombre = self.inputNombreJuego.text()
        generos = self.inputGeneros.text()
        precio = float(self.inputPrecio.text())

        if comprobarCatalogo(nombre):
            QMessageBox.critical(self,textos.get("tituloError"),textos.get("textoErrorSubida"))
        else:
            subir_juego(nombre,generos,precio)
            QMessageBox.information(self,textos.get("tituloExito"),textos.get("textoExitoSubida"))

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]
            
        self.inputNombreJuego.setPlaceholderText(textos["labelNombreJuego"])
        self.inputGeneros.setPlaceholderText(textos["labelGenerosJuego"])
        self.inputPrecio.setPlaceholderText(textos["labelPrecioJuego"])
        self.btnSubirJuego.setText(textos["btnSubirJuego"])