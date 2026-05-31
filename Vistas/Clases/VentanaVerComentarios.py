import os
from Main import BASE_DIR
from Conexiones import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

class ventanaVerComentarios(QDialog):
    def __init__(self,juego):
        super().__init__()

        self.juego = juego

        ruta_ui = os.path.join(BASE_DIR, "Vistas", "Ventanas", "ver_comentarios_widget.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        self.mostrar_comentarios()

    def mostrar_comentarios(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        contenedor = QWidget()

        layoutPrincipal =QVBoxLayout(contenedor)
        layoutPrincipal.setSpacing(15)

        comentarios = obtener_comentarios(self.juego)

        for c in comentarios:
            frameComent = QFrame()
            frameComent.setFrameShape(QFrame.Box)

            layoutFrame = QVBoxLayout(frameComent)
            layoutFrame.setContentsMargins(10,10,10,10)

            label_usuario=QLabel(textos.get("textoComNickname")+f"<b>{c['Nickname']}</b>")
            label_valor=QLabel(f"{c['Valoracion']}"+textos.get("textoComPuntuacion"))
            label_comen=QLabel(textos.get("textoComComentario")+f"{c['Comentario']}")
            label_comen.setWordWrap(True)

            layoutFrame.addWidget(label_usuario)
            layoutFrame.addWidget(label_valor)
            layoutFrame.addWidget(label_comen)

            layoutPrincipal.addWidget(frameComent)
        
        layoutPrincipal.addStretch()

        contenedor.setLayout(layoutPrincipal)

        self.scrollComentarios.setWidget(contenedor)
        self.scrollComentarios.setWidgetResizable(True)

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]
            
        self.lblTitulo.setText(textos.get("labelComentarios"))

        self.setWindowTitle(textos.get("tituloVentanaComentarios")+self.juego)