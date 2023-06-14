import os

from clases.preguntas import Pregunta
class AlmacenPreguntas:
    class CamposFicheroPreguntas:
        ENUNCIADO = 0
        OPCION_1 = 1
        OPCION_2 = 2
        OPCION_3 = 3
        OPCION_CORRECTA = 4

    def __init__(self):
        self._preguntas = []
        self.RUTA_FICHEROS = os.path.abspath('../autoescuelafast/files')

    def importar_preguntas(self):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'preguntas.csv'), 'r', newline="", encoding='UTF-8') as fichero_preguntas:
                lineas = fichero_preguntas.readlines()
                for linea in lineas:
                    linea = linea.replace("\\n", "\n")
                    datos = linea.split(';')
                    enunciado = datos[self.CamposFicheroPreguntas.ENUNCIADO].strip()
                    opcion_1 = datos[self.CamposFicheroPreguntas.OPCION_1].strip()
                    opcion_2 = datos[self.CamposFicheroPreguntas.OPCION_2].strip()
                    opcion_3 = datos[self.CamposFicheroPreguntas.OPCION_3].strip()
                    opcion_correcta = datos[self.CamposFicheroPreguntas.OPCION_CORRECTA].strip()
                    pregunta = Pregunta(enunciado, opcion_1, opcion_2, opcion_3, opcion_correcta)
                    self._preguntas.append(pregunta)
                return self._preguntas
        except IndexError:
            pass
