from states import *

class ControladorEstados:
    """ Define los estados que existen en el juego y su orden
        ademas actualiza el estado por el que está transitando
        un jugador.
    """

    def __init__(self):
        Estado.contolador_estado = self

        # Secuencia ordenada de estados.
        self.estados = [Configuracion, Bautizo, Colocacion, Batalla] 
 
        self.indice = 0
        self.estado_actual = self.estados[self.indice]()


    def actualizar(self):
        self.estado_actual.actualizar()


    def siguiente_estado(self):
        """ Asigna el estado a ejecutar como el que sucede al actual."""

        self.indice += 1
        self.estado_actual = self.estados[self.indice]()