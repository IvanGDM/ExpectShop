import os
from Main import BASE_DIR
from Estilos.Tamanio.Tamanio import tamanios as tamanios_base
from Conexiones import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import *

class ventanaConfiguracion(QWidget):
    def __init__(self,callback_ref):
        super().__init__()

        self.alCambiarConfig = callback_ref

        ruta_ui = os.path.join(BASE_DIR, "Vistas", "Ventanas", "config_widget.ui")
        uic.loadUi(ruta_ui,self)

        self.btnGuardar.clicked.connect(self.guardar_config)
        self.btnResetear.clicked.connect(self.resetear)

        app = QApplication.instance()
        self.sincronizar_widgets(app.configuracion_aplicada)
        self.actualizar_ventana()
        

    def sincronizar_widgets(self,diccionario_config):
        if diccionario_config["Idioma"] == "Es":
            self.rdbtnEspaniol.setChecked(True)
        else:
            self.rdbtnIngles.setChecked(True)

        if diccionario_config["Tema"] == "PD":
            self.rdbtnPD.setChecked(True)
        else:
            self.rdbtnDrk.setChecked(True)

        self.spnBxTamanio.setValue(diccionario_config["Fuente"])

    def actualizar_ventana(self):
        app = QApplication.instance()

        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        self.lblTema.setText(textos.get("labelTema"))
        self.lblTamanio.setText(textos.get("labelTamanio"))
        self.lblIdioma.setText(textos.get("labelIdioma"))
        self.rdbtnPD.setText(textos.get("rdbtnTemaDefect"))
        self.rdbtnEspaniol.setText(textos.get("rdbtnEsp"))
        self.rdbtnDrk.setText(textos.get("rdbtnTemaOscuro"))
        self.rdbtnIngles.setText(textos.get("rdbtnIng"))
        self.btnResetear.setText(textos.get("btnReset"))
        self.btnGuardar.setText(textos.get("btnGuardar"))
        self.lblTitulo.setText(textos.get("menuConfig"))

    def guardar_config(self):
        app = QApplication.instance()

        idiomaSeleccionado = "Es" if self.rdbtnEspaniol.isChecked() else "En"
        temaSeleccionado = "PD" if self.rdbtnPD.isChecked() else "Drk"
        tamanio_fuente = self.spnBxTamanio.value()

        guardar_estilo(temaSeleccionado,tamanio_fuente,idiomaSeleccionado)

        app.configuracion_aplicada["Idioma"] = idiomaSeleccionado
        app.configuracion_aplicada["Tema"] = temaSeleccionado
        app.configuracion_aplicada["Fuente"] = tamanio_fuente

        self.aplicar_estilo_global(app)
        self.actualizar_ventana()

        if self.alCambiarConfig:
            self.alCambiarConfig()


    def resetear(self):
        app = QApplication.instance()

        app.configuracion_aplicada = app.configuracion_inicial.copy()

        self.sincronizar_widgets(app.configuracion_aplicada)

        self.actualizar_ventana()

        self.aplicar_estilo_global(app)

    def aplicar_estilo_global(self,app):
        ruta_qss = os.path.join(BASE_DIR, "Estilos", "Temas", app.configuracion_aplicada["Tema"] + ".qss")
        
        with open(ruta_qss, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

            var = app.configuracion_aplicada["Fuente"]
            contenido = contenido.replace("{{label}}",f"{tamanios_base['label']+var}px")
            contenido = contenido.replace("{{titulo}}",f"{tamanios_base['titulo']+var}px")
            contenido = contenido.replace("{{button}}",f"{tamanios_base['button']+var}px")
            contenido = contenido.replace("{{menu}}",f"{tamanios_base['menu']+var}px")

            app.setStyleSheet(contenido)
        
        if self.layout():
            self.layout().activate()