from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon


class AcercaDe(QMainWindow):
    def __init__(self, ventana_user):
        super().__init__()
        self.ventana_user = ventana_user
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(794, 613)
        self.setMinimumSize(QtCore.QSize(794, 613))
        self.setMaximumSize(QtCore.QSize(794, 613))
        self.favicon = QIcon('./img/coche.png')
        self.setWindowIcon(self.favicon)
        self.print_body = QtWidgets.QLabel(self)
        self.print_body.setGeometry(QtCore.QRect(100, 50, 600, 411))
        self.print_body.setStyleSheet("color: #09B5CB;")
        self.print_body.setObjectName("print_body")
        self.print_body.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: #09B5CB;")
        self.print_title = QtWidgets.QLabel(self)
        self.print_title.setGeometry(QtCore.QRect(300, 20, 201, 81))
        self.print_title.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: #09B5CB;")
        self.print_title.setObjectName("print_title")
        self.frame_footer = QtWidgets.QFrame(self)
        self.frame_footer.setGeometry(QtCore.QRect(0, 490, 811, 131))
        self.frame_footer.setStyleSheet("background-color: #09B5CB;")
        self.frame_footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_footer.setObjectName("frame_footer")
        self.print_footer = QtWidgets.QLabel(self.frame_footer)
        self.print_footer.setGeometry(QtCore.QRect(190, 40, 461, 41))
        self.print_footer.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(56, 56, 56);")
        self.print_footer.setObjectName("print_footer")
        self.frame_body = QtWidgets.QFrame(self)
        self.frame_body.setGeometry(QtCore.QRect(-1, -1, 801, 491))
        self.frame_body.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.frame_body.raise_()
        self.frame_footer.raise_()
        self.print_body.raise_()
        self.print_title.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "AcercaDe"))
        self.print_body.setText(_translate("self", "ESTA APLICACIÓN ESTÁ DESARROLLADA CON EL FIN DE PODER EVALUAR \nA NUESTROS ALUMNOS, Y QUE ELLOS MISMOS COMPRUEBEN SU PROGRESO \nHACIENDO TEST, CON UNA SERIE DE ESTADIÍSTICAS QUE PODRÁN \nENCONTRAR EN \"MIS ESTADÍSTICAS\", AUTOESCUELA FAST BUSCA COMO \nSU NOMBRE INDICA NUESTROS ALUMNOS PUEDAN EVALUARSE DE UNA \nFORMA RÁPIDA Y EFICAZ, RECOMENDAMOS PRESENTARSE A EXÁMEN A \nLOS ALUMNOS CON UN 90% DE APROBADOS EN SUS TEST GLOBALES Y UNA \nMEDIA DE FALLOS DE TEST DE 1 O 2 COMO MÁXIMO.\n\nEN AUTOESCUELA FAST DISPONEMOS DE PROFESORES Y CLASES QUE \nFACILITARÁN SU APRENDIZAJE, ADEMÁS AL MATRICULARTE EN NUESTRA \nAUTOESCUELA RECIBIRÁS UN LIBRO DEL TEMARIO QUE DEBES ESTUDIAR \nPARA CONSEGUIR TU APTO EN EL TEÓRICO!!"))
        self.print_title.setText(_translate("self", "ACERCA DE"))
        self.print_footer.setText(_translate("self", "©  2023AutoescuelaFastApp. Todos los derechos reservados.  "))

    @QtCore.pyqtSlot(QtGui.QCloseEvent)
    def closeEvent(self, event):
        self.cerrar_ventana_hija()
    
    def cerrar_ventana_hija(self):
        self.close()
        self.ventana_user.show()