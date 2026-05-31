import os
from Main import BASE_DIR
from Modelos.Usuario_loged import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

class ventanaPerfilUsuario(QWidget):

    usuario_actual = Usuario_loged()

    def __init__(self):
        super().__init__()

        ruta_ui = os.path.join(BASE_DIR, "Vistas", "Ventanas", "perfil_usuario_widget.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]
            
        self.lblTitulo.setText(textos.get("labelPerfilUsuario"))
        self.labelNickname.setText(textos.get("labelNickPerfil")+str(self.usuario_actual.Nickname))
        self.labelSaldo.setText(textos.get("labelSaldoPerfil")+str(self.usuario_actual.Saldo)+"€")