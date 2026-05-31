import os
from Main import BASE_DIR
from Vistas.Clases.VentanaAnadirComentario import *
from Conexiones import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

class ventanaReembolso(QDialog):
    def __init__(self,juego,precio):
        super().__init__()

        self.juego_a_reembolsar = juego
        self.dinero_a_reembolsar = precio

        ruta_ui = os.path.join(BASE_DIR, "Vista", "Ventanas", "reembolso_dialog.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCancelar.clicked.connect(self.cancelar)

    def aceptar(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        reembolsar_juego(self.juego_a_reembolsar,self.dinero_a_reembolsar)
        QMessageBox.information(self,textos.get("tituloExito"),textos.get("textoExitoReembolso"))
        self.close()
    
    def cancelar(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        QMessageBox.information(self,textos.get("tituloCancel"),textos.get("textoCancelAccion"))
        self.close()

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        self.labelPregunta.setText(textos.get("textoPrevReembolso"))
        self.btnAceptar.setText(textos.get("btnAceptar"))
        self.btnCancelar.setText(textos.get("btnCancelar"))

        self.setWindowTitle(textos.get("tituloVentanaReembolso"))