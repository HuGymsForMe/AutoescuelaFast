from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.Qt import QSizePolicy
from PyQt5.QtGui import QIcon, QImage, QPixmap

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import os

#AÑADIR TIEMPO MEDIO TEST

class MiPerfil(QMainWindow):
    def __init__(self, ventana_user, almacen_usuarios, almacen_partidas, nickname_var):
        super().__init__()
        self.ventana_user = ventana_user
        self.almacen_usuarios = almacen_usuarios
        self.almacen_partidas = almacen_partidas
        self.nickname_var = nickname_var
        self.RUTA_CSS = os.path.abspath('./css/mi_perfil.css')
        
        #DATOS USUARIOS
        self.nombre = None
        self.gmail = None
        self.apellidos = None
        self.fecha_ingreso = None
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(904, 643)
        self.setMinimumSize(QtCore.QSize(904, 643))
        self.setMaximumSize(QtCore.QSize(904, 643))
        with open(self.RUTA_CSS) as f:
            self.setStyleSheet(f.read())

        self.favicon = QIcon('./img/coche.png')
        self.setWindowIcon(self.favicon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ventana_scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.ventana_scroll.setStyleSheet("")
        self.ventana_scroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ventana_scroll.setWidgetResizable(True)
        self.ventana_scroll.setObjectName("ventana_scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 868, 2022))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_scroll = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_scroll.setMinimumSize(QtCore.QSize(800, 1620))
        self.frame_scroll.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_scroll.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_scroll.setObjectName("frame_scroll")
        self.title_mis_datos = QtWidgets.QLabel(self.frame_scroll)
        self.title_mis_datos.setGeometry(QtCore.QRect(320, 10, 201, 71))
        self.title_mis_datos.setObjectName("title_mis_datos")
        self.print_nickname = QtWidgets.QLabel(self.frame_scroll)
        self.print_nickname.setGeometry(QtCore.QRect(150, 100, 221, 61))
        self.print_nickname.setObjectName("print_nickname")
        self.print_nombre = QtWidgets.QLabel(self.frame_scroll)
        self.print_nombre.setGeometry(QtCore.QRect(150, 170, 201, 61))
        self.print_nombre.setObjectName("print_nombre")
        self.print_apellidos = QtWidgets.QLabel(self.frame_scroll)
        self.print_apellidos.setGeometry(QtCore.QRect(150, 240, 201, 61))
        self.print_apellidos.setObjectName("print_apellidos")
        self.print_fecha_inicio = QtWidgets.QLabel(self.frame_scroll)
        self.print_fecha_inicio.setGeometry(QtCore.QRect(150, 310, 201, 61))
        self.print_fecha_inicio.setObjectName("print_fecha_inicio")
        self.print_gmail = QtWidgets.QLabel(self.frame_scroll)
        self.print_gmail.setGeometry(QtCore.QRect(150, 380, 201, 61))
        self.print_gmail.setObjectName("print_gmail")
        self.mi_nickname = QtWidgets.QLabel(self.frame_scroll)
        self.mi_nickname.setGeometry(QtCore.QRect(490, 100, 381, 61))
        self.mi_nickname.setObjectName("mi_nickname")
        self.mi_nombre = QtWidgets.QLabel(self.frame_scroll)
        self.mi_nombre.setGeometry(QtCore.QRect(490, 170, 381, 61))
        self.mi_nombre.setObjectName("mi_nombre")
        self.mis_apellidos = QtWidgets.QLabel(self.frame_scroll)
        self.mis_apellidos.setGeometry(QtCore.QRect(490, 240, 391, 61))
        self.mis_apellidos.setObjectName("mis_apellidos")
        self.mi_fecha_de_ingreso = QtWidgets.QLabel(self.frame_scroll)
        self.mi_fecha_de_ingreso.setGeometry(QtCore.QRect(490, 310, 381, 61))
        self.mi_fecha_de_ingreso.setObjectName("mi_fecha_de_ingreso")
        self.mi_gmail = QtWidgets.QLabel(self.frame_scroll)
        self.mi_gmail.setGeometry(QtCore.QRect(490, 380, 381, 61))
        self.mi_gmail.setObjectName("mi_gmail")
        self.title_mis_stats = QtWidgets.QLabel(self.frame_scroll)
        self.title_mis_stats.setGeometry(QtCore.QRect(260, 480, 351, 71))
        self.title_mis_stats.setObjectName("title_mis_stats")
        self.linea_separacion = QtWidgets.QFrame(self.frame_scroll)
        self.linea_separacion.setGeometry(QtCore.QRect(-20, 440, 911, 20))
        self.linea_separacion.setStyleSheet("")
        self.linea_separacion.setFrameShape(QtWidgets.QFrame.HLine)
        self.linea_separacion.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.linea_separacion.setObjectName("linea_separacion")
        self.print_test_realizados = QtWidgets.QLabel(self.frame_scroll)
        self.print_test_realizados.setGeometry(QtCore.QRect(290, 540, 251, 71))
        self.print_test_realizados.setObjectName("print_test_realizados")
        self.num_test_realizados = QtWidgets.QLabel(self.frame_scroll)
        self.num_test_realizados.setGeometry(QtCore.QRect(540, 540, 41, 71))
        self.num_test_realizados.setObjectName("num_test_realizados")
        self.title_ultimos_test = QtWidgets.QLabel(self.frame_scroll)
        self.title_ultimos_test.setGeometry(QtCore.QRect(240, 1000, 531, 71))
        self.title_ultimos_test.setObjectName("title_ultimos_test")
        self.frame_footer = QtWidgets.QFrame(self.frame_scroll)
        self.frame_footer.setGeometry(QtCore.QRect(-50, 1520, 941, 101))
        self.frame_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_footer.setObjectName("frame_footer")
        self.print_footer = QtWidgets.QLabel(self.frame_footer)
        self.print_footer.setGeometry(QtCore.QRect(210, 30, 551, 41))
        self.print_footer.setObjectName("print_footer")

        self.apto, self.no_apto, self.test_realizados = self.almacen_partidas.crear_grafico_sectores(self.nickname_var)
        diagrama_de_sectores = Figure()
        canvas = FigureCanvas(diagrama_de_sectores)
        plt = diagrama_de_sectores.add_subplot(111)
        #EVITAR ERROR 0,0
        if self.apto == 0 and self.no_apto == 0:
            data = [1, 1]
        else:
            data = [self.apto, self.no_apto]
        labels = ['APTO', 'NO APTO']
        colors = ['#99ff99', '#ff9999']
        plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%')
        pixmap = canvas.grab().scaledToWidth(521) #ANCHO DIAGRAMA
        self.diagrama_de_sectores = QtWidgets.QLabel(self.frame_scroll)
        self.diagrama_de_sectores.setPixmap(pixmap)
        self.diagrama_de_sectores.setGeometry(QtCore.QRect(170, 630, 521, 341))
        self.diagrama_de_sectores.setObjectName("diagrama_de_sectores")

        categorias, valores = self.almacen_partidas.crear_grafico_barras(self.nickname_var)
        diagrama_de_barras = Figure()
        canvas = FigureCanvas(diagrama_de_barras)
        plt = diagrama_de_barras.add_subplot(111)
        plt.bar(categorias, valores)
        pixmap = canvas.grab().scaledToWidth(521) #ANCHO DIAGRAMA
        self.diagrama_de_barras = QtWidgets.QLabel(self.frame_scroll)
        self.diagrama_de_barras.setPixmap(pixmap)
        self.diagrama_de_barras.setGeometry(QtCore.QRect(170, 1090, 521, 341))
        self.diagrama_de_barras.setObjectName("diagrama_de_barras")

        self.verticalLayout_2.addWidget(self.frame_scroll)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ventana_scroll.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.ventana_scroll)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self.centralwidget)

        self.recoger_datos_personales()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "MiPerfil"))
        self.title_mis_datos.setText(_translate("self", "MIS DATOS"))
        self.print_nickname.setText(_translate("self", "Nombre de usuario:"))
        self.print_nombre.setText(_translate("self", "Nombre:"))
        self.print_apellidos.setText(_translate("self", "Apellidos:"))
        self.print_fecha_inicio.setText(_translate("self", "Usuario desde:"))
        self.print_gmail.setText(_translate("self", "Correo Electrónico:"))
        self.mi_nickname.setText(_translate("self", f"{self.nickname_var}"))
        self.mi_nombre.setText(_translate("self", f"{self.nombre}"))
        self.mis_apellidos.setText(_translate("self", f"{self.apellidos}"))
        self.mi_fecha_de_ingreso.setText(_translate("self", f"{self.fecha_ingreso}"))
        self.mi_gmail.setText(_translate("self", f"{self.gmail}"))
        self.title_mis_stats.setText(_translate("self", "MIS ESTADÍSTICAS"))
        self.print_test_realizados.setText(_translate("self", "TEST REALIZADOS: "))
        self.num_test_realizados.setText(_translate("self", f"{self.test_realizados}"))
        self.diagrama_de_sectores.setText(_translate("self", ""))
        self.title_ultimos_test.setText(_translate("self", "ÚLTIMOS TEST REALIZADOS"))
        self.diagrama_de_barras.setText(_translate("self", ""))
        self.print_footer.setText(_translate("self", "©  2023AutoescuelaFastApp. Todos los derechos reservados.  "))

    def recoger_datos_personales(self):
        self.nombre, self.gmail, self.apellidos, self.fecha_ingreso = self.almacen_usuarios.encontrar_usuario_para_mostrar_datos(self.nickname_var)

    @QtCore.pyqtSlot(QtGui.QCloseEvent)
    def closeEvent(self, event):
        self.cerrar_ventana_hija()
    
    def cerrar_ventana_hija(self):
        self.close()
        self.ventana_user.show()