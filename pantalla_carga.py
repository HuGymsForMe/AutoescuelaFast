import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon

from login import MenuLogin

class PantallaDeCarga(QMainWindow):
    def __init__(self):
        super().__init__()
        self.RUTA_FOTO = os.path.abspath('img/logofast.png')
        self.RUTA_CSS = os.path.abspath('./css/pantalla_carga.css')
        self.setupUi()

    def setupUi(self):
        self.resize(800, 448)
        self.setMinimumSize(QtCore.QSize(800, 448))
        self.setMaximumSize(QtCore.QSize(800, 480))
        with open(self.RUTA_CSS) as f:
            self.setStyleSheet(f.read())
            
        self.favicon = QIcon('img/coche.png')
        self.setWindowIcon(self.favicon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.frame_pantalla_carga = QtWidgets.QFrame(self.centralwidget)
        self.frame_pantalla_carga.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame_pantalla_carga.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pantalla_carga.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pantalla_carga.setLineWidth(0)
        self.frame_pantalla_carga.setObjectName("frame_pantalla_carga")
        self.barra_de_progreso = QtWidgets.QProgressBar(self.frame_pantalla_carga)
        self.barra_de_progreso.setGeometry(QtCore.QRect(190, 330, 461, 41))
        self.barra_de_progreso.setMinimum(0)
        self.barra_de_progreso.setMaximum(100)
        self.barra_de_progreso.setTextVisible(False)
        self.barra_de_progreso.setOrientation(QtCore.Qt.Horizontal)
        self.barra_de_progreso.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.print_cargando = QtWidgets.QLabel(self.frame_pantalla_carga)
        self.print_cargando.setGeometry(QtCore.QRect(360, 390, 141, 31))
        self.print_cargando.setObjectName("print_cargando")
        self.foto_coche = QtWidgets.QLabel(self.frame_pantalla_carga)
        self.foto_coche.setGeometry(QtCore.QRect(150, 60, 400, 211))
        imagen_coche = QtGui.QImage(self.RUTA_FOTO)
        if imagen_coche.isNull():
            print("Error al cargar la imagen")
        else:
            self.foto_coche.setPixmap(QtGui.QPixmap.fromImage(imagen_coche))
        self.horizontalLayout.addWidget(self.frame_pantalla_carga)
        self.setCentralWidget(self.centralwidget)

        self.timer = QBasicTimer()
        self.timer.start(30, self)

        self.progress_value = 0

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def timerEvent(self, event):
        if self.progress_value > 100:
            self.timer.stop()
            return
        elif self.progress_value == 100:
            self.close()
            self.menu_login = MenuLogin()
        
        self.progress_value += 1
        self.barra_de_progreso.setValue(self.progress_value)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Bienvenido"))
        self.print_cargando.setText(_translate("self", "Cargando..."))
        self.foto_coche.setText(_translate("self", ""))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = PantallaDeCarga()
    ventana_principal.show()
    sys.exit(app.exec_())