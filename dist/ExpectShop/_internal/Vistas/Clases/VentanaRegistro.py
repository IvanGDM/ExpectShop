import os
from Main import BASE_DIR
from Conexiones import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

class ventanaRegistro(QDialog):
    def __init__(self):
        super().__init__()

        ruta_ui = os.path.join(BASE_DIR, "Vista", "Ventanas", "registro_dialog.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnRegistrarse.clicked.connect(self.registrar)

    def registrar(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        from Vistas.Clases.VentanaInicioSesion import ventanaInicioSesion

        if self.inputContra.text() != self.inputContra2.text():
            QMessageBox.critical(self,textos.get("tituloError"),textos.get("textoErrorRegistro"))

            self.inputContra.setText("")
            self.inputContra2.setText("")
        else:
            if self.rdbtnUser.isChecked():
                registrar_usuario(self.inputNickname.text(),self.inputContra.text(),"User")

            elif self.rdbtnCreador.isChecked():
                registrar_usuario(self.inputNickname.text(),self.inputContra.text(),"Creator")

            QMessageBox.information(self,textos.get("tituloExito"),textos.get("textoExitoRegistro"))
            
            self.inicio = ventanaInicioSesion()

            self.inicio.show()

            self.close()
            
    def cancelar(self):
        from Vistas.Clases.VentanaInicioSesion import ventanaInicioSesion

        self.inicio = ventanaInicioSesion()

        self.inicio.show()

        self.close()

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]
            
        self.lblNickname.setText(textos.get("labelNickname"))
        self.lblContra.setText(textos.get("labelContrasenia"))
        self.lblReContra.setText(textos.get("labelRepetirContra"))
        self.lblRol.setText(textos.get("labelRol"))
        self.rdbtnCreador.setText(textos.get("rdbtnCreator"))
        self.rdbtnUser.setText(textos.get("rdbtnUser"))
        self.btnCancelar.setText(textos.get("btnCancelar"))
        self.btnRegistrarse.setText(textos.get("btnRegistrarse"))
        self.inputNickname.setPlaceholderText(textos.get("labelNickname"))
        self.inputContra.setPlaceholderText(textos.get("labelContrasenia"))
        self.inputContra2.setPlaceholderText(textos.get("labelRepetirContra"))

        self.setWindowTitle(textos.get("tituloVentanaRegistro"))

