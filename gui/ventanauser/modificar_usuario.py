import os
import winsound

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon

from clases.validator import Validator

class ModificarUsuario(QMainWindow):
    def __init__(self, ventana_user, almacen_usuarios, almacen_partidas, nickname_var):
        super().__init__()
        self.ventana_user = ventana_user
        self.almacen_usuarios = almacen_usuarios
        self.almacen_partidas = almacen_partidas
        self.nickname_var = nickname_var
        self.validador = Validator()
        self.RUTA_CSS = os.path.abspath('./css/modificar_usuario.css')
        self.RUTA_SONIDO = os.path.abspath('./sounds/boton.wav')
        
        #DATOS USUARIOS
        self.password = None
        self.gmail = None
        self.nombre = None
        self.apellidos = None
        self.fecha_ingreso = None
        self.setupUi()

    def setupUi(self):
        self.resize(752, 583)
        self.setMinimumSize(QtCore.QSize(752, 583))
        self.setMaximumSize(QtCore.QSize(752, 583))
        with open(self.RUTA_CSS) as f:
            self.setStyleSheet(f.read())

        self.favicon = QIcon('./img/coche.png')
        self.setWindowIcon(self.favicon)
        self.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setProperty("class", "fondo_pantalla")
        self.title_modificar = QtWidgets.QLabel(self.frame)
        self.title_modificar.setGeometry(QtCore.QRect(190, -20, 381, 171))
        self.title_modificar.setProperty("class", "title_modificar")
        self.input_gmail = QtWidgets.QLineEdit(self.frame)
        self.input_gmail.setGeometry(QtCore.QRect(410, 170, 201, 31))
        self.input_gmail.setReadOnly(True)
        self.input_nombre = QtWidgets.QLineEdit(self.frame)
        self.input_nombre.setGeometry(QtCore.QRect(410, 270, 201, 31))
        self.print_nickname = QtWidgets.QLabel(self.frame)
        self.print_nickname.setGeometry(QtCore.QRect(130, 120, 181, 31))
        self.print_nickname.setProperty("class", "print_campos")
        self.input_apellidos = QtWidgets.QLineEdit(self.frame)
        self.input_apellidos.setGeometry(QtCore.QRect(410, 370, 201, 31))
        self.input_nickname = QtWidgets.QLineEdit(self.frame)
        self.input_nickname.setGeometry(QtCore.QRect(130, 170, 201, 31))
        self.input_nickname.setReadOnly(True)
        self.input_password = QtWidgets.QLineEdit(self.frame)
        self.input_password.setGeometry(QtCore.QRect(130, 270, 201, 31))
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_confirm_password = QtWidgets.QLineEdit(self.frame)
        self.input_confirm_password.setGeometry(QtCore.QRect(130, 370, 201, 31))
        self.input_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.print_password = QtWidgets.QLabel(self.frame)
        self.print_password.setGeometry(QtCore.QRect(130, 230, 181, 31))
        self.print_password.setProperty("class", "print_campos")
        self.print_confirm_password = QtWidgets.QLabel(self.frame)
        self.print_confirm_password.setGeometry(QtCore.QRect(130, 330, 201, 31))
        self.print_confirm_password.setProperty("class", "print_campos")
        self.print_gmail = QtWidgets.QLabel(self.frame)
        self.print_gmail.setGeometry(QtCore.QRect(410, 120, 181, 31))
        self.print_gmail.setProperty("class", "print_campos")
        self.print_nombre = QtWidgets.QLabel(self.frame)
        self.print_nombre.setGeometry(QtCore.QRect(410, 230, 181, 31))
        self.print_nombre.setProperty("class", "print_campos")
        self.print_apellidos = QtWidgets.QLabel(self.frame)
        self.print_apellidos.setGeometry(QtCore.QRect(410, 330, 181, 31))
        self.print_apellidos.setProperty("class", "print_campos")
        self.boton_modificar = QtWidgets.QPushButton(self.frame)
        self.boton_modificar.setGeometry(QtCore.QRect(130, 470, 201, 51))
        self.boton_modificar.setProperty("class", "botones_mod")
        self.boton_delete_historial = QtWidgets.QPushButton(self.frame)
        self.boton_delete_historial.setGeometry(QtCore.QRect(410, 470, 211, 51))
        self.boton_delete_historial.setProperty("class", "botones_mod")
        self.verticalLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        #BOTONES MODIFICAR USUARIO
        self.boton_delete_historial.clicked.connect(self.borrar_historial)
        self.boton_modificar.clicked.connect(self.modificar_usuario)

        self.recoger_datos_personales()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "ModificarUsuario"))
        self.title_modificar.setText(_translate("self", "MODIFICAR USUARIO"))
        self.print_nickname.setText(_translate("self", "Nombre de usuario"))
        self.print_password.setText(_translate("self", "Contraseña"))
        self.print_confirm_password.setText(_translate("self", "Confirmar Contraseña"))
        self.print_gmail.setText(_translate("self", "Correo Electrónico"))
        self.print_nombre.setText(_translate("self", "Nombre"))
        self.print_apellidos.setText(_translate("self", "Apellidos"))
        self.input_nickname.setText(_translate("self", f"{self.nickname_var}"))
        self.input_password.setText(_translate("self", f"{self.password}"))
        self.input_confirm_password.setText(_translate("self", f"{self.password}"))
        self.input_gmail.setText(_translate("self", f"{self.gmail}"))
        self.input_nombre.setText(_translate("self", f"{self.nombre}"))
        self.input_apellidos.setText(_translate("self", f"{self.apellidos}"))
        self.boton_modificar.setText(_translate("self", "MODIFICAR USUARIO"))
        self.boton_delete_historial.setText(_translate("self", "BORRAR HISTORIAL"))

    def recoger_datos_personales(self):
        self.nombre, self.password, self.gmail, self.apellidos, self.fecha_ingreso = self.almacen_usuarios.encontrar_usuario_para_mostrar_datos(self.nickname_var)

    def borrar_historial(self):
        winsound.PlaySound(self.RUTA_SONIDO, winsound.SND_FILENAME)
        self.almacen_partidas.borrar_partidas_de_un_usuario(self.nickname_var)
        QMessageBox.information(self, "Historial Borrado", "El historial ha sido borrado correctamente")
        self.cerrar_ventana_hija()

    def modificar_usuario(self):
        winsound.PlaySound(self.RUTA_SONIDO, winsound.SND_FILENAME)
        self.password = self.input_password.text()
        self.nombre = self.input_nombre.text()
        self.apellidos = self.input_apellidos.text()
        if self.input_password.text() == '' or self.input_nombre.text() == '' or self.input_apellidos.text() == '' or self.input_confirm_password.text() == '':
            QMessageBox.warning(self, "Error", "Debes rellenar todos los campos")
        elif len(self.nickname_var) > 20 or len(self.nickname_var) < 6:
            QMessageBox.warning(self, "Nombre de usuario incorrecto", "El nombre de usuario debe de tener entre 6 y 20 caracteres")
        elif self.validador.validar_contrasenia(self.input_password.text()) or self.validador.validar_contrasenia(self.input_confirm_password.text()):
            QMessageBox.warning(self, "Contraseña incorrecta", "La cadena tiene que contener al menos \n  8 caracteres tanto letras como dígitos")
        elif self.input_password.text() != self.input_confirm_password.text():
            QMessageBox.warning(self, "Error", "No coinciden las contraseñas")
        else:
            self.almacen_usuarios.del_usuario(self.nickname_var)
            if self.almacen_usuarios.add_usuario(self.nickname_var, self.password, self.gmail, self.nombre, self.apellidos):
                QMessageBox.information(self, "Usuario Añadido", "Usuario añadido con éxito")
                self.almacen_usuarios.sobreescribir_ficheros()
                self.cerrar_ventana_hija()
            else:
                QMessageBox.information(self, "Usuario Incorrecto", "El usuario ya está añadido")
        

    @QtCore.pyqtSlot(QtGui.QCloseEvent)
    def closeEvent(self, event):
        self.cerrar_ventana_hija()
    
    def cerrar_ventana_hija(self):
        self.close()
        self.ventana_user.show()

    #HACER MODIFICACION USER
    #HACER BORRAR PARTIDAS