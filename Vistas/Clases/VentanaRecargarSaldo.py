import os
from Main import BASE_DIR
from Conexiones import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

class ventanaRecargarSaldo(QWidget):

    def __init__(self):
        super().__init__()

        ruta_ui = os.path.join(BASE_DIR, "Vistas", "Ventanas", "recargar_widget.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        self.btnRecargar.clicked.connect(self.recargarDinero)

    def recargarDinero(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        usuario_actual = Usuario_loged()

        try:
            if float(self.inputDinero.text()) < 0:
                QMessageBox.critical(self,textos.get("tituloError"),textos.get("textoErrorIngresoSaldo"))
            else:
                resultado = usuario_actual.Saldo + int(self.inputDinero.text())
                usuario_actual.Saldo = resultado
                actualizarDatosUsuario()
                QMessageBox.information(self,textos.get("tituloExito"),textos.get("textoExitoRecarga"))
        except ValueError:
            QMessageBox.critical(self,textos.get("tituloError"),textos.get("textoErrorInput"))
        finally:
            self.inputDinero.setText("")

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        self.lblTitulo.setText(textos.get("labelIngreso"))
        self.btnRecargar.setText(textos.get("btnAñadirSaldo"))