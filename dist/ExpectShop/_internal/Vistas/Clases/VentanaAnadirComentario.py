import os
from Main import BASE_DIR
from Conexiones import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

class ventanaAnadirComentario(QWidget):
    def __init__(self):
        super().__init__()

        ruta_ui = os.path.join(BASE_DIR, "Vistas","Ventanas", "comentarios_widget.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        self.meter_juegos_combobox()
        self.btnSubirComent.clicked.connect(self.comentar)

    def meter_juegos_combobox(self):
        juegos = obtener_biblioteca()

        for j in juegos:
            self.comboJuegos.addItem(j["Nombre"])

    def comentar(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        juego = self.comboJuegos.currentText()
        valor = self.spnBxValoracion.value()
        comen = self.inputComentario.text()

        if comen == "":
            QMessageBox.information(self,textos.get("tituloError"),textos.get("textoErrorComent"))
        else:
            subir_comentario(juego,valor,comen)
            QMessageBox.information(self,textos.get("tituloExito"),textos.get("textoExitoComent"))
            self.comboJuegos.setCurrentIndex(-1)
            self.spnBxValoracion.setValue(0)
            self.inputComentario.setText("")

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]
            
        self.lblSelecciona.setText(textos["labelSeleccion"])
        self.lblIndica.setText(textos["labelPuntuacion"])
        self.lblInserta.setText(textos["labelInsertComent"])
        self.btnSubirComent.setText(textos["btnSubirComent"])