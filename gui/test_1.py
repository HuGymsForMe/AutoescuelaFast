import sys

from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication, QWidget, QVBoxLayout, QPushButton, QStackedLayout, QGridLayout, QMessageBox
from PyQt5.QtCore import QRect

from preguntas import *

import os


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainwindow = None
        self.RUTA_FOTO = os.path.abspath('./imgtest/imagen1.png')
        self.pregunta_1 = Frame1()
        self.frame_actual = None

        #CRONOMETRO
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.elapsed_time = 0
        self.start_time()

    def setupUi(self):
        self.mainwindow = QtWidgets.QMainWindow()
        self.mainwindow.setObjectName("TEST 1")
        self.mainwindow.resize(830, 820)
        self.mainwindow.setMinimumSize(QtCore.QSize(830, 820))
        self.mainwindow.setMaximumSize(QtCore.QSize(830, 820))
        self.centralwidget = QtWidgets.QWidget(self.mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_botones = QtWidgets.QFrame(self.mainwindow)
        self.frame_botones.setGeometry(QtCore.QRect(-10, 570, 861, 261))
        self.frame_botones.setStyleSheet("background-color: rgb(9, 181, 203);")
        self.frame_botones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_botones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botones.setObjectName("frame")

        self.boton_014 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_014.setGeometry(QtCore.QRect(280, 100, 50, 50))
        self.boton_014.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_014.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_014.setObjectName("boton_014")
        self.boton_021 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_021.setGeometry(QtCore.QRect(40, 170, 50, 50))
        self.boton_021.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_021.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_021.setObjectName("boton_021")
        self.boton_018 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_018.setGeometry(QtCore.QRect(600, 100, 50, 50))
        self.boton_018.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_018.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_018.setObjectName("boton_018")
        self.boton_007 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_007.setGeometry(QtCore.QRect(520, 30, 50, 50))
        self.boton_007.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_007.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_007.setObjectName("boton_007")
        self.boton_019 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_019.setGeometry(QtCore.QRect(680, 100, 50, 50))
        self.boton_019.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_019.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_019.setObjectName("boton_019")
        self.boton_002 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_002.setGeometry(QtCore.QRect(120, 30, 50, 50))
        self.boton_002.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_002.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_002.setObjectName("boton_002")
        self.boton_009 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_009.setGeometry(QtCore.QRect(680, 30, 50, 50))
        self.boton_009.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_009.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_009.setObjectName("boton_009")
        self.boton_017 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_017.setGeometry(QtCore.QRect(520, 100, 50, 50))
        self.boton_017.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_017.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_017.setObjectName("boton_017")
        self.boton_026 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_026.setGeometry(QtCore.QRect(440, 170, 50, 50))
        self.boton_026.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_026.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_026.setObjectName("boton_026")
        self.boton_022 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_022.setGeometry(QtCore.QRect(120, 170, 50, 50))
        self.boton_022.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_022.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_022.setObjectName("boton_022")
        self.boton_029 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_029.setGeometry(QtCore.QRect(680, 170, 50, 50))
        self.boton_029.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_029.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_029.setObjectName("boton_029")
        self.boton_013 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_013.setGeometry(QtCore.QRect(200, 100, 50, 50))
        self.boton_013.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_013.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_013.setObjectName("boton_013")
        self.boton_005 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_005.setGeometry(QtCore.QRect(360, 30, 50, 50))
        self.boton_005.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_005.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_005.setObjectName("boton_005")
        self.boton_012 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_012.setGeometry(QtCore.QRect(120, 100, 50, 50))
        self.boton_012.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_012.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_012.setObjectName("boton_012")
        self.boton_008 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_008.setGeometry(QtCore.QRect(600, 30, 50, 50))
        self.boton_008.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_008.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_008.setObjectName("boton_008")
        self.boton_027 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_027.setGeometry(QtCore.QRect(520, 170, 50, 50))
        self.boton_027.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_027.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_027.setObjectName("boton_027")
        self.boton_010 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_010.setGeometry(QtCore.QRect(760, 30, 50, 50))
        self.boton_010.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_010.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_010.setObjectName("boton_010")
        self.boton_001 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_001.setGeometry(QtCore.QRect(40, 30, 50, 50))
        self.boton_001.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_001.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_001.setObjectName("boton_001")
        self.boton_028 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_028.setGeometry(QtCore.QRect(600, 170, 50, 50))
        self.boton_028.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_028.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_028.setObjectName("boton_028")
        self.boton_025 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_025.setGeometry(QtCore.QRect(360, 170, 50, 50))
        self.boton_025.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_025.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_025.setObjectName("boton_025")
        self.boton_023 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_023.setGeometry(QtCore.QRect(200, 170, 50, 50))
        self.boton_023.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_023.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_023.setObjectName("boton_023")
        self.boton_003 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_003.setGeometry(QtCore.QRect(200, 30, 50, 50))
        self.boton_003.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_003.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_003.setObjectName("boton_003")
        self.boton_006 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_006.setGeometry(QtCore.QRect(440, 30, 50, 50))
        self.boton_006.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_006.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_006.setObjectName("boton_006")
        self.boton_024 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_024.setGeometry(QtCore.QRect(280, 170, 50, 50))
        self.boton_024.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_024.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_024.setObjectName("boton_024")
        self.boton_020 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_020.setGeometry(QtCore.QRect(760, 100, 50, 50))
        self.boton_020.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_020.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_020.setObjectName("boton_020")
        self.boton_015 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_015.setGeometry(QtCore.QRect(360, 100, 50, 50))
        self.boton_015.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_015.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_015.setObjectName("boton_015")
        self.boton_004 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_004.setGeometry(QtCore.QRect(280, 30, 50, 50))
        self.boton_004.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_004.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_004.setObjectName("boton_004")
        self.boton_011 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_011.setGeometry(QtCore.QRect(40, 100, 50, 50))
        self.boton_011.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_011.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_011.setObjectName("boton_011")
        self.boton_016 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_016.setGeometry(QtCore.QRect(440, 100, 50, 50))
        self.boton_016.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_016.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_016.setObjectName("boton_016")
        self.boton_030 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_030.setGeometry(QtCore.QRect(760, 170, 50, 50))
        self.boton_030.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_030.setStyleSheet("QPushButton{\n"
"background-color: rgb(56, 56, 56);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_030.setObjectName("boton_030")
        self.boton_finalizar = QtWidgets.QPushButton(self.mainwindow)
        self.boton_finalizar.setGeometry(QtCore.QRect(640, 20, 161, 51))
        self.boton_finalizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_finalizar.setStyleSheet("QPushButton{\n"
"background-color: rgb(9, 181, 203);\n"
"color: #FFFFFF;\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(86, 86, 86)\n"
"}")
        self.boton_finalizar.setObjectName("boton_finalizar")
        self.print_cronometro = QtWidgets.QLabel(self.mainwindow)
        self.print_cronometro.setGeometry(QtCore.QRect(30, 20, 111, 41))
        self.print_cronometro.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.print_cronometro.setObjectName("print_cronometro")

        '''self.frame_pregunta1 = QtWidgets.QFrame(self.mainwindow)
        self.frame_pregunta1.setGeometry(QtCore.QRect(-10, 0, 861, 600))
        self.frame_pregunta1.setStyleSheet("background-color: #383838;")
        self.frame_pregunta1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pregunta1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pregunta1.lower()

        self.titulo_pregunta1 = QtWidgets.QLabel(self.frame_pregunta1)
        self.titulo_pregunta1.setGeometry(QtCore.QRect(250, 10, 250, 70))
        self.titulo_pregunta1.setStyleSheet("background-color: #FFFFFF;")
        self.titulo_pregunta1.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";")
        self.titulo_pregunta1.setObjectName("titulo_pregunta1")

        self.imagen_pregunta1 = QtWidgets.QLabel(self.frame_pregunta1)
        self.imagen_pregunta1.setGeometry(QtCore.QRect(280, 200, 300, 300))
        imagen_pregunta1 = QtGui.QImage(self.RUTA_FOTO)
        if imagen_pregunta1.isNull():
            print("Error al cargar la imagen")
        else:
            self.imagen_pregunta1.setPixmap(QtGui.QPixmap.fromImage(imagen_pregunta1))

        self.imagen_pregunta1.setText("")
        self.imagen_pregunta1.setObjectName("imagen_pregunta1")

        self.radio_button_1 = QtWidgets.QRadioButton(self.frame_pregunta1)
        self.radio_button_1.setGeometry(QtCore.QRect(400, 200, 450, 50))
        self.radio_button_2 = QtWidgets.QRadioButton(self.frame_pregunta1)
        self.radio_button_2.setGeometry(QtCore.QRect(400, 300, 450, 50))
        self.radio_button_3 = QtWidgets.QRadioButton(self.frame_pregunta1)
        self.radio_button_3.setGeometry(QtCore.QRect(400, 400, 450, 20))
'''     
        self.boton_finalizar.clicked.connect(self.recoger_crono) #RECOGE EL TIEMPO QUE HA HECHO EL USUARIO
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.mainwindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.mainwindow.setWindowTitle(_translate("self.mainwindow", "Test1"))
        self.boton_014.setText(_translate("self.mainwindow", "14"))
        self.boton_021.setText(_translate("self.mainwindow", "21"))
        self.boton_018.setText(_translate("self.mainwindow", "18"))
        self.boton_007.setText(_translate("self.mainwindow", "7"))
        self.boton_019.setText(_translate("self.mainwindow", "19"))
        self.boton_002.setText(_translate("self.mainwindow", "2"))
        self.boton_009.setText(_translate("self.mainwindow", "9"))
        self.boton_017.setText(_translate("self.mainwindow", "17"))
        self.boton_026.setText(_translate("self.mainwindow", "26"))
        self.boton_022.setText(_translate("self.mainwindow", "22"))
        self.boton_029.setText(_translate("self.mainwindow", "29"))
        self.boton_013.setText(_translate("self.mainwindow", "13"))
        self.boton_005.setText(_translate("self.mainwindow", "5"))
        self.boton_012.setText(_translate("self.mainwindow", "12"))
        self.boton_008.setText(_translate("self.mainwindow", "8"))
        self.boton_027.setText(_translate("self.mainwindow", "27"))
        self.boton_010.setText(_translate("self.mainwindow", "10"))
        self.boton_001.setText(_translate("self.mainwindow", "1"))
        self.boton_028.setText(_translate("self.mainwindow", "28"))
        self.boton_025.setText(_translate("self.mainwindow", "25"))
        self.boton_023.setText(_translate("self.mainwindow", "23"))
        self.boton_003.setText(_translate("self.mainwindow", "3"))
        self.boton_006.setText(_translate("self.mainwindow", "6"))
        self.boton_024.setText(_translate("self.mainwindow", "24"))
        self.boton_020.setText(_translate("self.mainwindow", "20"))
        self.boton_015.setText(_translate("self.mainwindow", "15"))
        self.boton_004.setText(_translate("self.mainwindow", "4"))
        self.boton_011.setText(_translate("self.mainwindow", "11"))
        self.boton_016.setText(_translate("self.mainwindow", "16"))
        self.boton_030.setText(_translate("self.mainwindow", "30"))
        self.boton_finalizar.setText(_translate("self.mainwindow", "FINALIZAR TEST"))
        self.print_cronometro.setText(_translate("self.mainwindow", "00:00"))
        #self.titulo_pregunta1.setText(_translate("self.mainwindow", "PREGUNTA 1"))
        self.mostrar_frame1()


        '''self.radio_button_1.setText(_translate("self.mainwindow", "Vía reservada para automóviles."))
        self.radio_button_2.setText(_translate("self.mainwindow", "Calzada obligatoria para automóviles, excepto\n motocicletas sin sidecar."))
        self.radio_button_3.setText(_translate("self.mainwindow", "Calzada obligatoria para automóviles."))'''
        self.mainwindow.show()


    def start_time(self):
        self.timer.start(1000) 

    def update_time(self):
        self.elapsed_time += 1
        self.minutes = self.elapsed_time // 60
        self.seconds = self.elapsed_time % 60
        self.time_str = f"{self.minutes:02d}:{self.seconds:02d}"
        self.print_cronometro.setText(f"{self.time_str}")

    def recoger_crono(self):
        recoger_crono = self.time_str
        QMessageBox.information(None, "Hola", f"Has tardado {recoger_crono} segundos")


    def mostrar_frame1(self):
        layout_1 = QtWidgets.QVBoxLayout()
        layout_1.addLayout(self.pregunta_1.setupUi())
        #layout = self.centralwidget.setLayout(self.pregunta_1.setupUi())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = Ui_MainWindow()
    ventana_principal.mainwindow = ventana_principal  # Asignar la instancia a self.login
    ventana_principal.setupUi()
    sys.exit(app.exec_())
