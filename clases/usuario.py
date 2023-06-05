class Usuario:
    def __init__(self, nickname, password, gmail, nombre, apellidos, fecha_ingreso):
        self._nickname = nickname
        self._password = password
        self._gmail = gmail
        self._nombre = nombre
        self._apellidos = apellidos
        self._fecha_ingreso = fecha_ingreso

    def __str__(self):
        return f"{self._nickname};{self._password};{self._gmail};{self._nombre};{self._apellidos};{self._fecha_ingreso}"

    def __eq__(self, other):
        if isinstance(other, Usuario):
            return self._nickname == other._nickname
        return False


