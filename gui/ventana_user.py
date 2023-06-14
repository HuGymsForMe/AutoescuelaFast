from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

from gui.ventanauser.acerca_de import AcercaDe
from gui.ventanauser.realizar_test import RealizarTest

import os
import datetime

class VentanaUser(QMainWindow):
    def __init__(self, almacen_usuarios, almacen_partidas, nickname_var, ventana_login):
        super().__init__()
        self.almacen_usuarios = almacen_usuarios
        self.almacen_partidas = almacen_partidas
        self.nickname_var = nickname_var
        self.ventana_login = ventana_login
        self.ventana_acerca_de = None
        self.ventana_realizar_test = None
        self.RUTA_FOTO = os.path.abspath('./img/logofast.png')
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(948, 639)
        self.setMinimumSize(QtCore.QSize(948, 639))
        self.setMaximumSize(QtCore.QSize(948, 639))
        self.favicon = QIcon('./img/coche.png')
        self.setWindowIcon(self.favicon)
        self.boton_realizar_test = QtWidgets.QPushButton(self)
        self.boton_realizar_test.setGeometry(QtCore.QRect(90, 220, 521, 81))
        self.boton_realizar_test.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_realizar_test.setStyleSheet("QPushButton{\n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"background-color: #09B5CB;\n"
"color: #FFFFFF;\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #0ccbbb;\n"
"}")
        self.boton_realizar_test.setObjectName("boton_realizar_test")
        self.boton_mis_stats = QtWidgets.QPushButton(self)
        self.boton_mis_stats.setGeometry(QtCore.QRect(90, 340, 521, 81))
        self.boton_mis_stats.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_mis_stats.setStyleSheet("QPushButton{\n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"background-color: #09B5CB;\n"
"color: #FFFFFF;\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #0ccbbb;\n"
"}")
        self.boton_mis_stats.setObjectName("boton_mis_stats")
        self.boton_acerca_de = QtWidgets.QPushButton(self)
        self.boton_acerca_de.setGeometry(QtCore.QRect(90, 460, 521, 81))
        self.boton_acerca_de.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_acerca_de.setStyleSheet("QPushButton{\n"
"    font: 13pt \"MS Shell Dlg 2\";\n"
"background-color: #09B5CB;\n"
"color: #FFFFFF;\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #0ccbbb;\n"
"}")
        self.boton_acerca_de.setObjectName("boton_acerca_de")

        self.foto_coche = QtWidgets.QLabel(self)
        imagen_coche = QtGui.QImage(self.RUTA_FOTO)
        if imagen_coche.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_coche.setPixmap(QtGui.QPixmap.fromImage(imagen_coche))
        self.foto_coche.setGeometry(QtCore.QRect(530, -40, 491, 351))
        self.print_bienvenido_usuario = QtWidgets.QLabel(self)
        self.print_bienvenido_usuario.setGeometry(QtCore.QRect(120, 80, 571, 91))
        self.print_bienvenido_usuario.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\", italic;")
        self.print_bienvenido_usuario.setObjectName("print_bienvenido_usuario")
        self.frame_ventana_user = QtWidgets.QFrame(self)
        self.frame_ventana_user.setGeometry(QtCore.QRect(0, 0, 951, 641))
        self.frame_ventana_user.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.frame_ventana_user.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ventana_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ventana_user.setObjectName("frame_ventana_user")
        self.frame_ventana_user.raise_()
        self.print_fecha_actual = QtWidgets.QLabel(self)
        self.print_fecha_actual.setGeometry(QtCore.QRect(30, 10, 171, 61))
        self.print_fecha_actual.setStyleSheet("color: #FFFFFF;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_fecha_actual.setText(str(QtCore.Qt.AutoText))
        self.print_fecha_actual.setObjectName("print_fecha_actual")

        #EVENTO BOTONES
        self.boton_acerca_de.clicked.connect(self.abrir_ventana_acerca_de)
        self.boton_realizar_test.clicked.connect(self.abrir_ventana_realizar_test)
        self.print_fecha_actual.raise_()
        self.boton_realizar_test.raise_()
        self.boton_mis_stats.raise_()
        self.boton_acerca_de.raise_()
        self.foto_coche.raise_()
        self.print_bienvenido_usuario.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.move(500, 120)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "VentanaUsuario"))
        self.boton_realizar_test.setText(_translate("self", "REALIZAR TEST"))
        self.boton_mis_stats.setText(_translate("self", "MIS ESTADÍSTICAS"))
        self.boton_acerca_de.setText(_translate("self", "ACERCA DE"))
        fecha_actual = datetime.datetime.now().strftime("%H:%M:%S")
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_fecha)
        self.timer.start(1000) 
        self.print_fecha_actual.setText(_translate("self.form", fecha_actual))
        self.print_bienvenido_usuario.setText(_translate("self", f"Bienvenido {self.nickname_var}"))

    def actualizar_fecha(self):
        fecha_actual = datetime.datetime.now().strftime("%H:%M:%S")
        self.print_fecha_actual.setText(fecha_actual)

    def abrir_ventana_acerca_de(self):
        self.hide()
        self.ventana_acerca_de = AcercaDe(self)

    def abrir_ventana_realizar_test(self):
        self.hide()
        self.ventana_realizar_test = RealizarTest(self, self.almacen_partidas, self.nickname_var)

    @QtCore.pyqtSlot(QtGui.QCloseEvent)
    def closeEvent(self, event):
        self.cerrar_ventana_hija()
    
    def cerrar_ventana_hija(self):
        self.close()
        self.ventana_login.show()