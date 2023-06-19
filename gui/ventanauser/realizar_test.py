from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon

from gui.ventanauser.test_de_examen.test_1 import Test1
from gui.ventanauser.test_de_examen.test_2 import Test2
from gui.ventanauser.test_de_examen.test_3 import Test3
from gui.ventanauser.test_de_examen.test_4 import Test4
from gui.ventanauser.test_de_examen.test_5 import Test5
from gui.ventanauser.test_de_examen.test_6 import Test6
from gui.ventanauser.test_de_examen.test_7 import Test7
from gui.ventanauser.test_de_examen.test_8 import Test8
from gui.ventanauser.test_de_examen.test_9 import Test9
from gui.ventanauser.test_de_examen.test_10 import Test10

import os

class RealizarTest(QMainWindow):
    def __init__(self, ventana_user, almacen_partidas, nickname_var):
        super().__init__()
        self.ventana_user = ventana_user
        self.almacen_partidas = almacen_partidas
        self.nickname_var = nickname_var
        self.RUTA_CSS = os.path.abspath('./css/realizar_test.css')
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1017, 705)
        self.setMinimumSize(QtCore.QSize(1017, 705))
        self.setMaximumSize(QtCore.QSize(1017, 705))
        with open(self.RUTA_CSS) as f:
            self.setStyleSheet(f.read())

        #FAVICON
        self.favicon = QIcon('./img/coche.png')
        self.setWindowIcon(self.favicon)
        self.boton_test_1 = QtWidgets.QPushButton(self)
        self.boton_test_1.setGeometry(QtCore.QRect(60, 150, 431, 71))
        self.boton_test_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_1.setObjectName("boton_test_1")
        self.boton_test_2 = QtWidgets.QPushButton(self)
        self.boton_test_2.setGeometry(QtCore.QRect(60, 260, 431, 71))
        self.boton_test_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_2.setObjectName("boton_test_2")
        self.boton_test_3 = QtWidgets.QPushButton(self)
        self.boton_test_3.setGeometry(QtCore.QRect(60, 370, 431, 71))
        self.boton_test_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_3.setObjectName("boton_test_3")
        self.boton_test_4 = QtWidgets.QPushButton(self)
        self.boton_test_4.setGeometry(QtCore.QRect(60, 480, 431, 71))
        self.boton_test_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_4.setObjectName("boton_test_4")
        self.boton_test_5 = QtWidgets.QPushButton(self)
        self.boton_test_5.setGeometry(QtCore.QRect(60, 590, 431, 71))
        self.boton_test_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_5.setObjectName("boton_test_5")
        self.boton_test_6 = QtWidgets.QPushButton(self)
        self.boton_test_6.setGeometry(QtCore.QRect(520, 150, 431, 71))
        self.boton_test_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_6.setObjectName("boton_test_6")
        self.boton_test_7 = QtWidgets.QPushButton(self)
        self.boton_test_7.setGeometry(QtCore.QRect(520, 260, 431, 71))
        self.boton_test_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_7.setObjectName("boton_test_7")
        self.boton_test_8 = QtWidgets.QPushButton(self)
        self.boton_test_8.setGeometry(QtCore.QRect(520, 370, 431, 71))
        self.boton_test_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_8.setObjectName("boton_test_8")
        self.boton_test_9 = QtWidgets.QPushButton(self)
        self.boton_test_9.setGeometry(QtCore.QRect(520, 480, 431, 71))
        self.boton_test_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_9.setObjectName("boton_test_9")
        self.boton_test_10 = QtWidgets.QPushButton(self)
        self.boton_test_10.setGeometry(QtCore.QRect(520, 590, 431, 71))
        self.boton_test_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_test_10.setObjectName("boton_test_10")
        self.fondo_test = QtWidgets.QFrame(self)
        self.fondo_test.setGeometry(QtCore.QRect(-11, -11, 1041, 741))
        self.fondo_test.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fondo_test.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fondo_test.setObjectName("fondo_test")
        self.print_pregunta = QtWidgets.QLabel(self.fondo_test)
        self.print_pregunta.setGeometry(QtCore.QRect(300, 50, 441, 71))
        self.print_pregunta.setObjectName("print_pregunta")
        self.fondo_test.raise_()
        self.boton_test_1.raise_()
        self.boton_test_2.raise_()
        self.boton_test_3.raise_()
        self.boton_test_4.raise_()
        self.boton_test_5.raise_()
        self.boton_test_6.raise_()
        self.boton_test_7.raise_()
        self.boton_test_8.raise_()
        self.boton_test_9.raise_()
        self.boton_test_10.raise_()

        #EVENTOS BOTONES TEST
        self.boton_test_1.clicked.connect(self.abrir_test_1)
        self.boton_test_2.clicked.connect(self.abrir_test_2)
        self.boton_test_3.clicked.connect(self.abrir_test_3)
        self.boton_test_4.clicked.connect(self.abrir_test_4)
        self.boton_test_5.clicked.connect(self.abrir_test_5) 
        self.boton_test_6.clicked.connect(self.abrir_test_6)
        self.boton_test_7.clicked.connect(self.abrir_test_7)
        self.boton_test_8.clicked.connect(self.abrir_test_8)
        self.boton_test_9.clicked.connect(self.abrir_test_9)
        self.boton_test_10.clicked.connect(self.abrir_test_10)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "HacerTest"))
        self.boton_test_1.setText(_translate("self", "TEST 1"))
        self.boton_test_2.setText(_translate("self", "TEST 2"))
        self.boton_test_6.setText(_translate("self", "TEST 6"))
        self.boton_test_5.setText(_translate("self", "TEST 5"))
        self.boton_test_4.setText(_translate("self", "TEST 4"))
        self.boton_test_3.setText(_translate("self", "TEST 3"))
        self.boton_test_8.setText(_translate("self", "TEST 8"))
        self.boton_test_7.setText(_translate("self", "TEST 7"))
        self.boton_test_10.setText(_translate("self", "TEST 10"))
        self.boton_test_9.setText(_translate("self", "TEST 9"))
        self.print_pregunta.setText(_translate("self", "¿QUÉ TEST DESEAS REALIZAR?"))

    def abrir_test_1(self):
        self.hide()
        self.ventana_test_1 = Test1(self, self.almacen_partidas, self.nickname_var)

    def abrir_test_2(self):
        self.hide()
        self.ventana_test_2 = Test2(self, self.almacen_partidas, self.nickname_var)

    def abrir_test_3(self):
        self.hide()
        self.ventana_test_3 = Test3(self, self.almacen_partidas, self.nickname_var)

    def abrir_test_4(self):
        self.hide()
        self.ventana_test_4 = Test4(self, self.almacen_partidas, self.nickname_var)

    def abrir_test_5(self):
        self.hide()
        self.ventana_test_5 = Test5(self, self.almacen_partidas, self.nickname_var)

    def abrir_test_6(self):
        self.hide()
        self.ventana_test_6 = Test6(self, self.almacen_partidas, self.nickname_var)

    def abrir_test_7(self):
        self.hide()
        self.ventana_test_7 = Test7(self, self.almacen_partidas, self.nickname_var)

    def abrir_test_8(self):
        self.hide()
        self.ventana_test_8 = Test8(self, self.almacen_partidas, self.nickname_var)

    def abrir_test_9(self):
        self.hide()
        self.ventana_test_9 = Test9(self, self.almacen_partidas, self.nickname_var)

    def abrir_test_10(self):
        self.hide()
        self.ventana_test_10 = Test10(self, self.almacen_partidas, self.nickname_var)

    @QtCore.pyqtSlot(QtGui.QCloseEvent)
    def closeEvent(self, event):
        self.cerrar_ventana_hija()
    
    def cerrar_ventana_hija(self):
        self.close()
        self.ventana_user.show()