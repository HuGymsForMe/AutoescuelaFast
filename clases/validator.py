import re

class Validator:
    def __init__(self):
        self.patron = None

    def validar_contrasenia(self, password_var):
        self.patron = r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$'
        if re.match(self.patron, password_var):
            return True
        else:
            return False