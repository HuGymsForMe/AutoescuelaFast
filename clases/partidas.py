class Partida:
    def __init__(self, nickname, id_partida, aciertos, fallos, tiempo):
        self._nickname = nickname
        self._id_partida = id_partida
        self._aciertos = aciertos
        self._fallos = fallos
        self._tiempo = tiempo

    def __str__(self):
        return f"{self._nickname};{self._id_partida};{self._aciertos};{self._fallos};{self._tiempo}"
