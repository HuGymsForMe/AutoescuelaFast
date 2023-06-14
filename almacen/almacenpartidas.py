import os
import random

from clases.partidas import Partida

class AlmacenPartidas:
    class CamposFicheroPartidas:
        NICKNAME = 0
        ID_PARTIDA = 1
        ACIERTOS = 2
        FALLOS = 3
        TIEMPO = 4

    def __init__(self):
        self._partidas = []
        self._id_partida = []
        self.RUTA_FICHEROS = os.path.abspath('../autoescuelafast/files')

    def importar_partidas(self):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'partidas.csv'), 'r', encoding='UTF-8') as fichero_partidas:
                lineas = fichero_partidas.readlines()
                for linea in lineas:
                    datos = linea.split(';')
                    nickname = datos[self.CamposFicheroPartidas.NICKNAME].strip()
                    id_partida = datos[self.CamposFicheroPartidas.ID_PARTIDA].strip()
                    aciertos = datos[self.CamposFicheroPartidas.ACIERTOS].strip()
                    fallos = datos[self.CamposFicheroPartidas.FALLOS].strip()
                    tiempo = datos[self.CamposFicheroPartidas.TIEMPO].strip()
                    partida = Partida(nickname, id_partida, aciertos, fallos, tiempo)
                    self._partidas.append(partida)
                    self._id_partida.append(id_partida)
        except IndexError:
            pass

    def add_partida(self, nickname, aciertos, fallos, tiempo):
        aniadido = True
        while aniadido:
            id_partida = f"P{random.randint(1, 1001)}"
            if id_partida not in self._id_partida:
                self._id_partida.append(id_partida)
                aniadido = False
        partida = Partida(nickname, id_partida, aciertos, fallos, tiempo)
        self._partidas.append(partida)
        with open(os.path.join(self.RUTA_FICHEROS, 'partidas.csv'), 'a', encoding='UTF-8') as fichero_partidas:
            nueva_partida = f"{str(partida)}\n"
            fichero_partidas.write(nueva_partida)

        