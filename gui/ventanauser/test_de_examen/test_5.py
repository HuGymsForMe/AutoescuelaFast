from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

from almacen.almacenpreguntas import AlmacenPreguntas

import os

class Test5(QMainWindow):
    class NumeroPregunta:
        PREGUNTA_1 = 120
        PREGUNTA_2 = 121
        PREGUNTA_3 = 122
        PREGUNTA_4 = 123
        PREGUNTA_5 = 124
        PREGUNTA_6 = 125
        PREGUNTA_7 = 126
        PREGUNTA_8 = 127
        PREGUNTA_9 = 128
        PREGUNTA_10 = 129
        PREGUNTA_11 = 130
        PREGUNTA_12 = 131
        PREGUNTA_13 = 132
        PREGUNTA_14 = 133
        PREGUNTA_15 = 134
        PREGUNTA_16 = 135
        PREGUNTA_17 = 136
        PREGUNTA_18 = 137
        PREGUNTA_19 = 138
        PREGUNTA_20 = 139
        PREGUNTA_21 = 140
        PREGUNTA_22 = 141
        PREGUNTA_23 = 142
        PREGUNTA_24 = 143
        PREGUNTA_25 = 144
        PREGUNTA_26 = 145
        PREGUNTA_27 = 146
        PREGUNTA_28 = 147
        PREGUNTA_29 = 148
        PREGUNTA_30 = 149

    def __init__(self, ventana_realizar_test, almacen_partidas, nickname_var):
        super().__init__()
        self.ventana_realizar_test = ventana_realizar_test
        self.almacen_partidas = almacen_partidas
        self.nickname_var = nickname_var
        self.RUTA_FOTO = os.path.abspath('../autoescuelafast/gui/imgtest')
        self.RUTA_CSS = os.path.abspath('./css/tests_examen.css')

        #CRONOMETRO
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.elapsed_time = 0
        self.start_time()
        self.setupUi()

        #ESTADÍSTICAS
        self.no_contestadas = 30
        self.acertadas = 0
        self.falladas = 0

    def setupUi(self):
        self.almacen_preguntas = AlmacenPreguntas()
        self.almacen_preguntas.importar_preguntas()
        self.resize(846, 682)
        self.setMinimumSize(QtCore.QSize(846, 682))
        self.setMaximumSize(QtCore.QSize(846, 682))

        with open(self.RUTA_CSS) as f:
            self.setStyleSheet(f.read())

        #FAVICON
        self.favicon = QIcon('./img/coche.png')
        self.setWindowIcon(self.favicon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.frame_body = QtWidgets.QFrame(self.centralwidget)
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.frame_botones = QtWidgets.QFrame(self.frame_body)
        self.frame_botones.setGeometry(QtCore.QRect(0, 440, 901, 241))
        self.frame_botones.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_botones.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botones.setObjectName("frame_botones")
        
        self.boton_014 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_014.setGeometry(QtCore.QRect(280, 100, 50, 50))
        self.boton_014.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_014.setProperty("class", "botones_preguntas")
        self.boton_021 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_021.setGeometry(QtCore.QRect(40, 170, 50, 50))
        self.boton_021.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_021.setProperty("class", "botones_preguntas")
        self.boton_018 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_018.setGeometry(QtCore.QRect(600, 100, 50, 50))
        self.boton_018.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_018.setProperty("class", "botones_preguntas")
        self.boton_007 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_007.setGeometry(QtCore.QRect(520, 30, 50, 50))
        self.boton_007.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_007.setProperty("class", "botones_preguntas")
        self.boton_019 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_019.setGeometry(QtCore.QRect(680, 100, 50, 50))
        self.boton_019.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_019.setProperty("class", "botones_preguntas")
        self.boton_002 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_002.setGeometry(QtCore.QRect(120, 30, 50, 50))
        self.boton_002.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_002.setProperty("class", "botones_preguntas")
        self.boton_009 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_009.setGeometry(QtCore.QRect(680, 30, 50, 50))
        self.boton_009.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_009.setProperty("class", "botones_preguntas")
        self.boton_017 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_017.setGeometry(QtCore.QRect(520, 100, 50, 50))
        self.boton_017.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_017.setProperty("class", "botones_preguntas")
        self.boton_026 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_026.setGeometry(QtCore.QRect(440, 170, 50, 50))
        self.boton_026.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_026.setProperty("class", "botones_preguntas")
        self.boton_022 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_022.setGeometry(QtCore.QRect(120, 170, 50, 50))
        self.boton_022.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_022.setProperty("class", "botones_preguntas")
        self.boton_029 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_029.setGeometry(QtCore.QRect(680, 170, 50, 50))
        self.boton_029.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_029.setProperty("class", "botones_preguntas")
        self.boton_013 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_013.setGeometry(QtCore.QRect(200, 100, 50, 50))
        self.boton_013.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_013.setProperty("class", "botones_preguntas")
        self.boton_005 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_005.setGeometry(QtCore.QRect(360, 30, 50, 50))
        self.boton_005.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_005.setProperty("class", "botones_preguntas")
        self.boton_012 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_012.setGeometry(QtCore.QRect(120, 100, 50, 50))
        self.boton_012.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_012.setProperty("class", "botones_preguntas")
        self.boton_008 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_008.setGeometry(QtCore.QRect(600, 30, 50, 50))
        self.boton_008.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_008.setProperty("class", "botones_preguntas")
        self.boton_027 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_027.setGeometry(QtCore.QRect(520, 170, 50, 50))
        self.boton_027.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_027.setProperty("class", "botones_preguntas")
        self.boton_010 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_010.setGeometry(QtCore.QRect(760, 30, 50, 50))
        self.boton_010.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_010.setProperty("class", "botones_preguntas")
        self.boton_001 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_001.setGeometry(QtCore.QRect(40, 30, 50, 50))
        self.boton_001.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_001.setProperty("class", "botones_preguntas")
        self.boton_028 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_028.setGeometry(QtCore.QRect(600, 170, 50, 50))
        self.boton_028.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_028.setProperty("class", "botones_preguntas")
        self.boton_025 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_025.setGeometry(QtCore.QRect(360, 170, 50, 50))
        self.boton_025.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_025.setProperty("class", "botones_preguntas")
        self.boton_023 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_023.setGeometry(QtCore.QRect(200, 170, 50, 50))
        self.boton_023.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_023.setProperty("class", "botones_preguntas")
        self.boton_003 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_003.setGeometry(QtCore.QRect(200, 30, 50, 50))
        self.boton_003.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_003.setProperty("class", "botones_preguntas")
        self.boton_006 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_006.setGeometry(QtCore.QRect(440, 30, 50, 50))
        self.boton_006.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_006.setProperty("class", "botones_preguntas")
        self.boton_024 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_024.setGeometry(QtCore.QRect(280, 170, 50, 50))
        self.boton_024.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_024.setProperty("class", "botones_preguntas")
        self.boton_020 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_020.setGeometry(QtCore.QRect(760, 100, 50, 50))
        self.boton_020.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_020.setProperty("class", "botones_preguntas")
        self.boton_015 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_015.setGeometry(QtCore.QRect(360, 100, 50, 50))
        self.boton_015.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_015.setProperty("class", "botones_preguntas")
        self.boton_004 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_004.setGeometry(QtCore.QRect(280, 30, 50, 50))
        self.boton_004.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_004.setProperty("class", "botones_preguntas")
        self.boton_011 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_011.setGeometry(QtCore.QRect(40, 100, 50, 50))
        self.boton_011.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_011.setProperty("class", "botones_preguntas")
        self.boton_016 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_016.setGeometry(QtCore.QRect(440, 100, 50, 50))
        self.boton_016.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_016.setProperty("class", "botones_preguntas")
        self.boton_030 = QtWidgets.QPushButton(self.frame_botones)
        self.boton_030.setGeometry(QtCore.QRect(760, 170, 50, 50))
        self.boton_030.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_030.setProperty("class", "botones_preguntas")

        self.frame_central = QtWidgets.QFrame(self.frame_body)
        self.frame_central.setGeometry(QtCore.QRect(-11, -1, 891, 441))
        self.frame_central.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tiempo = QtWidgets.QFrame(self.frame_central)
        self.frame_tiempo.setGeometry(QtCore.QRect(10, 0, 161, 91))
        self.frame_tiempo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tiempo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.print_cronometro = QtWidgets.QLabel(self.frame_tiempo)
        self.print_cronometro.setGeometry(QtCore.QRect(30, 20, 111, 41))
        self.print_cronometro.setObjectName("print_cronometro")
        self.frame_finalizar = QtWidgets.QFrame(self.frame_central)
        self.frame_finalizar.setGeometry(QtCore.QRect(660, 0, 201, 91))
        self.frame_finalizar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_finalizar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.boton_finalizar = QtWidgets.QPushButton(self.frame_finalizar)
        self.boton_finalizar.setGeometry(QtCore.QRect(20, 20, 161, 51))
        self.boton_finalizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_finalizar.setObjectName("boton_finalizar")
        self.frame_num_pregunta = QtWidgets.QFrame(self.frame_central)
        self.frame_num_pregunta.setGeometry(QtCore.QRect(170, 0, 491, 91))
        self.frame_num_pregunta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_num_pregunta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ventanas_num_preguntas = QtWidgets.QStackedWidget(self.frame_num_pregunta)
        self.ventanas_num_preguntas.setGeometry(QtCore.QRect(0, 10, 521, 71))
        self.num_pregunta_1 = QtWidgets.QWidget()
        self.title_pregunta_1 = QtWidgets.QLabel(self.num_pregunta_1)
        self.title_pregunta_1.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_1.setProperty("class", "title_pregunta")        
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_1)
        self.num_pregunta_8 = QtWidgets.QWidget()
        self.title_pregunta_8 = QtWidgets.QLabel(self.num_pregunta_8)
        self.title_pregunta_8.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_8.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_8)
        self.num_pregunta_9 = QtWidgets.QWidget()
        self.title_pregunta_9 = QtWidgets.QLabel(self.num_pregunta_9)
        self.title_pregunta_9.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_9.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_9)
        self.num_pregunta_10 = QtWidgets.QWidget()
        self.title_pregunta_10 = QtWidgets.QLabel(self.num_pregunta_10)
        self.title_pregunta_10.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_10.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_10)
        self.num_pregunta_11 = QtWidgets.QWidget()
        self.title_pregunta_11 = QtWidgets.QLabel(self.num_pregunta_11)
        self.title_pregunta_11.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_11.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_11)
        self.num_pregunta_12 = QtWidgets.QWidget()
        self.title_pregunta_12 = QtWidgets.QLabel(self.num_pregunta_12)
        self.title_pregunta_12.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_12.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_12)
        self.num_pregunta_13 = QtWidgets.QWidget()
        self.title_pregunta_13 = QtWidgets.QLabel(self.num_pregunta_13)
        self.title_pregunta_13.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_13.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_13)
        self.num_pregunta_14 = QtWidgets.QWidget()
        self.title_pregunta_14 = QtWidgets.QLabel(self.num_pregunta_14)
        self.title_pregunta_14.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_14.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_14)
        self.num_pregunta_15 = QtWidgets.QWidget()
        self.title_pregunta_15 = QtWidgets.QLabel(self.num_pregunta_15)
        self.title_pregunta_15.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_15.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_15)
        self.num_pregunta_16 = QtWidgets.QWidget()
        self.title_pregunta_16 = QtWidgets.QLabel(self.num_pregunta_16)
        self.title_pregunta_16.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_16.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_16)
        self.num_pregunta_17 = QtWidgets.QWidget()
        self.title_pregunta_17 = QtWidgets.QLabel(self.num_pregunta_17)
        self.title_pregunta_17.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_17.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_17)
        self.num_pregunta_18 = QtWidgets.QWidget()
        self.title_pregunta_18 = QtWidgets.QLabel(self.num_pregunta_18)
        self.title_pregunta_18.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_18.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_18)
        self.num_pregunta_19 = QtWidgets.QWidget()
        self.title_pregunta_19 = QtWidgets.QLabel(self.num_pregunta_19)
        self.title_pregunta_19.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_19.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_19)
        self.num_pregunta_20 = QtWidgets.QWidget()
        self.title_pregunta_20 = QtWidgets.QLabel(self.num_pregunta_20)
        self.title_pregunta_20.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_20.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_20)
        self.num_pregunta_21 = QtWidgets.QWidget()
        self.title_pregunta_21 = QtWidgets.QLabel(self.num_pregunta_21)
        self.title_pregunta_21.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_21.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_21)
        self.num_pregunta_22 = QtWidgets.QWidget()
        self.title_pregunta_22 = QtWidgets.QLabel(self.num_pregunta_22)
        self.title_pregunta_22.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_22.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_22)
        self.num_pregunta_23 = QtWidgets.QWidget()
        self.title_pregunta_23 = QtWidgets.QLabel(self.num_pregunta_23)
        self.title_pregunta_23.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_23.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_23)
        self.num_pregunta_24 = QtWidgets.QWidget()
        self.title_pregunta_24 = QtWidgets.QLabel(self.num_pregunta_24)
        self.title_pregunta_24.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_24.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_24)
        self.num_pregunta_25 = QtWidgets.QWidget()
        self.title_pregunta_25 = QtWidgets.QLabel(self.num_pregunta_25)
        self.title_pregunta_25.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_25.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_25)
        self.num_pregunta_26 = QtWidgets.QWidget()
        self.title_pregunta_26 = QtWidgets.QLabel(self.num_pregunta_26)
        self.title_pregunta_26.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_26.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_26)
        self.num_pregunta_27 = QtWidgets.QWidget()
        self.title_pregunta_27 = QtWidgets.QLabel(self.num_pregunta_27)
        self.title_pregunta_27.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_27.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_27)
        self.num_pregunta_28 = QtWidgets.QWidget()
        self.title_pregunta_28 = QtWidgets.QLabel(self.num_pregunta_28)
        self.title_pregunta_28.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_28.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_28)
        self.num_pregunta_29 = QtWidgets.QWidget()
        self.title_pregunta_29 = QtWidgets.QLabel(self.num_pregunta_29)
        self.title_pregunta_29.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_29.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_29)
        self.num_pregunta_30 = QtWidgets.QWidget()
        self.title_pregunta_30 = QtWidgets.QLabel(self.num_pregunta_30)
        self.title_pregunta_30.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_30.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_30)
        self.num_pregunta_3 = QtWidgets.QWidget()
        self.title_pregunta_3 = QtWidgets.QLabel(self.num_pregunta_3)
        self.title_pregunta_3.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_3.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_3)
        self.num_pregunta_4 = QtWidgets.QWidget()
        self.title_pregunta_4 = QtWidgets.QLabel(self.num_pregunta_4)
        self.title_pregunta_4.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_4.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_4)
        self.num_pregunta_5 = QtWidgets.QWidget()
        self.title_pregunta_5 = QtWidgets.QLabel(self.num_pregunta_5)
        self.title_pregunta_5.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_5.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_5)
        self.num_pregunta_7 = QtWidgets.QWidget()
        self.title_pregunta_7 = QtWidgets.QLabel(self.num_pregunta_7)
        self.title_pregunta_7.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_7.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_7)
        self.num_pregunta_6 = QtWidgets.QWidget()
        self.title_pregunta_6 = QtWidgets.QLabel(self.num_pregunta_6)
        self.title_pregunta_6.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_6.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_6)
        self.num_pregunta_2 = QtWidgets.QWidget()
        self.title_pregunta_2 = QtWidgets.QLabel(self.num_pregunta_2)
        self.title_pregunta_2.setGeometry(QtCore.QRect(120, 0, 251, 61))
        self.title_pregunta_2.setProperty("class", "title_pregunta")
        self.ventanas_num_preguntas.addWidget(self.num_pregunta_2)
        self.frame_pregunta = QtWidgets.QFrame(self.frame_central)
        self.frame_pregunta.setGeometry(QtCore.QRect(10, 80, 871, 371))
        self.frame_pregunta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pregunta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_pregunta)
        self.ventanas_preguntas = QtWidgets.QStackedWidget(self.frame_pregunta)
        self.ventanas_preguntas.setFocusPolicy(QtCore.Qt.WheelFocus)
        
        self.pregunta_1 = QtWidgets.QWidget()
        self.enunciado_1 = QtWidgets.QLabel(self.pregunta_1)
        self.enunciado_1.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_1.setProperty("class", "enunciado")
        self.foto_1 = QtWidgets.QLabel(self.pregunta_1)
        self.foto_1.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_1 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen121.jpg'))
        if imagen_1.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_1.setPixmap(QtGui.QPixmap.fromImage(imagen_1))
        self.opcion_1_3 = QtWidgets.QRadioButton(self.pregunta_1)
        self.opcion_1_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.opcion_1_2 = QtWidgets.QRadioButton(self.pregunta_1)
        self.opcion_1_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_1_1 = QtWidgets.QRadioButton(self.pregunta_1)
        self.opcion_1_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_1)
        self.pregunta_20 = QtWidgets.QWidget()
        self.enunciado_20 = QtWidgets.QLabel(self.pregunta_20)
        self.enunciado_20.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_20.setProperty("class", "enunciado")
        self.foto_20 = QtWidgets.QLabel(self.pregunta_20)
        self.foto_20.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_20 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen140.jpg'))
        if imagen_20.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_20.setPixmap(QtGui.QPixmap.fromImage(imagen_20))
        self.opcion_20_1 = QtWidgets.QRadioButton(self.pregunta_20)
        self.opcion_20_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_20_2 = QtWidgets.QRadioButton(self.pregunta_20)
        self.opcion_20_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_20_3 = QtWidgets.QRadioButton(self.pregunta_20)
        self.opcion_20_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_20)
        self.pregunta_21 = QtWidgets.QWidget()
        self.enunciado_21 = QtWidgets.QLabel(self.pregunta_21)
        self.enunciado_21.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_21.setProperty("class", "enunciado")
        self.foto_21 = QtWidgets.QLabel(self.pregunta_21)
        self.foto_21.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_21 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen141.jpg'))
        if imagen_21.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_21.setPixmap(QtGui.QPixmap.fromImage(imagen_21))
        self.opcion_21_1 = QtWidgets.QRadioButton(self.pregunta_21)
        self.opcion_21_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_21_2 = QtWidgets.QRadioButton(self.pregunta_21)
        self.opcion_21_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_21_3 = QtWidgets.QRadioButton(self.pregunta_21)
        self.opcion_21_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_21)
        self.pregunta_22 = QtWidgets.QWidget()
        self.enunciado_22 = QtWidgets.QLabel(self.pregunta_22)
        self.enunciado_22.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_22.setProperty("class", "enunciado")
        self.foto_22 = QtWidgets.QLabel(self.pregunta_22)
        self.foto_22.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_22 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen142.jpg'))
        if imagen_22.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_22.setPixmap(QtGui.QPixmap.fromImage(imagen_22))
        self.opcion_22_2 = QtWidgets.QRadioButton(self.pregunta_22)
        self.opcion_22_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_22_1 = QtWidgets.QRadioButton(self.pregunta_22)
        self.opcion_22_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_22_3 = QtWidgets.QRadioButton(self.pregunta_22)
        self.opcion_22_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_22)
        self.pregunta_23 = QtWidgets.QWidget()
        self.enunciado_23 = QtWidgets.QLabel(self.pregunta_23)
        self.enunciado_23.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_23.setProperty("class", "enunciado")
        self.foto_23 = QtWidgets.QLabel(self.pregunta_23)
        self.foto_23.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_23 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen143.jpg'))
        if imagen_23.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_23.setPixmap(QtGui.QPixmap.fromImage(imagen_23))
        self.opcion_23_1 = QtWidgets.QRadioButton(self.pregunta_23)
        self.opcion_23_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_23_2 = QtWidgets.QRadioButton(self.pregunta_23)
        self.opcion_23_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_23_3 = QtWidgets.QRadioButton(self.pregunta_23)
        self.opcion_23_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_23)
        self.pregunta_24 = QtWidgets.QWidget()
        self.enunciado_24 = QtWidgets.QLabel(self.pregunta_24)
        self.enunciado_24.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_24.setProperty("class", "enunciado")
        self.foto_24 = QtWidgets.QLabel(self.pregunta_24)
        self.foto_24.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_24 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen144.jpg'))
        if imagen_24.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_24.setPixmap(QtGui.QPixmap.fromImage(imagen_24))
        self.opcion_24_1 = QtWidgets.QRadioButton(self.pregunta_24)
        self.opcion_24_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_24_2 = QtWidgets.QRadioButton(self.pregunta_24)
        self.opcion_24_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_24_3 = QtWidgets.QRadioButton(self.pregunta_24)
        self.opcion_24_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_24)
        self.pregunta_25 = QtWidgets.QWidget()
        self.enunciado_25 = QtWidgets.QLabel(self.pregunta_25)
        self.enunciado_25.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_25.setProperty("class", "enunciado")
        self.foto_25 = QtWidgets.QLabel(self.pregunta_25)
        self.foto_25.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_25 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen145.jpg'))
        if imagen_25.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_25.setPixmap(QtGui.QPixmap.fromImage(imagen_25))
        self.opcion_25_1 = QtWidgets.QRadioButton(self.pregunta_25)
        self.opcion_25_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_25_2 = QtWidgets.QRadioButton(self.pregunta_25)
        self.opcion_25_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_25_3 = QtWidgets.QRadioButton(self.pregunta_25)
        self.opcion_25_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_25)
        self.pregunta_26 = QtWidgets.QWidget()
        self.enunciado_26 = QtWidgets.QLabel(self.pregunta_26)
        self.enunciado_26.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_26.setProperty("class", "enunciado")
        self.foto_26 = QtWidgets.QLabel(self.pregunta_26)
        self.foto_26.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_26 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen146.jpg'))
        if imagen_26.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_26.setPixmap(QtGui.QPixmap.fromImage(imagen_26))
        self.opcion_26_1 = QtWidgets.QRadioButton(self.pregunta_26)
        self.opcion_26_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_26_2 = QtWidgets.QRadioButton(self.pregunta_26)
        self.opcion_26_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_26_3 = QtWidgets.QRadioButton(self.pregunta_26)
        self.opcion_26_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_26)
        self.pregunta_27 = QtWidgets.QWidget()
        self.enunciado_27 = QtWidgets.QLabel(self.pregunta_27)
        self.enunciado_27.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_27.setProperty("class", "enunciado")
        self.foto_27 = QtWidgets.QLabel(self.pregunta_27)
        self.foto_27.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_27 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen147.jpg'))
        if imagen_27.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_27.setPixmap(QtGui.QPixmap.fromImage(imagen_27))
        self.opcion_27_1 = QtWidgets.QRadioButton(self.pregunta_27)
        self.opcion_27_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_27_2 = QtWidgets.QRadioButton(self.pregunta_27)
        self.opcion_27_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_27_3 = QtWidgets.QRadioButton(self.pregunta_27)
        self.opcion_27_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_27)
        self.pregunta_28 = QtWidgets.QWidget()
        self.enunciado_28 = QtWidgets.QLabel(self.pregunta_28)
        self.enunciado_28.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_28.setProperty("class", "enunciado")
        self.foto_28 = QtWidgets.QLabel(self.pregunta_28)
        self.foto_28.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_28 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen148.jpg'))
        if imagen_28.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_28.setPixmap(QtGui.QPixmap.fromImage(imagen_28))
        self.opcion_28_1 = QtWidgets.QRadioButton(self.pregunta_28)
        self.opcion_28_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_28_2 = QtWidgets.QRadioButton(self.pregunta_28)
        self.opcion_28_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_28_3 = QtWidgets.QRadioButton(self.pregunta_28)
        self.opcion_28_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_28)
        self.pregunta_29 = QtWidgets.QWidget()
        self.enunciado_29 = QtWidgets.QLabel(self.pregunta_29)
        self.enunciado_29.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_29.setProperty("class", "enunciado")
        self.foto_29 = QtWidgets.QLabel(self.pregunta_29)
        self.foto_29.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_29 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen149.jpg'))
        if imagen_29.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_29.setPixmap(QtGui.QPixmap.fromImage(imagen_29))
        self.opcion_29_1 = QtWidgets.QRadioButton(self.pregunta_29)
        self.opcion_29_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_29_2 = QtWidgets.QRadioButton(self.pregunta_29)
        self.opcion_29_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_29_3 = QtWidgets.QRadioButton(self.pregunta_29)
        self.opcion_29_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_29)
        self.pregunta_30 = QtWidgets.QWidget()
        self.enunciado_30 = QtWidgets.QLabel(self.pregunta_30)
        self.enunciado_30.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_30.setProperty("class", "enunciado")
        self.foto_30 = QtWidgets.QLabel(self.pregunta_30)
        self.foto_30.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_30 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen150.jpg'))
        if imagen_30.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_30.setPixmap(QtGui.QPixmap.fromImage(imagen_30))
        self.opcion_30_1 = QtWidgets.QRadioButton(self.pregunta_30)
        self.opcion_30_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_30_2 = QtWidgets.QRadioButton(self.pregunta_30)
        self.opcion_30_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_30_3 = QtWidgets.QRadioButton(self.pregunta_30)
        self.opcion_30_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_30)
        self.pregunta_3 = QtWidgets.QWidget()
        self.enunciado_3 = QtWidgets.QLabel(self.pregunta_3)
        self.enunciado_3.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_3.setProperty("class", "enunciado")
        self.foto_3 = QtWidgets.QLabel(self.pregunta_3)
        self.foto_3.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_3 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen123.jpg'))
        if imagen_3.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_3.setPixmap(QtGui.QPixmap.fromImage(imagen_3))
        self.opcion_3_1 = QtWidgets.QRadioButton(self.pregunta_3)
        self.opcion_3_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_3_2 = QtWidgets.QRadioButton(self.pregunta_3)
        self.opcion_3_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_3_3 = QtWidgets.QRadioButton(self.pregunta_3)
        self.opcion_3_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_3)
        self.pregunta_4 = QtWidgets.QWidget()
        self.enunciado_4 = QtWidgets.QLabel(self.pregunta_4)
        self.enunciado_4.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_4.setProperty("class", "enunciado")
        self.foto_4 = QtWidgets.QLabel(self.pregunta_4)
        self.foto_4.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_4 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen124.jpg'))
        if imagen_4.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_4.setPixmap(QtGui.QPixmap.fromImage(imagen_4))
        self.opcion_4_1 = QtWidgets.QRadioButton(self.pregunta_4)
        self.opcion_4_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_4_3 = QtWidgets.QRadioButton(self.pregunta_4)
        self.opcion_4_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.opcion_4_2 = QtWidgets.QRadioButton(self.pregunta_4)
        self.opcion_4_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_4)
        self.pregunta_6 = QtWidgets.QWidget()
        self.enunciado_6 = QtWidgets.QLabel(self.pregunta_6)
        self.enunciado_6.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_6.setProperty("class", "enunciado")
        self.foto_6 = QtWidgets.QLabel(self.pregunta_6)
        self.foto_6.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_6 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen126.jpg'))
        if imagen_6.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_6.setPixmap(QtGui.QPixmap.fromImage(imagen_6))
        self.opcion_6_1 = QtWidgets.QRadioButton(self.pregunta_6)
        self.opcion_6_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_6_2 = QtWidgets.QRadioButton(self.pregunta_6)
        self.opcion_6_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_6_3 = QtWidgets.QRadioButton(self.pregunta_6)
        self.opcion_6_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_6)
        self.pregunta_7 = QtWidgets.QWidget()
        self.enunciado_7 = QtWidgets.QLabel(self.pregunta_7)
        self.enunciado_7.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_7.setProperty("class", "enunciado")
        self.foto_7 = QtWidgets.QLabel(self.pregunta_7)
        self.foto_7.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_7 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen127.jpg'))
        if imagen_7.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_7.setPixmap(QtGui.QPixmap.fromImage(imagen_7))
        self.opcion_7_1 = QtWidgets.QRadioButton(self.pregunta_7)
        self.opcion_7_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_7_2 = QtWidgets.QRadioButton(self.pregunta_7)
        self.opcion_7_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_7_3 = QtWidgets.QRadioButton(self.pregunta_7)
        self.opcion_7_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_7)
        self.pregunta_8 = QtWidgets.QWidget()
        self.enunciado_8 = QtWidgets.QLabel(self.pregunta_8)
        self.enunciado_8.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_8.setProperty("class", "enunciado")
        self.foto_8 = QtWidgets.QLabel(self.pregunta_8)
        self.foto_8.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_8 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen128.jpg'))
        if imagen_8.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_8.setPixmap(QtGui.QPixmap.fromImage(imagen_8))
        self.opcion_8_1 = QtWidgets.QRadioButton(self.pregunta_8)
        self.opcion_8_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_8_2 = QtWidgets.QRadioButton(self.pregunta_8)
        self.opcion_8_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_8_3 = QtWidgets.QRadioButton(self.pregunta_8)
        self.opcion_8_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_8)
        self.pregunta_9 = QtWidgets.QWidget()
        self.enunciado_9 = QtWidgets.QLabel(self.pregunta_9)
        self.enunciado_9.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_9.setProperty("class", "enunciado")
        self.foto_9 = QtWidgets.QLabel(self.pregunta_9)
        self.foto_9.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_9 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen129.jpg'))
        if imagen_9.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_9.setPixmap(QtGui.QPixmap.fromImage(imagen_9))
        self.opcion_9_1 = QtWidgets.QRadioButton(self.pregunta_9)
        self.opcion_9_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_9_2 = QtWidgets.QRadioButton(self.pregunta_9)
        self.opcion_9_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_9_3 = QtWidgets.QRadioButton(self.pregunta_9)
        self.opcion_9_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_9)
        self.pregunta_10 = QtWidgets.QWidget()
        self.enunciado_10 = QtWidgets.QLabel(self.pregunta_10)
        self.enunciado_10.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_10.setProperty("class", "enunciado")
        self.foto_10 = QtWidgets.QLabel(self.pregunta_10)
        self.foto_10.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_10 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen130.jpg'))
        if imagen_10.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_10.setPixmap(QtGui.QPixmap.fromImage(imagen_10))
        self.opcion_10_1 = QtWidgets.QRadioButton(self.pregunta_10)
        self.opcion_10_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_10_2 = QtWidgets.QRadioButton(self.pregunta_10)
        self.opcion_10_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_10_3 = QtWidgets.QRadioButton(self.pregunta_10)
        self.opcion_10_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_10)
        self.pregunta_11 = QtWidgets.QWidget()
        self.enunciado_11 = QtWidgets.QLabel(self.pregunta_11)
        self.enunciado_11.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_11.setProperty("class", "enunciado")
        self.foto_11 = QtWidgets.QLabel(self.pregunta_11)
        self.foto_11.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_11 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen131.jpg'))
        if imagen_11.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_11.setPixmap(QtGui.QPixmap.fromImage(imagen_11))
        self.opcion_11_1 = QtWidgets.QRadioButton(self.pregunta_11)
        self.opcion_11_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_11_2 = QtWidgets.QRadioButton(self.pregunta_11)
        self.opcion_11_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_11_3 = QtWidgets.QRadioButton(self.pregunta_11)
        self.opcion_11_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_11)
        self.pregunta_12 = QtWidgets.QWidget()
        self.enunciado_12 = QtWidgets.QLabel(self.pregunta_12)
        self.enunciado_12.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_12.setProperty("class", "enunciado")
        self.foto_12 = QtWidgets.QLabel(self.pregunta_12)
        self.foto_12.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_12 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen132.jpg'))
        if imagen_12.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_12.setPixmap(QtGui.QPixmap.fromImage(imagen_12))
        self.opcion_12_1 = QtWidgets.QRadioButton(self.pregunta_12)
        self.opcion_12_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_12_2 = QtWidgets.QRadioButton(self.pregunta_12)
        self.opcion_12_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_12_3 = QtWidgets.QRadioButton(self.pregunta_12)
        self.opcion_12_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_12)
        self.pregunta_13 = QtWidgets.QWidget()
        self.enunciado_13 = QtWidgets.QLabel(self.pregunta_13)
        self.enunciado_13.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_13.setProperty("class", "enunciado")
        self.foto_13 = QtWidgets.QLabel(self.pregunta_13)
        self.foto_13.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_13 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen133.jpg'))
        if imagen_13.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_13.setPixmap(QtGui.QPixmap.fromImage(imagen_13))
        self.opcion_13_1 = QtWidgets.QRadioButton(self.pregunta_13)
        self.opcion_13_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_13_2 = QtWidgets.QRadioButton(self.pregunta_13)
        self.opcion_13_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_13_3 = QtWidgets.QRadioButton(self.pregunta_13)
        self.opcion_13_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_13)
        self.pregunta_17 = QtWidgets.QWidget()
        self.enunciado_17 = QtWidgets.QLabel(self.pregunta_17)
        self.enunciado_17.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_17.setProperty("class", "enunciado")
        self.foto_17 = QtWidgets.QLabel(self.pregunta_17)
        self.foto_17.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_17 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen137.jpg'))
        if imagen_17.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_17.setPixmap(QtGui.QPixmap.fromImage(imagen_17))
        self.opcion_17_1 = QtWidgets.QRadioButton(self.pregunta_17)
        self.opcion_17_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_17_2 = QtWidgets.QRadioButton(self.pregunta_17)
        self.opcion_17_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_17_3 = QtWidgets.QRadioButton(self.pregunta_17)
        self.opcion_17_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_17)
        self.pregunta_18 = QtWidgets.QWidget()
        self.enunciado_18 = QtWidgets.QLabel(self.pregunta_18)
        self.enunciado_18.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_18.setProperty("class", "enunciado")
        self.foto_18 = QtWidgets.QLabel(self.pregunta_18)
        self.foto_18.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_18 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen138.jpg'))
        if imagen_18.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_18.setPixmap(QtGui.QPixmap.fromImage(imagen_18))
        self.opcion_18_1 = QtWidgets.QRadioButton(self.pregunta_18)
        self.opcion_18_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_18_2 = QtWidgets.QRadioButton(self.pregunta_18)
        self.opcion_18_2.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.opcion_18_3 = QtWidgets.QRadioButton(self.pregunta_18)
        self.opcion_18_3.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_18)
        self.pregunta_19 = QtWidgets.QWidget()
        self.enunciado_19 = QtWidgets.QLabel(self.pregunta_19)
        self.enunciado_19.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_19.setProperty("class", "enunciado")
        self.foto_19 = QtWidgets.QLabel(self.pregunta_19)
        self.foto_19.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_19 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen139.jpg'))
        if imagen_19.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_19.setPixmap(QtGui.QPixmap.fromImage(imagen_19))
        self.opcion_19_1 = QtWidgets.QRadioButton(self.pregunta_19)
        self.opcion_19_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_19_2 = QtWidgets.QRadioButton(self.pregunta_19)
        self.opcion_19_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_19_3 = QtWidgets.QRadioButton(self.pregunta_19)
        self.opcion_19_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_19)
        self.pregunta_14 = QtWidgets.QWidget()
        self.enunciado_14 = QtWidgets.QLabel(self.pregunta_14)
        self.enunciado_14.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_14.setProperty("class", "enunciado")
        self.foto_14 = QtWidgets.QLabel(self.pregunta_14)
        self.foto_14.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_14 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen134.jpg'))
        if imagen_14.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_14.setPixmap(QtGui.QPixmap.fromImage(imagen_14))
        self.opcion_14_1 = QtWidgets.QRadioButton(self.pregunta_14)
        self.opcion_14_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_14_2 = QtWidgets.QRadioButton(self.pregunta_14)
        self.opcion_14_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_14_3 = QtWidgets.QRadioButton(self.pregunta_14)
        self.opcion_14_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_14)
        self.pregunta_15 = QtWidgets.QWidget()
        self.enunciado_15 = QtWidgets.QLabel(self.pregunta_15)
        self.enunciado_15.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_15.setProperty("class", "enunciado")
        self.foto_15 = QtWidgets.QLabel(self.pregunta_15)
        self.foto_15.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_15 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen135.jpg'))
        if imagen_15.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_15.setPixmap(QtGui.QPixmap.fromImage(imagen_15))
        self.opcion_15_1 = QtWidgets.QRadioButton(self.pregunta_15)
        self.opcion_15_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_15_2 = QtWidgets.QRadioButton(self.pregunta_15)
        self.opcion_15_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_15_3 = QtWidgets.QRadioButton(self.pregunta_15)
        self.opcion_15_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_15)
        self.pregunta_16 = QtWidgets.QWidget()
        self.enunciado_16 = QtWidgets.QLabel(self.pregunta_16)
        self.enunciado_16.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_16.setProperty("class", "enunciado")
        self.foto_16 = QtWidgets.QLabel(self.pregunta_16)
        self.foto_16.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_16 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen136.jpg'))
        if imagen_16.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_16.setPixmap(QtGui.QPixmap.fromImage(imagen_16))
        self.opcion_16_2 = QtWidgets.QRadioButton(self.pregunta_16)
        self.opcion_16_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_16_1 = QtWidgets.QRadioButton(self.pregunta_16)
        self.opcion_16_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_16_3 = QtWidgets.QRadioButton(self.pregunta_16)
        self.opcion_16_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_16)
        self.pregunta_5 = QtWidgets.QWidget()
        self.enunciado_5 = QtWidgets.QLabel(self.pregunta_5)
        self.enunciado_5.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_5.setProperty("class", "enunciado")
        self.foto_5 = QtWidgets.QLabel(self.pregunta_5)
        self.foto_5.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_5 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen125.jpg'))
        if imagen_5.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_5.setPixmap(QtGui.QPixmap.fromImage(imagen_5))
        self.opcion_5_1 = QtWidgets.QRadioButton(self.pregunta_5)
        self.opcion_5_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_5_2 = QtWidgets.QRadioButton(self.pregunta_5)
        self.opcion_5_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_5_3 = QtWidgets.QRadioButton(self.pregunta_5)
        self.opcion_5_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_5)
        self.pregunta_2 = QtWidgets.QWidget()
        self.enunciado_2 = QtWidgets.QLabel(self.pregunta_2)
        self.enunciado_2.setGeometry(QtCore.QRect(0, 0, 851, 71))
        self.enunciado_2.setProperty("class", "enunciado")
        self.foto_2 = QtWidgets.QLabel(self.pregunta_2)
        self.foto_2.setGeometry(QtCore.QRect(-10, 80, 331, 271))
        imagen_2 = QtGui.QImage(os.path.join(self.RUTA_FOTO, 'imagen122.jpg'))
        if imagen_2.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_2.setPixmap(QtGui.QPixmap.fromImage(imagen_2))
        self.opcion_2_1 = QtWidgets.QRadioButton(self.pregunta_2)
        self.opcion_2_1.setGeometry(QtCore.QRect(330, 80, 501, 91))
        self.opcion_2_2 = QtWidgets.QRadioButton(self.pregunta_2)
        self.opcion_2_2.setGeometry(QtCore.QRect(330, 170, 501, 91))
        self.opcion_2_3 = QtWidgets.QRadioButton(self.pregunta_2)
        self.opcion_2_3.setGeometry(QtCore.QRect(330, 260, 501, 91))
        self.ventanas_preguntas.addWidget(self.pregunta_2)
        self.verticalLayout_2.addWidget(self.ventanas_preguntas)
        self.verticalLayout.addWidget(self.frame_body)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        self.ventanas_num_preguntas.setCurrentIndex(0)
        self.ventanas_preguntas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "TEST 5"))
        self.boton_014.setText(_translate("self", "14"))
        self.boton_021.setText(_translate("self", "21"))
        self.boton_018.setText(_translate("self", "18"))
        self.boton_007.setText(_translate("self", "7"))
        self.boton_019.setText(_translate("self", "19"))
        self.boton_002.setText(_translate("self", "2"))
        self.boton_009.setText(_translate("self", "9"))
        self.boton_017.setText(_translate("self", "17"))
        self.boton_026.setText(_translate("self", "26"))
        self.boton_022.setText(_translate("self", "22"))
        self.boton_029.setText(_translate("self", "29"))
        self.boton_013.setText(_translate("self", "13"))
        self.boton_005.setText(_translate("self", "5"))
        self.boton_012.setText(_translate("self", "12"))
        self.boton_008.setText(_translate("self", "8"))
        self.boton_027.setText(_translate("self", "27"))
        self.boton_010.setText(_translate("self", "10"))
        self.boton_001.setText(_translate("self", "1"))
        self.boton_028.setText(_translate("self", "28"))
        self.boton_025.setText(_translate("self", "25"))
        self.boton_023.setText(_translate("self", "23"))
        self.boton_003.setText(_translate("self", "3"))
        self.boton_006.setText(_translate("self", "6"))
        self.boton_024.setText(_translate("self", "24"))
        self.boton_020.setText(_translate("self", "20"))
        self.boton_015.setText(_translate("self", "15"))
        self.boton_004.setText(_translate("self", "4"))
        self.boton_011.setText(_translate("self", "11"))
        self.boton_016.setText(_translate("self", "16"))
        self.boton_030.setText(_translate("self", "30"))
        self.print_cronometro.setText(_translate("self", "00:00"))
        self.boton_finalizar.setText(_translate("self", "FINALIZAR TEST"))
        self.title_pregunta_1.setText(_translate("self", "PREGUNTA 1"))
        self.title_pregunta_8.setText(_translate("self", "PREGUNTA 8"))
        self.title_pregunta_9.setText(_translate("self", "PREGUNTA 9"))
        self.title_pregunta_10.setText(_translate("self", "PREGUNTA 10"))
        self.title_pregunta_11.setText(_translate("self", "PREGUNTA 11"))
        self.title_pregunta_12.setText(_translate("self", "PREGUNTA 12"))
        self.title_pregunta_13.setText(_translate("self", "PREGUNTA 13"))
        self.title_pregunta_14.setText(_translate("self", "PREGUNTA 14"))
        self.title_pregunta_15.setText(_translate("self", "PREGUNTA 15"))
        self.title_pregunta_16.setText(_translate("self", "PREGUNTA 16"))
        self.title_pregunta_17.setText(_translate("self", "PREGUNTA 17"))
        self.title_pregunta_18.setText(_translate("self", "PREGUNTA 18"))
        self.title_pregunta_19.setText(_translate("self", "PREGUNTA 19"))
        self.title_pregunta_20.setText(_translate("self", "PREGUNTA 20"))
        self.title_pregunta_21.setText(_translate("self", "PREGUNTA 21"))
        self.title_pregunta_22.setText(_translate("self", "PREGUNTA 22"))
        self.title_pregunta_23.setText(_translate("self", "PREGUNTA 23"))
        self.title_pregunta_24.setText(_translate("self", "PREGUNTA 24"))
        self.title_pregunta_25.setText(_translate("self", "PREGUNTA 25"))
        self.title_pregunta_26.setText(_translate("self", "PREGUNTA 26"))
        self.title_pregunta_27.setText(_translate("self", "PREGUNTA 27"))
        self.title_pregunta_28.setText(_translate("self", "PREGUNTA 28"))
        self.title_pregunta_29.setText(_translate("self", "PREGUNTA 29"))
        self.title_pregunta_30.setText(_translate("self", "PREGUNTA 30"))
        self.title_pregunta_3.setText(_translate("self", "PREGUNTA 3"))
        self.title_pregunta_4.setText(_translate("self", "PREGUNTA 4"))
        self.title_pregunta_5.setText(_translate("self", "PREGUNTA 5"))
        self.title_pregunta_7.setText(_translate("self", "PREGUNTA 7"))
        self.title_pregunta_6.setText(_translate("self", "PREGUNTA 6"))
        self.title_pregunta_2.setText(_translate("self", "PREGUNTA 2"))
        self.enunciado_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_1]._enunciado}"))
        self.foto_1.setText(_translate("self", ""))
        self.opcion_1_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_1]._opcion_1}"))
        self.opcion_1_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_1]._opcion_2}"))
        self.opcion_1_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_1]._opcion_3}"))
        self.enunciado_20.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_20]._enunciado}"))
        self.foto_20.setText(_translate("self", ""))
        self.opcion_20_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_20]._opcion_1}"))
        self.opcion_20_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_20]._opcion_2}"))
        self.opcion_20_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_20]._opcion_3}"))
        self.enunciado_21.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_21]._enunciado}"))
        self.foto_21.setText(_translate("self", ""))
        self.opcion_21_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_21]._opcion_1}"))
        self.opcion_21_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_21]._opcion_2}"))
        self.opcion_21_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_21]._opcion_3}"))
        self.enunciado_22.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_22]._enunciado}"))
        self.foto_22.setText(_translate("self", ""))
        self.opcion_22_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_22]._opcion_1}"))
        self.opcion_22_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_22]._opcion_2}"))
        self.opcion_22_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_22]._opcion_3}"))
        self.enunciado_23.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_23]._enunciado}"))
        self.foto_23.setText(_translate("self", ""))
        self.opcion_23_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_23]._opcion_1}"))
        self.opcion_23_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_23]._opcion_2}"))
        self.opcion_23_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_23]._opcion_3}"))
        self.enunciado_24.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_24]._enunciado}"))
        self.foto_24.setText(_translate("self", ""))
        self.opcion_24_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_24]._opcion_1}"))
        self.opcion_24_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_24]._opcion_2}"))
        self.opcion_24_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_24]._opcion_3}"))
        self.enunciado_25.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_25]._enunciado}"))
        self.foto_25.setText(_translate("self", ""))
        self.opcion_25_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_25]._opcion_1}"))
        self.opcion_25_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_25]._opcion_2}"))
        self.opcion_25_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_25]._opcion_3}"))
        self.enunciado_26.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_26]._enunciado}"))
        self.foto_26.setText(_translate("self", ""))
        self.opcion_26_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_26]._opcion_1}"))
        self.opcion_26_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_26]._opcion_2}"))
        self.opcion_26_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_26]._opcion_3}"))
        self.enunciado_27.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_27]._enunciado}"))
        self.foto_27.setText(_translate("self", ""))
        self.opcion_27_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_27]._opcion_1}"))
        self.opcion_27_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_27]._opcion_2}"))
        self.opcion_27_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_27]._opcion_3}"))
        self.enunciado_28.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_28]._enunciado}"))
        self.foto_28.setText(_translate("self", ""))
        self.opcion_28_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_28]._opcion_1}"))
        self.opcion_28_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_28]._opcion_2}"))
        self.opcion_28_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_28]._opcion_3}"))
        self.enunciado_29.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_29]._enunciado}"))
        self.foto_29.setText(_translate("self", ""))
        self.opcion_29_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_29]._opcion_1}"))
        self.opcion_29_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_29]._opcion_2}"))
        self.opcion_29_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_29]._opcion_3}"))
        self.enunciado_30.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_30]._enunciado}"))
        self.foto_30.setText(_translate("self", ""))
        self.opcion_30_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_30]._opcion_1}"))
        self.opcion_30_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_30]._opcion_2}"))
        self.opcion_30_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_30]._opcion_3}"))
        self.enunciado_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_3]._enunciado}"))
        self.foto_3.setText(_translate("self", ""))
        self.opcion_3_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_3]._opcion_1}"))
        self.opcion_3_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_3]._opcion_2}"))
        self.opcion_3_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_3]._opcion_3}"))
        self.enunciado_4.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_4]._enunciado}"))
        self.foto_4.setText(_translate("self", ""))
        self.opcion_4_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_4]._opcion_1}"))
        self.opcion_4_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_4]._opcion_2}"))
        self.opcion_4_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_4]._opcion_3}"))
        self.enunciado_6.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_6]._enunciado}"))
        self.foto_6.setText(_translate("self", ""))
        self.opcion_6_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_6]._opcion_1}"))
        self.opcion_6_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_6]._opcion_2}"))
        self.opcion_6_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_6]._opcion_3}"))
        self.enunciado_7.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_7]._enunciado}"))
        self.foto_7.setText(_translate("self", ""))
        self.opcion_7_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_7]._opcion_1}"))
        self.opcion_7_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_7]._opcion_2}"))
        self.opcion_7_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_7]._opcion_3}"))
        self.enunciado_8.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_8]._enunciado}"))
        self.foto_8.setText(_translate("self", ""))
        self.opcion_8_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_8]._opcion_1}"))
        self.opcion_8_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_8]._opcion_2}"))
        self.opcion_8_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_8]._opcion_3}"))
        self.enunciado_9.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_9]._enunciado}"))
        self.foto_9.setText(_translate("self", ""))
        self.opcion_9_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_9]._opcion_1}"))
        self.opcion_9_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_9]._opcion_2}"))
        self.opcion_9_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_9]._opcion_3}"))
        self.enunciado_10.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_10]._enunciado}"))
        self.foto_10.setText(_translate("self", ""))
        self.opcion_10_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_10]._opcion_1}"))
        self.opcion_10_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_10]._opcion_2}"))
        self.opcion_10_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_10]._opcion_3}"))
        self.enunciado_11.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_11]._enunciado}"))
        self.foto_11.setText(_translate("self", ""))
        self.opcion_11_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_11]._opcion_1}"))
        self.opcion_11_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_11]._opcion_2}"))
        self.opcion_11_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_11]._opcion_3}"))
        self.enunciado_12.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_12]._enunciado}"))
        self.foto_12.setText(_translate("self", ""))
        self.opcion_12_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_12]._opcion_1}"))
        self.opcion_12_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_12]._opcion_2}"))
        self.opcion_12_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_12]._opcion_3}"))
        self.enunciado_13.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_13]._enunciado}"))
        self.foto_13.setText(_translate("self", ""))
        self.opcion_13_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_13]._opcion_1}"))
        self.opcion_13_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_13]._opcion_2}"))
        self.opcion_13_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_13]._opcion_3}"))
        self.enunciado_17.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_17]._enunciado}"))
        self.foto_17.setText(_translate("self", ""))
        self.opcion_17_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_17]._opcion_1}"))
        self.opcion_17_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_17]._opcion_2}"))
        self.opcion_17_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_17]._opcion_3}"))
        self.enunciado_18.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_18]._enunciado}"))
        self.foto_18.setText(_translate("self", ""))
        self.opcion_18_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_18]._opcion_1}"))
        self.opcion_18_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_18]._opcion_2}"))
        self.opcion_18_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_18]._opcion_3}"))
        self.enunciado_19.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_19]._enunciado}"))
        self.foto_19.setText(_translate("self", ""))
        self.opcion_19_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_19]._opcion_1}"))
        self.opcion_19_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_19]._opcion_2}"))
        self.opcion_19_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_19]._opcion_3}"))
        self.enunciado_14.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_14]._enunciado}"))
        self.foto_14.setText(_translate("self", ""))
        self.opcion_14_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_14]._opcion_1}"))
        self.opcion_14_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_14]._opcion_2}"))
        self.opcion_14_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_14]._opcion_3}"))
        self.enunciado_15.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_15]._enunciado}"))
        self.foto_15.setText(_translate("self", ""))
        self.opcion_15_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_15]._opcion_1}"))
        self.opcion_15_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_15]._opcion_2}"))
        self.opcion_15_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_15]._opcion_3}"))
        self.enunciado_16.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_16]._enunciado}"))
        self.foto_16.setText(_translate("self", ""))
        self.opcion_16_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_16]._opcion_1}"))
        self.opcion_16_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_16]._opcion_2}"))
        self.opcion_16_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_16]._opcion_3}"))
        self.enunciado_5.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_5]._enunciado}"))
        self.foto_5.setText(_translate("self", ""))
        self.opcion_5_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_5]._opcion_1}"))
        self.opcion_5_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_5]._opcion_2}"))
        self.opcion_5_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_5]._opcion_3}"))
        self.enunciado_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_2]._enunciado}"))
        self.foto_2.setText(_translate("self", ""))
        self.opcion_2_1.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_2]._opcion_1}"))
        self.opcion_2_2.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_2]._opcion_2}"))
        self.opcion_2_3.setText(_translate("self", f"{self.almacen_preguntas._preguntas[self.NumeroPregunta.PREGUNTA_2]._opcion_3}"))

        #CAMBIAR DE PREGUNTA
        self.boton_001.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_1))
        self.boton_001.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_1))
        self.boton_002.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_2))
        self.boton_002.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_2))
        self.boton_003.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_3))
        self.boton_003.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_3))
        self.boton_004.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_4))
        self.boton_004.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_4))
        self.boton_005.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_5))
        self.boton_005.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_5))
        self.boton_006.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_6))
        self.boton_006.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_6))
        self.boton_007.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_7))
        self.boton_007.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_7))
        self.boton_008.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_8))
        self.boton_008.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_8))
        self.boton_009.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_9))
        self.boton_009.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_9))
        self.boton_010.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_10))
        self.boton_010.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_10))
        self.boton_011.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_11))
        self.boton_011.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_11))
        self.boton_012.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_12))
        self.boton_012.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_12))
        self.boton_013.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_13))
        self.boton_013.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_13))
        self.boton_014.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_14))
        self.boton_014.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_14))
        self.boton_015.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_15))
        self.boton_015.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_15))
        self.boton_016.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_16))
        self.boton_016.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_16))
        self.boton_017.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_17))
        self.boton_017.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_17))
        self.boton_018.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_18))
        self.boton_018.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_18))
        self.boton_019.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_19))
        self.boton_019.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_19))
        self.boton_020.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_20))
        self.boton_020.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_20))
        self.boton_021.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_21))
        self.boton_021.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_21))
        self.boton_022.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_22))
        self.boton_022.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_22))
        self.boton_023.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_23))
        self.boton_023.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_23))
        self.boton_024.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_24))
        self.boton_024.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_24))
        self.boton_025.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_25))
        self.boton_025.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_25))
        self.boton_026.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_26))
        self.boton_026.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_26))
        self.boton_027.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_27))
        self.boton_027.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_27))
        self.boton_028.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_28))
        self.boton_028.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_28))
        self.boton_029.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_29))
        self.boton_029.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_29))
        self.boton_030.clicked.connect(lambda: self.ventanas_preguntas.setCurrentWidget(self.pregunta_30))
        self.boton_030.clicked.connect(lambda: self.ventanas_num_preguntas.setCurrentWidget(self.num_pregunta_30))

        #RADIO BUTTONS CLICKADOS
        self.opcion_1_1.toggled.connect(self.devolver_respuesta_1)
        self.opcion_1_2.toggled.connect(self.devolver_respuesta_1)
        self.opcion_1_3.toggled.connect(self.devolver_respuesta_1)
        self.opcion_2_1.toggled.connect(self.devolver_respuesta_2)
        self.opcion_2_2.toggled.connect(self.devolver_respuesta_2)
        self.opcion_2_3.toggled.connect(self.devolver_respuesta_2)
        self.opcion_3_1.toggled.connect(self.devolver_respuesta_3)
        self.opcion_3_2.toggled.connect(self.devolver_respuesta_3)
        self.opcion_3_3.toggled.connect(self.devolver_respuesta_3)
        self.opcion_4_1.toggled.connect(self.devolver_respuesta_4)
        self.opcion_4_2.toggled.connect(self.devolver_respuesta_4)
        self.opcion_4_3.toggled.connect(self.devolver_respuesta_4)
        self.opcion_5_1.toggled.connect(self.devolver_respuesta_5)
        self.opcion_5_2.toggled.connect(self.devolver_respuesta_5)
        self.opcion_5_3.toggled.connect(self.devolver_respuesta_5)
        self.opcion_6_1.toggled.connect(self.devolver_respuesta_6)
        self.opcion_6_2.toggled.connect(self.devolver_respuesta_6)
        self.opcion_6_3.toggled.connect(self.devolver_respuesta_6)
        self.opcion_7_1.toggled.connect(self.devolver_respuesta_7)
        self.opcion_7_2.toggled.connect(self.devolver_respuesta_7)
        self.opcion_7_3.toggled.connect(self.devolver_respuesta_7)
        self.opcion_8_1.toggled.connect(self.devolver_respuesta_8)
        self.opcion_8_2.toggled.connect(self.devolver_respuesta_8)
        self.opcion_8_3.toggled.connect(self.devolver_respuesta_8)
        self.opcion_9_1.toggled.connect(self.devolver_respuesta_9)
        self.opcion_9_2.toggled.connect(self.devolver_respuesta_9)
        self.opcion_9_3.toggled.connect(self.devolver_respuesta_9)
        self.opcion_10_1.toggled.connect(self.devolver_respuesta_10)
        self.opcion_10_2.toggled.connect(self.devolver_respuesta_10)
        self.opcion_10_3.toggled.connect(self.devolver_respuesta_10)
        self.opcion_11_1.toggled.connect(self.devolver_respuesta_11)
        self.opcion_11_2.toggled.connect(self.devolver_respuesta_11)
        self.opcion_11_3.toggled.connect(self.devolver_respuesta_11)
        self.opcion_12_1.toggled.connect(self.devolver_respuesta_12)
        self.opcion_12_2.toggled.connect(self.devolver_respuesta_12)
        self.opcion_12_3.toggled.connect(self.devolver_respuesta_12)
        self.opcion_13_1.toggled.connect(self.devolver_respuesta_13)
        self.opcion_13_2.toggled.connect(self.devolver_respuesta_13)
        self.opcion_13_3.toggled.connect(self.devolver_respuesta_13)
        self.opcion_14_1.toggled.connect(self.devolver_respuesta_14)
        self.opcion_14_2.toggled.connect(self.devolver_respuesta_14)
        self.opcion_14_3.toggled.connect(self.devolver_respuesta_14)
        self.opcion_15_1.toggled.connect(self.devolver_respuesta_15)
        self.opcion_15_2.toggled.connect(self.devolver_respuesta_15)
        self.opcion_15_3.toggled.connect(self.devolver_respuesta_15)
        self.opcion_16_1.toggled.connect(self.devolver_respuesta_16)
        self.opcion_16_2.toggled.connect(self.devolver_respuesta_16)
        self.opcion_16_3.toggled.connect(self.devolver_respuesta_16)
        self.opcion_17_1.toggled.connect(self.devolver_respuesta_17)
        self.opcion_17_2.toggled.connect(self.devolver_respuesta_17)
        self.opcion_17_3.toggled.connect(self.devolver_respuesta_17)
        self.opcion_18_1.toggled.connect(self.devolver_respuesta_18)
        self.opcion_18_2.toggled.connect(self.devolver_respuesta_18)
        self.opcion_18_3.toggled.connect(self.devolver_respuesta_18)
        self.opcion_19_1.toggled.connect(self.devolver_respuesta_19)
        self.opcion_19_2.toggled.connect(self.devolver_respuesta_19)
        self.opcion_19_3.toggled.connect(self.devolver_respuesta_19)
        self.opcion_20_1.toggled.connect(self.devolver_respuesta_20)
        self.opcion_20_2.toggled.connect(self.devolver_respuesta_20)
        self.opcion_20_3.toggled.connect(self.devolver_respuesta_20)
        self.opcion_21_1.toggled.connect(self.devolver_respuesta_21)
        self.opcion_21_2.toggled.connect(self.devolver_respuesta_21)
        self.opcion_21_3.toggled.connect(self.devolver_respuesta_21)
        self.opcion_22_1.toggled.connect(self.devolver_respuesta_22)
        self.opcion_22_2.toggled.connect(self.devolver_respuesta_22)
        self.opcion_22_3.toggled.connect(self.devolver_respuesta_22)
        self.opcion_23_1.toggled.connect(self.devolver_respuesta_23)
        self.opcion_23_2.toggled.connect(self.devolver_respuesta_23)
        self.opcion_23_3.toggled.connect(self.devolver_respuesta_23)
        self.opcion_24_1.toggled.connect(self.devolver_respuesta_24)
        self.opcion_24_2.toggled.connect(self.devolver_respuesta_24)
        self.opcion_24_3.toggled.connect(self.devolver_respuesta_24)
        self.opcion_25_1.toggled.connect(self.devolver_respuesta_25)
        self.opcion_25_2.toggled.connect(self.devolver_respuesta_25)
        self.opcion_25_3.toggled.connect(self.devolver_respuesta_25)
        self.opcion_26_1.toggled.connect(self.devolver_respuesta_26)
        self.opcion_26_2.toggled.connect(self.devolver_respuesta_26)
        self.opcion_26_3.toggled.connect(self.devolver_respuesta_26)
        self.opcion_27_1.toggled.connect(self.devolver_respuesta_27)
        self.opcion_27_2.toggled.connect(self.devolver_respuesta_27)
        self.opcion_27_3.toggled.connect(self.devolver_respuesta_27)
        self.opcion_28_1.toggled.connect(self.devolver_respuesta_28)
        self.opcion_28_2.toggled.connect(self.devolver_respuesta_28)
        self.opcion_28_3.toggled.connect(self.devolver_respuesta_28)
        self.opcion_29_1.toggled.connect(self.devolver_respuesta_29)
        self.opcion_29_2.toggled.connect(self.devolver_respuesta_29)
        self.opcion_29_3.toggled.connect(self.devolver_respuesta_29)
        self.opcion_30_1.toggled.connect(self.devolver_respuesta_30)
        self.opcion_30_2.toggled.connect(self.devolver_respuesta_30)
        self.opcion_30_3.toggled.connect(self.devolver_respuesta_30)

        #BOTON FINALIZAR
        self.boton_finalizar.clicked.connect(self.mostrar_resultados)
        self.show()
        
    def start_time(self):
        self.timer.start(1000) 

    def update_time(self):
        self.elapsed_time += 1
        self.minutes = self.elapsed_time // 60
        self.seconds = self.elapsed_time % 60
        self.time_str = f"{self.minutes:02d}:{self.seconds:02d}"
        self.print_cronometro.setText(f"{self.time_str}")
        if self.time_str == "30:00":
            tiempo_limite = QMessageBox.information(self, "Tiempo Límite", "Te quedaste sin tiempo, lo siento...")
            self.cerrar_ventana_hija()
            
    def devolver_respuesta_1(self):
        self.opcion_1_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_1_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_1_3.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_1_1.setEnabled(False)
        self.opcion_1_2.setEnabled(False)
        self.opcion_1_3.setEnabled(False)
        if self.opcion_1_3.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_001.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_1_1.isChecked() or self.opcion_1_2.isChecked():
            self.boton_001.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_2(self):
        self.opcion_2_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_2_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_2_3.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_2_1.setEnabled(False)
        self.opcion_2_2.setEnabled(False)
        self.opcion_2_3.setEnabled(False)
        if self.opcion_2_3.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_002.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_2_1.isChecked() or self.opcion_2_2.isChecked():
            self.boton_002.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_3(self):
        self.opcion_3_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_3_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_3_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_3_1.setEnabled(False)
        self.opcion_3_2.setEnabled(False)
        self.opcion_3_3.setEnabled(False)
        if self.opcion_3_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_003.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_3_1.isChecked() or self.opcion_3_3.isChecked():
            self.boton_003.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_4(self):
        self.opcion_4_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_4_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_4_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_4_1.setEnabled(False)
        self.opcion_4_2.setEnabled(False)
        self.opcion_4_3.setEnabled(False)
        if self.opcion_4_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_004.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_4_1.isChecked() or self.opcion_4_3.isChecked():
            self.boton_004.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_5(self):
        self.opcion_5_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_5_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_5_3.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_5_1.setEnabled(False)
        self.opcion_5_2.setEnabled(False)
        self.opcion_5_3.setEnabled(False)
        if self.opcion_5_3.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_005.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_5_1.isChecked() or self.opcion_5_2.isChecked():
            self.boton_005.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1
    
    def devolver_respuesta_6(self):
        self.opcion_6_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_6_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_6_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_6_1.setEnabled(False)
        self.opcion_6_2.setEnabled(False)
        self.opcion_6_3.setEnabled(False)
        if self.opcion_6_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_006.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_6_2.isChecked() or self.opcion_6_3.isChecked():
            self.boton_006.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_7(self):
        self.opcion_7_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_7_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_7_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_7_1.setEnabled(False)
        self.opcion_7_2.setEnabled(False)
        self.opcion_7_3.setEnabled(False)
        if self.opcion_7_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_007.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_7_2.isChecked() or self.opcion_7_3.isChecked():
            self.boton_007.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_8(self):
        self.opcion_8_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_8_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_8_3.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_8_1.setEnabled(False)
        self.opcion_8_2.setEnabled(False)
        self.opcion_8_3.setEnabled(False)
        if self.opcion_8_3.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_008.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_8_1.isChecked() or self.opcion_8_2.isChecked():
            self.boton_008.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_9(self):
        self.opcion_9_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_9_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_9_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_9_1.setEnabled(False)
        self.opcion_9_2.setEnabled(False)
        self.opcion_9_3.setEnabled(False)
        if self.opcion_9_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_009.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_9_2.isChecked() or self.opcion_9_3.isChecked():
            self.boton_009.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_10(self):
        self.opcion_10_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_10_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_10_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_10_1.setEnabled(False)
        self.opcion_10_2.setEnabled(False)
        self.opcion_10_3.setEnabled(False)
        if self.opcion_10_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_010.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_10_2.isChecked() or self.opcion_10_3.isChecked():
            self.boton_010.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_11(self):
        self.opcion_11_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_11_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_11_3.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_11_1.setEnabled(False)
        self.opcion_11_2.setEnabled(False)
        self.opcion_11_3.setEnabled(False)
        if self.opcion_11_3.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_011.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_11_1.isChecked() or self.opcion_11_2.isChecked():
            self.boton_011.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_12(self):
        self.opcion_12_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_12_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_12_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_12_1.setEnabled(False)
        self.opcion_12_2.setEnabled(False)
        self.opcion_12_3.setEnabled(False)
        if self.opcion_12_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_012.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_12_1.isChecked() or self.opcion_12_3.isChecked():
            self.boton_012.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_13(self):
        self.opcion_13_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_13_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_13_3.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_13_1.setEnabled(False)
        self.opcion_13_2.setEnabled(False)
        self.opcion_13_3.setEnabled(False)
        if self.opcion_13_3.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_013.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_13_1.isChecked() or self.opcion_13_2.isChecked():
            self.boton_013.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_14(self):
        self.opcion_14_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_14_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_14_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_14_1.setEnabled(False)
        self.opcion_14_2.setEnabled(False)
        self.opcion_14_3.setEnabled(False)
        if self.opcion_14_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_014.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_14_1.isChecked() or self.opcion_14_3.isChecked():
            self.boton_014.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_15(self):
        self.opcion_15_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_15_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_15_3.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_15_1.setEnabled(False)
        self.opcion_15_2.setEnabled(False)
        self.opcion_15_3.setEnabled(False)
        if self.opcion_15_3.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_015.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_15_1.isChecked() or self.opcion_15_2.isChecked():
            self.boton_015.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_16(self):
        self.opcion_16_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_16_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_16_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_16_1.setEnabled(False)
        self.opcion_16_2.setEnabled(False)
        self.opcion_16_3.setEnabled(False)
        if self.opcion_16_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_016.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_16_1.isChecked() or self.opcion_16_3.isChecked():
            self.boton_016.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_17(self):
        self.opcion_17_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_17_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_17_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_17_1.setEnabled(False)
        self.opcion_17_2.setEnabled(False)
        self.opcion_17_3.setEnabled(False)
        if self.opcion_17_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_017.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_17_1.isChecked() or self.opcion_17_3.isChecked():
            self.boton_017.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_18(self):
        self.opcion_18_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_18_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_18_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_18_1.setEnabled(False)
        self.opcion_18_2.setEnabled(False)
        self.opcion_18_3.setEnabled(False)
        if self.opcion_18_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_018.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_18_2.isChecked() or self.opcion_18_3.isChecked():
            self.boton_018.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_19(self):
        self.opcion_19_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_19_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_19_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_19_1.setEnabled(False)
        self.opcion_19_2.setEnabled(False)
        self.opcion_19_3.setEnabled(False)
        if self.opcion_19_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_019.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_19_2.isChecked() or self.opcion_19_3.isChecked():
            self.boton_019.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_20(self):
        self.opcion_20_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_20_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_20_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_20_1.setEnabled(False)
        self.opcion_20_2.setEnabled(False)
        self.opcion_20_3.setEnabled(False)
        if self.opcion_20_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_020.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_20_1.isChecked() or self.opcion_20_3.isChecked():
            self.boton_020.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1
    
    def devolver_respuesta_21(self):
        self.opcion_21_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_21_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_21_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_21_1.setEnabled(False)
        self.opcion_21_2.setEnabled(False)
        self.opcion_21_3.setEnabled(False)
        if self.opcion_21_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_021.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_21_2.isChecked() or self.opcion_21_3.isChecked():
            self.boton_021.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_22(self):
        self.opcion_22_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_22_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_22_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_22_1.setEnabled(False)
        self.opcion_22_2.setEnabled(False)
        self.opcion_22_3.setEnabled(False)
        if self.opcion_22_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_022.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_22_2.isChecked() or self.opcion_22_3.isChecked():
            self.boton_022.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_23(self):
        self.opcion_23_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_23_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_23_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_23_1.setEnabled(False)
        self.opcion_23_2.setEnabled(False)
        self.opcion_23_3.setEnabled(False)
        if self.opcion_23_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_023.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_23_1.isChecked() or self.opcion_23_3.isChecked():
            self.boton_023.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_24(self):
        self.opcion_24_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_24_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_24_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_24_1.setEnabled(False)
        self.opcion_24_2.setEnabled(False)
        self.opcion_24_3.setEnabled(False)
        if self.opcion_24_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_024.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_24_1.isChecked() or self.opcion_24_3.isChecked():
            self.boton_024.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_25(self):
        self.opcion_25_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_25_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_25_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_25_1.setEnabled(False)
        self.opcion_25_2.setEnabled(False)
        self.opcion_25_3.setEnabled(False)
        if self.opcion_25_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_025.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_25_2.isChecked() or self.opcion_25_3.isChecked():
            self.boton_025.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_26(self):
        self.opcion_26_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_26_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_26_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_26_1.setEnabled(False)
        self.opcion_26_2.setEnabled(False)
        self.opcion_26_3.setEnabled(False)
        if self.opcion_26_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_026.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_26_1.isChecked() or self.opcion_26_3.isChecked():
            self.boton_026.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_27(self):
        self.opcion_27_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_27_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_27_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_27_1.setEnabled(False)
        self.opcion_27_2.setEnabled(False)
        self.opcion_27_3.setEnabled(False)
        if self.opcion_27_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_027.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_27_1.isChecked() or self.opcion_27_3.isChecked():
            self.boton_027.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_28(self):
        self.opcion_28_1.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_28_2.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_28_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_28_1.setEnabled(False)
        self.opcion_28_2.setEnabled(False)
        self.opcion_28_3.setEnabled(False)
        if self.opcion_28_1.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_028.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_28_2.isChecked() or self.opcion_28_3.isChecked():
            self.boton_028.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_29(self):
        self.opcion_29_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_29_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_29_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_29_1.setEnabled(False)
        self.opcion_29_2.setEnabled(False)
        self.opcion_29_3.setEnabled(False)
        if self.opcion_29_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_029.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_29_1.isChecked() or self.opcion_29_3.isChecked():
            self.boton_029.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def devolver_respuesta_30(self):
        self.opcion_30_1.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_30_2.setStyleSheet("color: rgb(138, 255, 156);")
        self.opcion_30_3.setStyleSheet("color: rgb(255, 76, 76);")
        self.opcion_30_1.setEnabled(False)
        self.opcion_30_2.setEnabled(False)
        self.opcion_30_3.setEnabled(False)
        if self.opcion_30_2.isChecked():
            self.no_contestadas -= 1
            self.acertadas += 1
            self.boton_030.setStyleSheet("QPushButton{\n""background-color: rgb(138, 255, 156);\n""border-radius: 4px\n""}\n")
        elif self.opcion_30_1.isChecked() or self.opcion_30_3.isChecked():
            self.boton_030.setStyleSheet("QPushButton{\n""background-color: rgb(255, 76, 76);\n""border-radius: 4px\n""}\n")
            self.no_contestadas -= 1
            self.falladas += 1

    def mostrar_resultados(self):
        if self.no_contestadas == 0:
            if self.acertadas >= 27:
                resumen_test = QMessageBox.information(self, "Resultados", f"APTO\nACERTADAS: {self.acertadas}\nFALLADAS: {self.falladas}\nTIEMPO: {self.time_str}")
            else:
                resumen_test = QMessageBox.information(self, "Resultados", f"NO APTO\nACERTADAS: {self.acertadas}\nFALLADAS: {self.falladas}\nTIEMPO: {self.time_str}")
            self.cerrar_ventana_hija()
            self.almacen_partidas.add_partida(self.nickname_var, self.acertadas, self.falladas, self.time_str)
        else:
            no_contestadas = QMessageBox.warning(self, "Fallo", "Te quedan preguntas sin contestar")

    @QtCore.pyqtSlot(QtGui.QCloseEvent)
    def closeEvent(self, event):
        if self.no_contestadas > 0:
            cerrar_antes_de_tiempo = QMessageBox.question(
                self,
                "Cerrar Test",
                "¿Estás seguro de que quieres cerrar la aplicación?\n    No se guardarán tus resultados actuales",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if cerrar_antes_de_tiempo == QMessageBox.Yes:
                self.cerrar_ventana_hija()
            else:
                event.ignore()

    def cerrar_ventana_hija(self):
        self.close()
        self.ventana_realizar_test.show()