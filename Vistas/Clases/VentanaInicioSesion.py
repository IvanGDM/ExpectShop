import os
from Conexiones import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

class ventanaInicioSesion(QDialog):
    def __init__(self):
        super().__init__()
        from Main import BASE_DIR

        ruta_ui = os.path.join(BASE_DIR,"Vistas", "Ventanas", "login_dialog.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        self.btnIniciarSesion.clicked.connect(self.iniciar_sesion)

        self.btnRegistrar.clicked.connect(self.registrarse)

    def iniciar_sesion(self):
        from Vistas.Clases.VentanaPrincipal import ventanaPrincipal
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        result = iniciarSesion(self.editNickname.text(),self.editContra.text())

        if result:

            self.menu_principal = ventanaPrincipal()

            self.menu_principal.show()

            self.close()
        else:
            QMessageBox.critical(self,textos.get("tituloError"),textos.get("labelErrorInicio"))

    def registrarse(self):
        from Vistas.Clases.VentanaRegistro import ventanaRegistro
        
        self.menu_registro = ventanaRegistro()

        self.menu_registro.show()

        self.close()

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]
            
        self.lblNickname.setText(textos.get("labelNickname"))
        self.lblContra.setText(textos.get("labelContrasenia"))
        self.editNickname.setPlaceholderText(textos.get("labelNickname"))
        self.editContra.setPlaceholderText(textos.get("labelContrasenia"))
        self.btnIniciarSesion.setText(textos.get("btnIniciarSesion"))
        self.btnRegistrar.setText(textos.get("btnRegistrarse"))

        self.setWindowTitle(textos.get("tituloVentanaInicio"))
