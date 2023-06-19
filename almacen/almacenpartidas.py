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
        self._aciertos_grafico_barras = []
        self._num_partida = []
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

    def crear_grafico_sectores(self, nombre_usuario):
        apto = no_apto = test_realizados = 0
        with open(os.path.join(self.RUTA_FICHEROS, 'partidas.csv'), 'r', encoding='UTF-8') as fichero_partidas:
            lineas = fichero_partidas.readlines()
            for linea in lineas:
                datos = linea.split(';')
                nickname = datos[self.CamposFicheroPartidas.NICKNAME].strip()
                if nickname == nombre_usuario:
                    aciertos = datos[self.CamposFicheroPartidas.ACIERTOS].strip()
                    tiempo = datos[self.CamposFicheroPartidas.TIEMPO].strip() #DATOS A POSTERIORI
                    if int(aciertos) > 26:
                        apto += 1
                    else:
                        no_apto += 1
                    test_realizados += 1
            return apto, no_apto, test_realizados
        
    def crear_grafico_barras(self, nombre_usuario):
        contador_partidas = 0
        with open(os.path.join(self.RUTA_FICHEROS, 'partidas.csv'), 'r', encoding='UTF-8') as fichero_partidas:
            lineas = fichero_partidas.readlines()
            lineas.reverse()
            for linea in lineas:
                datos = linea.split(';')
                nickname = datos[self.CamposFicheroPartidas.NICKNAME].strip()
                if nickname == nombre_usuario:
                    contador_partidas += 1
                    aciertos = datos[self.CamposFicheroPartidas.ACIERTOS].strip()
                    self._aciertos_grafico_barras.append(int(aciertos))
                    self._num_partida.append(contador_partidas)
                if contador_partidas > 10:
                    return self._num_partida, self._aciertos_grafico_barras
            return self._num_partida, self._aciertos_grafico_barras
                

        

        