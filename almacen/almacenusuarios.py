import os
import datetime

from clases.usuario import Usuario

class AlmacenUsuarios:

    class CamposFicheroUsuario:
        NICKNAME = 0
        PASSWORD = 1
        GMAIL = 2
        NOMBRE = 3
        APELLIDOS = 4
        FECHA_INGRESO = 5

        @staticmethod
        def opciones():
            return range(Agenda.CamposFicheroCsv.NICKNAME,
                        Agenda.CamposFicheroCsv.FECHA_INGRESO+1)

    def __init__(self):
        self._usuarios = []
        self.RUTA_FICHEROS = os.path.abspath('../autoescuelafast/files')

    def importar_usuarios(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'usuarios.csv'), 'r', encoding='UTF-8') as fichero_usuarios:
            lineas = fichero_usuarios.readlines()
            for linea in lineas:
                datos = linea.split(';')
                nickname = datos[self.CamposFicheroUsuario.NICKNAME].strip()
                password = datos[self.CamposFicheroUsuario.PASSWORD].strip()
                gmail = datos[self.CamposFicheroUsuario.GMAIL].strip()
                nombre = datos[self.CamposFicheroUsuario.NOMBRE].strip()
                apellidos = datos[self.CamposFicheroUsuario.APELLIDOS].strip()
                fecha_ingreso = datos[self.CamposFicheroUsuario.FECHA_INGRESO].strip()
                usuario = Usuario(nickname, password, gmail, nombre, apellidos, fecha_ingreso)
                self._usuarios.append(usuario) 

    def login_existencia_usuario(self, nickname_var, password_var):
        #DEBERIA PONER BIEN SU CONTRASEÑA
        for user in self._usuarios:
            if nickname_var == user._nickname and password_var == user._password:
                return True
        return False

    def comprobar_existencia_usuario(self, usuario):
        if (isinstance(usuario, Usuario) and usuario not in self._usuarios):
            return True
        return False
        
    def add_usuario(self, nickname_var, password_var, gmail_var, name_var, apellidos_var):
        fecha_ingreso_var = datetime.datetime.now().strftime("%d-%m-%Y")
        nuevo_usuario = Usuario(nickname=nickname_var, password=password_var, gmail=gmail_var, 
        nombre=name_var, apellidos=apellidos_var, fecha_ingreso=fecha_ingreso_var)     
        if self.comprobar_existencia_usuario(nuevo_usuario):
            self._usuarios.append(nuevo_usuario)
            return True
        return False
