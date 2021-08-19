from events import EventosGenerales as eventos
from model import Posicion, Tablero, Jugador
import string


class Juego:
    def __init__(self):
        self.tableros = []
        self.jugadores = []

        # Genera los tableros:
        [self.tableros.append(Tablero()) for i in range(2)]

        # Genera los jugadores:
        [self.jugadores.append(Jugador()) for i in range(2)]
        

    def actualizar(self, eventos):
        for ev in eventos:
            if ev == eventos.CONFIGURADO:
                Tablero.posiciones = self._generar_posiciones(ev.orden)
                Tablero.cant_barcos = ev.cant_barcos
                

    def _generar_posiciones(self, orden): 
        """ Dado un orden genera una lista con ese numero 
            de filas y columnas posiciones.

            Recibe:
                orden:<int>
        """

        assert type(orden) == int, (
            "La cantidad de filas y columnas"
             + " debe determinarse a través de un valor entero")

        posiciones = []    
        for i in range(orden): 
            for x in range (orden):
                posiciones.append(
                    # Se usa (x + 1) porque el tablero no tiene 0
                    Posicion(string.ascii_uppercase[i], x + 1)) 
        
        return posiciones
