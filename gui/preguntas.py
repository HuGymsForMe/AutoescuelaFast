import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QRadioButton, QHBoxLayout

class Frame1(QWidget):
    def __init__(self):
        super().__init__()
        layout = self.setupUi()
        self.setLayout(layout)
        '''self.frame_pregunta1.setStyleSheet("background-color: #383838;")
        self.frame_pregunta1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pregunta1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pregunta1.lower()'''

        '''self.titulo_pregunta1 = QtWidgets.QLabel(self.frame_pregunta1)
        self.titulo_pregunta1.setGeometry(QtCore.QRect(250, 10, 250, 70))
        self.titulo_pregunta1.setStyleSheet("background-color: #FFFFFF;")
        self.titulo_pregunta1.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";")
        self.titulo_pregunta1.setObjectName("titulo_pregunta1")'''

        '''self.imagen_pregunta1 = QtWidgets.QLabel(self.frame_pregunta1)
        self.imagen_pregunta1.setGeometry(QtCore.QRect(280, 200, 300, 300))
        imagen_pregunta1 = QtGui.QImage(self.RUTA_FOTO)
        if imagen_pregunta1.isNull():
            print("Error al cargar la imagen")
        else:
            self.imagen_pregunta1.setPixmap(QtGui.QPixmap.fromImage(imagen_pregunta1))

        self.imagen_pregunta1.setText("")
        self.imagen_pregunta1.setObjectName("imagen_pregunta1")'''

    def setupUi(self):
        layout = QVBoxLayout()
        self.radio_button_group = QFrame()
        self.radio_button_group.setLayout(layout)
        self.radio_button_group.setStyleSheet("background-color: red;")

        self.radio_button_1 = QRadioButton("Vía reservada para automóviles.")
        self.radio_button_2 = QRadioButton("Calzada obligatoria para automóviles, excepto\n motocicletas sin sidecar.")
        self.radio_button_3 = QRadioButton("Calzada obligatoria para automóviles.")

        layout.addWidget(self.radio_button_1)
        layout.addWidget(self.radio_button_2)
        layout.addWidget(self.radio_button_3)
        layout.addWidget(self.radio_button_group)
        
        return layout