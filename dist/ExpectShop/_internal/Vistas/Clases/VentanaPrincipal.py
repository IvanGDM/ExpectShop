import os
from Main import BASE_DIR
from Vistas.Clases.VentanaBiblioteca import *
from Vistas.Clases.VentanaRecargarSaldo import *
from Vistas.Clases.VentanaPerfilUsuario import *
from Vistas.Clases.VentanaPerfilCreador import *
from Vistas.Clases.VentanaCatalogo import *
from Vistas.Clases.VentanaAnadirJuego import *
from Vistas.Clases.VentanaConfiguracion import *
from Vistas.Clases.VentanaAnadirComentario import *
from Vistas.Clases.VentanaInforme import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

class ventanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.usuario_actual = Usuario_loged()

        ruta_ui = os.path.join(BASE_DIR, "Vistas", "Ventanas", "ventana_principal.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        if self.usuario_actual.Rol == "User":
            self.actionAnadirJuego.setVisible(False)

        self.actionBiblioteca.triggered.connect(self.ver_biblioteca)
        self.actionRecargar.triggered.connect(self.rec_saldo)
        self.actionPerfil.triggered.connect(self.ver_perfil)
        self.actionCerrarSesion.triggered.connect(self.cerrar_sesion)
        self.actionComprar.triggered.connect(self.ver_catalogo)
        self.actionAnadirJuego.triggered.connect(self.anadir_juego)
        self.menuConfig.aboutToShow.connect(self.configurar)
        self.actionAnadirComentario.triggered.connect(self.anadir_comen)
        self.menuInformes.aboutToShow.connect(self.ver_informes)

    def ver_biblioteca(self):
        self.wid_biblioteca = ventanaBiblioteca()

        self.setCentralWidget(self.wid_biblioteca)

    def rec_saldo(self):
        self.wid_rec_sal = ventanaRecargarSaldo()

        self.setCentralWidget(self.wid_rec_sal)

    def ver_perfil(self):
        self.wid_perfil = None

        if self.usuario_actual.Rol == "User":
            self.wid_perfil = ventanaPerfilUsuario()
        elif self.usuario_actual.Rol == "Creator":
            self.wid_perfil = ventanaPerfilCreador()

        self.setCentralWidget(self.wid_perfil)

    def cerrar_sesion(self):
        from Vistas.Clases.VentanaInicioSesion import ventanaInicioSesion

        self.ventana_inicio_sesion = ventanaInicioSesion()

        self.ventana_inicio_sesion.show()

        self.close()

    def ver_catalogo(self):
        self.wid_cat = ventanaCatalogo()

        self.setCentralWidget(self.wid_cat)

    def anadir_juego(self):
        self.wid_anadir = ventanaAnadirJuego()

        self.setCentralWidget(self.wid_anadir)

    def configurar(self):
        self.wid_config = ventanaConfiguracion(callback_ref=self.actualizar_interfaz)

        self.setCentralWidget(self.wid_config)

    def anadir_comen(self):
        self.wid_anadir_comen = ventanaAnadirComentario()

        self.setCentralWidget(self.wid_anadir_comen)

    def ver_informes(self):
        self.wid_informe = ventanaInfome()

        self.setCentralWidget(self.wid_informe)

    def actualizar_interfaz(self):
            app = QApplication.instance()
            textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]
            
            self.menuUsuario.setTitle(textos["menuUsuario"])
            self.actionBiblioteca.setText(textos["actionBiblio"])
            self.actionRecargar.setText(textos["actionRecargar"])
            self.actionPerfil.setText(textos["actionPerfil"])
            self.actionCerrarSesion.setText(textos["actionCerrarSesion"])

            self.menuJuegos.setTitle(textos["menuCatalogo"])
            self.actionComprar.setText(textos["actionComprar"])
            self.actionAnadirJuego.setText(textos["actionAnadir"])
            self.actionAnadirComentario.setText(textos["actionAnadirComentario"])

            self.menuConfig.setTitle(textos["menuConfig"])

            self.menuInformes.setTitle(textos["menuInformes"])

            self.setWindowTitle(textos.get("tituloVentanaPrincipal"))
