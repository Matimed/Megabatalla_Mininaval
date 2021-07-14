from Posicion import Posicion
from Tablero import Tablero
import string

class Programa:
    def __init__(self, cant_filas):
        assert cant_filas <= len(string.ascii_uppercase), "cantidad de filas mayor a cantidad de letras"

        self.posiciones = []
        for i in range(cant_filas): # La cantidad de columnas se define a partir de cant_filas
            [self.posiciones.append(Posicion(string.ascii_uppercase[i], x)) for x in range(cant_filas)]

        self.tableros = [Tablero(self.posiciones), Tablero(self.posiciones)]
        self.jugadores = []

    def validar_posicion(self, y, x):
        return (y, x) in self.posiciones

    def traducir_posicion(int, char):
        
