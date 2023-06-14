from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtGui import QIcon

from gui.registrarse import Registrarse
from gui.ventana_user import VentanaUser

from almacen.almacenusuarios import AlmacenUsuarios

import os

class MenuLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana_registro = None
        self.ventana_menu_user = None
        self.login = None
        self.RUTA_FOTO = os.path.abspath('img/logofast.png')

    def setupUi(self):
        #CARGARMOS DATOS
        self.almacen_usuarios = AlmacenUsuarios()
        self.cargar_ficheros_en_app()     
        self.login.setObjectName("Login")
        self.login.resize(1099, 747)
        self.login.setMinimumSize(QtCore.QSize(1099, 747))
        self.login.setMaximumSize(QtCore.QSize(1099, 747))
        self.login.setStyleSheet("")
        self.login.setDocumentMode(False)
        self.ventana = QtWidgets.QWidget(self.login)
        self.ventana.setObjectName("ventana")
        #FAVICON
        self.favicon = QIcon('img/coche.png')
        self.login.setWindowIcon(self.favicon)
        self.print_nickname = QtWidgets.QLabel(self.ventana)
        self.print_nickname.setGeometry(QtCore.QRect(310, 350, 170, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.print_nickname.setFont(font)
        self.print_nickname.setStyleSheet("color: #09B5CB;")
        self.print_nickname.setTextFormat(QtCore.Qt.AutoText)
        self.print_nickname.setObjectName("print_nickname")
        self.print_password = QtWidgets.QLabel(self.ventana)
        self.print_password.setGeometry(QtCore.QRect(310, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.print_password.setFont(font)
        self.print_password.setStyleSheet("color: #09B5CB;")
        self.print_password.setObjectName("print_password")
        self.input_nickname = QtWidgets.QLineEdit(self.ventana)
        self.input_nickname.setGeometry(QtCore.QRect(310, 410, 451, 41))
        self.input_nickname.setObjectName("input_nickname")
        self.input_nickname.setStyleSheet("font-size: 16px;")
        self.input_password = QtWidgets.QLineEdit(self.ventana)
        self.input_password.setGeometry(QtCore.QRect(310, 520, 451, 41))
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.fondo_negro = QtWidgets.QFrame(self.ventana)
        self.fondo_negro.setGeometry(QtCore.QRect(-20, -40, 1181, 900))
        self.fondo_negro.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.fondo_negro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fondo_negro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fondo_negro.setObjectName("fondo_negro")
        self.imagen_coche = QtWidgets.QLabel(self.fondo_negro)
        self.imagen_coche.setGeometry(QtCore.QRect(280, 70, 531, 431))
        imagen_coche = QtGui.QImage(self.RUTA_FOTO)
        if imagen_coche.isNull():
            print("Error al cargar la imagen")
        else:
            self.imagen_coche.setPixmap(QtGui.QPixmap.fromImage(imagen_coche))
        self.boton_iniciar_sesion = QtWidgets.QPushButton(self.fondo_negro)
        self.boton_iniciar_sesion.setGeometry(QtCore.QRect(630, 630, 141, 41))
        self.boton_iniciar_sesion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton_iniciar_sesion.setStyleSheet("background-color: #09B5CB;\n"
"color: #FFFFFF;")
        self.boton_iniciar_sesion.setFlat(False)
        self.boton_iniciar_sesion.setObjectName("boton_iniciar_sesion")
        self.print_iniciar_sesion = QtWidgets.QLabel(self.fondo_negro)
        self.print_iniciar_sesion.setGeometry(QtCore.QRect(330, 70, 441, 131))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.print_iniciar_sesion.setFont(font)
        self.print_iniciar_sesion.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.print_iniciar_sesion.setMouseTracking(False)
        self.print_iniciar_sesion.setStyleSheet("font: 63 36pt \"Bahnschrift SemiBold\";\n"
"color: #09B5CB;\n"
"")
        self.print_iniciar_sesion.setObjectName("print_iniciar_sesion")
        self.link_registrarse = QtWidgets.QCommandLinkButton(self.fondo_negro)
        self.link_registrarse.setGeometry(QtCore.QRect(330, 630, 222, 48))
        self.link_registrarse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.link_registrarse.setStyleSheet("color: #09B5CB;")
        self.link_registrarse.setCheckable(False)
        self.link_registrarse.setChecked(False)
        self.link_registrarse.setAutoRepeat(False)
        self.link_registrarse.setAutoExclusive(False)
        self.link_registrarse.setAutoDefault(False)
        self.link_registrarse.setDefault(False)
        self.link_registrarse.setObjectName("link_registrarse")
        self.fondo_negro.raise_()
        self.print_nickname.raise_()
        self.print_password.raise_()
        self.input_nickname.raise_()
        self.input_password.raise_()
        self.login.setCentralWidget(self.ventana)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.login)

        self.link_registrarse.clicked.connect(self.abrir_registrarse)
        self.boton_iniciar_sesion.clicked.connect(self.comprobar_datos)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.login.setWindowTitle(_translate("self.login", "AutoescuelaFast"))
        self.print_nickname.setText(_translate("self.login", "Nombre de Usuario"))
        self.print_password.setText(_translate("self.login", "Contraseña"))
        self.boton_iniciar_sesion.setText(_translate("self.login", "INICIAR SESIÓN"))
        self.print_iniciar_sesion.setText(_translate("self.login", "INICIAR SESIÓN"))
        self.link_registrarse.setText(_translate("self.login", "Registrate"))

    def cargar_ficheros_en_app(self):
        self.almacen_usuarios.importar_usuarios()

    #ENLACE REGISTRASE
    def abrir_registrarse(self):
        self.login.hide()
        self.ventana_registro = Registrarse(self.almacen_usuarios, self.login)
        
    #BOTÓN INICIAR SESIÓN
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.boton_iniciar_sesion.clicked.emit()

    def recoger_campos_boton_iniciar_sesion(self): #LO IMPLEMENTAREMOS PARA RECOGER DATOS Y VALIDARLOS
        nickname_var = self.input_nickname.text()
        password_var = self.input_password.text()
        return nickname_var, password_var

    def comprobar_datos(self):
        nickname_var, password_var = self.recoger_campos_boton_iniciar_sesion()
        if self.almacen_usuarios.login_existencia_usuario(nickname_var, password_var):
            self.login.hide()
            self.ventana_menu_user = VentanaUser(self.almacen_usuarios, nickname_var, self.login)
        else:
            campos_obligatorios = QMessageBox.warning(None, "Error", "Contraseña o nombre incorrectos")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = MenuLogin()
    ventana_principal.login = ventana_principal
    ventana_principal.setupUi()
    ventana_principal.show()
    sys.exit(app.exec_())