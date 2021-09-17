from view.states import Estado
from view.tablero import TableroView

class Colocacion(Estado):
    """ Etapa donde los jugadores distribuyen sus barcos
        en posiciones determinadas de sus tableros
        que termina cuando todos los barcos de ambos jugadores
        fueron colocados de manera satisfactoria.
    """

    def __init__(self, tableros):
        """ Recibe la referencia del tablero del modelo 
            para poder comunicarse con él."""

        super().__init__()
        self.modelo_tableros = tableros
        self.vista_tablero = self._crear_tablero()


    def _crear_tablero(self):
        cant_barcos = self.modelo_tableros[0].cant_barcos
        posiciones =  self.modelo_tableros[0].posiciones
         
        return TableroView(cant_barcos, posiciones, (0,0),(50,50))