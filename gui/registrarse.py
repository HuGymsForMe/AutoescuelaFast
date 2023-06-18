from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtGui import QIcon, QCloseEvent


import datetime
import os

from clases.validator import Validator

class Registrarse(QMainWindow):
    def __init__(self, almacen_usuarios, ventana_login):
        super().__init__()
        self.almacen_usuarios = almacen_usuarios
        self.validador = Validator()
        self.ventana_login = ventana_login
        self.RUTA_FOTO = os.path.abspath('./img/logofast.png')
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1102, 752)
        self.setMinimumSize(QtCore.QSize(1102, 752))
        self.setMaximumSize(QtCore.QSize(1102, 752))
        self.print_password = QtWidgets.QLabel(self)
        self.print_password.setGeometry(QtCore.QRect(130, 280, 181, 51))
        self.favicon = QIcon('./img/coche.png')
        self.setWindowIcon(self.favicon)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_password.setFont(font)
        self.print_password.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_password.setText(str(QtCore.Qt.AutoText))
        self.print_password.setObjectName("print_password")
        self.print_confirm_password = QtWidgets.QLabel(self)
        self.print_confirm_password.setGeometry(QtCore.QRect(130, 390, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_confirm_password.setFont(font)
        self.print_confirm_password.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_confirm_password.setText(str(QtCore.Qt.AutoText))
        self.print_confirm_password.setObjectName("print_confirm_password")
        self.print_name = QtWidgets.QLabel(self)
        self.print_name.setGeometry(QtCore.QRect(470, 280, 81, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_name.setFont(font)
        self.print_name.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_name.setText(str(QtCore.Qt.AutoText))
        self.print_name.setObjectName("print_name")
        self.print_apellidos = QtWidgets.QLabel(self)
        self.print_apellidos.setGeometry(QtCore.QRect(470, 390, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_apellidos.setFont(font)
        self.print_apellidos.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_apellidos.setText(str(QtCore.Qt.AutoText))
        self.print_apellidos.setObjectName("print_apellidos")
        self.input_nickname = QtWidgets.QLineEdit(self)
        self.input_nickname.setGeometry(QtCore.QRect(130, 230, 291, 41))
        self.input_nickname.setObjectName("input_nickname")
        self.input_nickname.setStyleSheet("font-size: 16px;")
        self.input_password = QtWidgets.QLineEdit(self)
        self.input_password.setGeometry(QtCore.QRect(130, 330, 291, 41))
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.input_gmail = QtWidgets.QLineEdit(self)
        self.input_gmail.setGeometry(QtCore.QRect(470, 230, 291, 41))
        self.input_gmail.setObjectName("input_gmail")
        self.input_gmail.setStyleSheet("font-size: 16px;")
        self.input_confirm_password = QtWidgets.QLineEdit(self)
        self.input_confirm_password.setGeometry(QtCore.QRect(130, 440, 291, 41))
        self.input_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_confirm_password.setObjectName("input_confirm_password")
        self.input_nombre = QtWidgets.QLineEdit(self)
        self.input_nombre.setGeometry(QtCore.QRect(470, 330, 291, 41))
        self.input_nombre.setObjectName("input_nombre")
        self.input_nombre.setStyleSheet("font-size: 16px;")
        self.foto_coche = QtWidgets.QLabel(self)
        imagen_coche = QtGui.QImage(self.RUTA_FOTO)
        if imagen_coche.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_coche.setPixmap(QtGui.QPixmap.fromImage(imagen_coche))
        self.foto_coche.setGeometry(QtCore.QRect(70, 450, 491, 351))
        self.print_fecha_actual = QtWidgets.QLabel(self)
        self.print_fecha_actual.setGeometry(QtCore.QRect(890, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_fecha_actual.setFont(font)
        self.print_fecha_actual.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_fecha_actual.setText(str(QtCore.Qt.AutoText))
        self.print_fecha_actual.setObjectName("print_fecha_actual")
        self.print_nickname = QtWidgets.QLabel(self)
        self.print_nickname.setGeometry(QtCore.QRect(130, 170, 250, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_nickname.setFont(font)
        self.print_nickname.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_nickname.setText(str(QtCore.Qt.AutoText))
        self.print_nickname.setObjectName("print_nickname")
        self.boton_registrarse = QtWidgets.QPushButton(self)
        self.boton_registrarse.setGeometry(QtCore.QRect(780, 600, 231, 71))
        self.boton_registrarse.setStyleSheet("background-color: #09B5CB;\n"
"color: #FFFFFF;")
        self.boton_registrarse.setObjectName("boton_registrarse")
        self.boton_registrarse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.print_correo_electronico = QtWidgets.QLabel(self)
        self.print_correo_electronico.setGeometry(QtCore.QRect(470, 170, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.print_correo_electronico.setFont(font)
        self.print_correo_electronico.setStyleSheet("color: #09B5CB;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.print_correo_electronico.setText(str(QtCore.Qt.AutoText))
        self.print_correo_electronico.setObjectName("print_correo_electronico")
        self.input_apellidos = QtWidgets.QLineEdit(self)
        self.input_apellidos.setGeometry(QtCore.QRect(470, 440, 291, 41))
        self.input_apellidos.setObjectName("input_apellidos")
        self.input_apellidos.setStyleSheet("font-size: 16px;")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-11, -21, 1181, 811))
        self.frame.setStyleSheet("\n"
"background-color: rgb(56, 56, 56);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.print_registrarse = QtWidgets.QLabel(self.frame)
        self.print_registrarse.setGeometry(QtCore.QRect(260, 40, 391, 131))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.print_registrarse.setFont(font)
        self.print_registrarse.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.print_registrarse.setMouseTracking(False)
        self.print_registrarse.setStyleSheet("font: 63 36pt \"Bahnschrift SemiBold\";\n"
"color: #09B5CB;\n"
"")
        self.print_registrarse.setObjectName("print_registrarse")
        self.frame.raise_()
        self.foto_coche.raise_()
        self.print_password.raise_()
        self.print_confirm_password.raise_()
        self.print_name.raise_()
        self.print_apellidos.raise_()
        self.input_nickname.raise_()
        self.input_password.raise_()
        self.input_gmail.raise_()
        self.input_confirm_password.raise_()
        self.input_nombre.raise_()
        self.print_fecha_actual.raise_()
        self.print_nickname.raise_()
        self.boton_registrarse.raise_()
        self.print_correo_electronico.raise_()
        self.input_apellidos.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.move(500, 120)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Registrarse"))
        self.print_password.setText(_translate("self", "Contraseña"))
        self.print_confirm_password.setText(_translate("self", "Confirmar Contraseña"))
        self.print_name.setText(_translate("self", "Nombre"))
        self.print_apellidos.setText(_translate("self", "Apellidos"))
        fecha_actual = datetime.datetime.now().strftime("%H:%M:%S")
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_fecha)
        self.timer.start(1000) 
        self.print_fecha_actual.setText(_translate("self", fecha_actual))
        self.print_nickname.setText(_translate("self", "Nombre de Usuario"))
        self.boton_registrarse.setText(_translate("self", "REGISTRARSE"))
        self.print_correo_electronico.setText(_translate("self", "Correo Electrónico"))
        self.print_registrarse.setText(_translate("self", "REGISTRARSE"))

        self.boton_registrarse.clicked.connect(self.comprobar_registro)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.boton_registrarse.clicked.emit()
    
    '''def closeEvent(self, event):
        event.accept()
        self.volver_al_menu()'''
        
    def actualizar_fecha(self):
        fecha_actual = datetime.datetime.now().strftime("%H:%M:%S")
        self.print_fecha_actual.setText(fecha_actual)
     
    #COMPROBAR QUE LAS CONTRASEÑAS SEAN IGUALES
    def recoger_datos_registro(self):
        nickname_var = self.input_nickname.text()
        password_var = self.input_password.text()
        confirm_password_var = self.input_confirm_password.text()
        gmail_var = self.input_gmail.text()
        name_var = self.input_nombre.text()
        apellidos_var = self.input_apellidos.text()
        return nickname_var, password_var, confirm_password_var, gmail_var, name_var, apellidos_var

    def comprobar_registro(self):
        nickname_var, password_var, confirm_password_var, gmail_var, name_var, apellidos_var = self.recoger_datos_registro()
        if (nickname_var == '' or password_var == '' or confirm_password_var == '' 
        or gmail_var == '' or name_var == '' or apellidos_var == ''):
            campos_obligatorios = QMessageBox.warning(self, "Error", "Debes rellenar todos los campos")
        elif len(nickname_var) > 20 or len(nickname_var) < 6:
            max_caracteres = QMessageBox.warning(self, "Nombre de usuario incorrecto", "El nombre de usuario debe de tener entre 6 y 20 caracteres")
        elif self.validador.validar_contrasenia(password_var) or self.validador.validar_contrasenia(confirm_password_var):
            advertencia = QMessageBox.warning(self, "Contraseña incorrecta", "La cadena tiene que contener al menos \n  8 dígitos tanto letras como dígitos")
        elif password_var != confirm_password_var:
            password_desigual = QMessageBox.warning(self, "Error", "No coinciden las contraseñas")
        else:
            if self.almacen_usuarios.add_usuario(nickname_var, password_var, gmail_var, name_var, apellidos_var):
                adicion_correcta = QMessageBox.information(self, "Usuario Añadido", "Usuario añadido con éxito")
                self.almacen_usuarios.sobreescribir_ficheros()
                self.volver_al_menu()
            else:
                adicion_correcta = QMessageBox.information(self, "Usuario Incorrecto", "El usuario ya está añadido")

    @QtCore.pyqtSlot(QtGui.QCloseEvent)
    def closeEvent(self, event):
        self.cerrar_ventana_hija()
    
    def cerrar_ventana_hija(self):
        self.close()
        self.ventana_login.show()
    




