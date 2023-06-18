from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.Qt import QSizePolicy
from PyQt5.QtGui import QIcon, QImage, QPixmap

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MiPerfil(QMainWindow):
    def __init__(self, ventana_user):
        super().__init__()
        self.ventana_user = ventana_user
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(904, 643)
        self.setMinimumSize(QtCore.QSize(904, 643))
        self.setMaximumSize(QtCore.QSize(904, 643))
        self.favicon = QIcon('./img/coche.png')
        self.setWindowIcon(self.favicon)
        self.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(0, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(9, 181, 203);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(4, 129, 145);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(56, 56, 0);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(0, 80, 122);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(0, 80, 122);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(56, 56, 0);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(0, 80, 122);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(0, 80, 122);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("background-color: rgb(56, 56, 56);")
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
        self.frame_scroll.setMinimumSize(QtCore.QSize(800, 1550))
        self.frame_scroll.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.frame_scroll.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_scroll.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_scroll.setObjectName("frame_scroll")
        self.title_mis_datos = QtWidgets.QLabel(self.frame_scroll)
        self.title_mis_datos.setGeometry(QtCore.QRect(320, 10, 201, 71))
        self.title_mis_datos.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.title_mis_datos.setObjectName("title_mis_datos")
        self.print_nickname = QtWidgets.QLabel(self.frame_scroll)
        self.print_nickname.setGeometry(QtCore.QRect(150, 100, 221, 61))
        self.print_nickname.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.print_nickname.setObjectName("print_nickname")
        self.print_nombre = QtWidgets.QLabel(self.frame_scroll)
        self.print_nombre.setGeometry(QtCore.QRect(150, 170, 201, 61))
        self.print_nombre.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.print_nombre.setObjectName("print_nombre")
        self.print_apellidos = QtWidgets.QLabel(self.frame_scroll)
        self.print_apellidos.setGeometry(QtCore.QRect(150, 240, 201, 61))
        self.print_apellidos.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.print_apellidos.setObjectName("print_apellidos")
        self.print_fecha_inicio = QtWidgets.QLabel(self.frame_scroll)
        self.print_fecha_inicio.setGeometry(QtCore.QRect(150, 310, 201, 61))
        self.print_fecha_inicio.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.print_fecha_inicio.setObjectName("print_fecha_inicio")
        self.mi_nickname = QtWidgets.QLabel(self.frame_scroll)
        self.mi_nickname.setGeometry(QtCore.QRect(490, 100, 381, 61))
        self.mi_nickname.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.mi_nickname.setObjectName("mi_nickname")
        self.mi_nombre = QtWidgets.QLabel(self.frame_scroll)
        self.mi_nombre.setGeometry(QtCore.QRect(490, 170, 381, 61))
        self.mi_nombre.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.mi_nombre.setObjectName("mi_nombre")
        self.mis_apellidos = QtWidgets.QLabel(self.frame_scroll)
        self.mis_apellidos.setGeometry(QtCore.QRect(490, 240, 391, 61))
        self.mis_apellidos.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.mis_apellidos.setObjectName("mis_apellidos")
        self.mi_fecha_de_ingreso = QtWidgets.QLabel(self.frame_scroll)
        self.mi_fecha_de_ingreso.setGeometry(QtCore.QRect(490, 310, 381, 61))
        self.mi_fecha_de_ingreso.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.mi_fecha_de_ingreso.setObjectName("mi_fecha_de_ingreso")
        self.title_mis_stats = QtWidgets.QLabel(self.frame_scroll)
        self.title_mis_stats.setGeometry(QtCore.QRect(260, 410, 351, 71))
        self.title_mis_stats.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.title_mis_stats.setObjectName("title_mis_stats")
        self.linea_separacion = QtWidgets.QFrame(self.frame_scroll)
        self.linea_separacion.setGeometry(QtCore.QRect(-20, 390, 911, 20))
        self.linea_separacion.setStyleSheet("")
        self.linea_separacion.setFrameShape(QtWidgets.QFrame.HLine)
        self.linea_separacion.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.linea_separacion.setObjectName("linea_separacion")
        self.print_test_realizados = QtWidgets.QLabel(self.frame_scroll)
        self.print_test_realizados.setGeometry(QtCore.QRect(280, 490, 251, 71))
        self.print_test_realizados.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.print_test_realizados.setObjectName("print_test_realizados")
        self.num_test_realizados = QtWidgets.QLabel(self.frame_scroll)
        self.num_test_realizados.setGeometry(QtCore.QRect(530, 490, 41, 71))
        self.num_test_realizados.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.num_test_realizados.setObjectName("num_test_realizados")
        self.title_ultimos_test = QtWidgets.QLabel(self.frame_scroll)
        self.title_ultimos_test.setGeometry(QtCore.QRect(240, 930, 531, 71))
        self.title_ultimos_test.setStyleSheet("color: rgb(9, 181, 203);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.title_ultimos_test.setObjectName("title_ultimos_test")
        self.frame_footer = QtWidgets.QFrame(self.frame_scroll)
        self.frame_footer.setGeometry(QtCore.QRect(-50, 1450, 941, 101))
        self.frame_footer.setStyleSheet("background-color: rgb(9, 181, 203);")
        self.frame_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_footer.setObjectName("frame_footer")
        self.print_footer = QtWidgets.QLabel(self.frame_footer)
        self.print_footer.setGeometry(QtCore.QRect(210, 30, 551, 41))
        self.print_footer.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.print_footer.setObjectName("print_footer")
        
        #self.diagrama_de_sectores = QtWidgets.QLabel(self.frame_scroll)
        #self.diagrama_de_sectores.setGeometry(QtCore.QRect(190, 580, 471, 321))
        #self.diagrama_de_sectores.setStyleSheet("COLOR: rgb(129, 255, 224);")
        #self.diagrama_de_sectores.setObjectName("diagrama_de_sectores")

        diagrama_de_sectores = Figure()
        canvas = FigureCanvas(diagrama_de_sectores)
        labels = ['A', 'B', 'C', 'D']
        sizes = [30, 25, 15, 30]
        explode = (0, 0, 0, 0)
        ax = diagrama_de_sectores.add_subplot()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        canvas.draw()
        width, height = canvas.get_width_height()
        image = QImage(canvas.buffer_rgba(), 300, 300, QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(image)
        self.diagrama_de_sectores = QtWidgets.QLabel(self.frame_scroll)
        self.diagrama_de_sectores.setPixmap(pixmap)
        self.diagrama_de_sectores.setGeometry(QtCore.QRect(170, 1020, 521, 341))
        self.diagrama_de_sectores.setObjectName("diagrama_de_barras")


        diagrama_de_barras = Figure()
        canvas = FigureCanvas(diagrama_de_barras)
        plt = diagrama_de_barras.add_subplot(111)
        categorias = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        valores = [25, 40, 30, 55, 70, 10, 40, 80]
        plt.bar(categorias, valores)
        #plt.style.use('Solarize_Light2')
        #plt.tick_params(axis='x', colors='#FFFFFF')  # Números en el eje x
        #plt.tick_params(axis='y', colors='#FFFFFF')  # Números en el eje y
        pixmap = canvas.grab().scaledToWidth(521) #ANCHO DIAGRAMA
        self.diagrama_de_barras = QtWidgets.QLabel(self.frame_scroll)
        self.diagrama_de_barras.setPixmap(pixmap)
        self.diagrama_de_barras.setGeometry(QtCore.QRect(170, 1020, 521, 341))
        self.diagrama_de_barras.setObjectName("diagrama_de_barras")



        self.verticalLayout_2.addWidget(self.frame_scroll)
        self.ventana_scroll.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.ventana_scroll)
        self.setCentralWidget(self.centralwidget)

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
        self.mi_nickname.setText(_translate("self", "Nombre de usuario:"))
        self.mi_nombre.setText(_translate("self", "Nombre de usuario:"))
        self.mis_apellidos.setText(_translate("self", "Nombre de usuario:"))
        self.mi_fecha_de_ingreso.setText(_translate("self", "Nombre de usuario:"))
        self.title_mis_stats.setText(_translate("self", "MIS ESTADÍSTICAS"))
        self.print_test_realizados.setText(_translate("self", "TEST REALIZADOS: "))
        self.num_test_realizados.setText(_translate("self", "XX"))
        self.diagrama_de_sectores.setText(_translate("self", ""))
        self.title_ultimos_test.setText(_translate("self", "ÚLTIMOS TEST REALIZADOS"))
        self.diagrama_de_barras.setText(_translate("self", ""))
        self.print_footer.setText(_translate("self", "©  2023AutoescuelaFastApp. Todos los derechos reservados.  "))

    @QtCore.pyqtSlot(QtGui.QCloseEvent)
    def closeEvent(self, event):
        self.cerrar_ventana_hija()
    
    def cerrar_ventana_hija(self):
        self.close()
        self.ventana_user.show()