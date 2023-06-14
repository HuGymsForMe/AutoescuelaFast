class Pregunta:
    def __init__(self, enunciado, opcion_1, opcion_2, opcion_3, opcion_correcta):
        self._enunciado = enunciado
        self._opcion_1 = opcion_1
        self._opcion_2 = opcion_2
        self._opcion_3 = opcion_3
        self._opcion_correcta = opcion_correcta

    def __str__(self):
        return f"{self._enunciado};{self._opcion_1};{self._opcion_2};{self._opcion_3};{self._opcion_correcta}"