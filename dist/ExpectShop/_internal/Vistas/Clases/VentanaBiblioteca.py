import os
from Main import BASE_DIR
from Vistas.Clases.VentanaAnadirComentario import *
from Vistas.Clases.VentanaReembolso import *
from Conexiones import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import *

class ventanaBiblioteca(QWidget):

    def __init__(self):
        super().__init__()

        self.juegos_usuario = obtener_biblioteca()

        ruta_ui = os.path.join(BASE_DIR, "Vistas", "Ventanas", "biblioteca_widget.ui")
        uic.loadUi(ruta_ui,self)

        self.tablaBiblioteca.setSelectionMode(QAbstractItemView.NoSelection)
        self.tablaBiblioteca.horizontalHeader().setHighlightSections(False)
        self.tablaBiblioteca.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tablaBiblioteca.verticalHeader().setVisible(False)
        self.tablaBiblioteca.setRowCount(len(self.juegos_usuario))

        self.actualizar_interfaz()

        self.rellenar_tabla()



    def rellenar_tabla(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]

        fila = 0

        for juego in self.juegos_usuario:
            self.tablaBiblioteca.setItem(fila,0,QTableWidgetItem(juego["Nombre"]))
            self.tablaBiblioteca.setItem(fila,1,QTableWidgetItem(juego["Autor"]))
            self.tablaBiblioteca.setItem(fila,2,QTableWidgetItem(juego["Generos"]))
            boton_jugar = QPushButton(textos.get("btnJugar"))
            self.tablaBiblioteca.setCellWidget(fila,3,boton_jugar)
            boton_rembolso = QPushButton(textos.get("btnReembolsar"))
            self.tablaBiblioteca.setCellWidget(fila,4,boton_rembolso)

            boton_jugar.clicked.connect(self.opcion_jugar)
            boton_rembolso.clicked.connect(lambda _,j = juego["Nombre"],pre = juego["Precio"]:self.opcion_reembolso(j,pre))

            fila += 1

    def opcion_jugar(self):
        QMessageBox.information(self,"Jugando","Jugando")

    def opcion_reembolso(self,juego,precio):
        self.ventana_reembolso = ventanaReembolso(juego,precio)

        self.ventana_reembolso.exec_()

        self.juegos_usuario = obtener_biblioteca()

        self.tablaBiblioteca.setRowCount(len(self.juegos_usuario))

        self.rellenar_tabla()

    def actualizar_interfaz(self):
        app = QApplication.instance()
        textos = app.diccionario_idiomas[app.configuracion_aplicada["Idioma"]]
            
        self.lblTitulo.setText(textos["labelTituloBiblioteca"])
        columnas = textos.get("cabecerasBiblioteca")
        self.tablaBiblioteca.setHorizontalHeaderLabels(columnas)
    
