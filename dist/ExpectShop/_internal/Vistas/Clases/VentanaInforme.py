import os
from Main import BASE_DIR
from Conexiones import *
import pyqtgraph as pg 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import *

class ventanaInfome(QWidget):
    def __init__(self):
        super().__init__()

        ruta_ui = os.path.join(BASE_DIR, "Vistas", "Ventanas", "informe_widget.ui")
        uic.loadUi(ruta_ui,self)

        self.actualizar_interfaz()

        self.insertar_grafico()

    def insertar_grafico(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        self.grafico = pg.PlotWidget()
        self.verticalLayout.addWidget(self.grafico)

        self.grafico.setBackground("w")
        self.grafico.setLabel("left",textos.get("leyendaY"),color="k")
        self.grafico.setLabel("bottom",textos.get("leyendaX"),color="k")

        datos = obtener_datos()

        nombres = list(datos.keys())
        ventas = list(datos.values())

        posiciones_x = list(range(len(nombres)))

        color_barras = QColor("#6631D7") if app.configuracion_aplicada["Tema"] == "PD" else QColor("#000000")

        item_barras = pg.BarGraphItem(
            x=posiciones_x,
            height=ventas,
            width=0.6,
            brush=color_barras
        )

        self.grafico.addItem(item_barras)

        eje_x = self.grafico.getAxis("bottom")
        etiquetas_eje = list(enumerate(nombres))
        eje_x.setTicks([etiquetas_eje])

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        self.lblTitulo.setText(textos.get("labelTituloInformes"))

