from custom_errors.cell_full_error import CellFullError
from custom_errors.not_enought_boatsError import NotEnoughtBoatsError
from celda import Celda
from barco import Barco
import random

class Tablero:
    def __init__(self, posiciones, cant_barcos):
        """ Recibe una lista de objetos tipo Posicion a los que asignara
            una celda por cada uno y la cantidad de barcos que se quieren utilizar"""

        assert type(posiciones) == list
        assert type(cant_barcos) == int
        self.celdas = {}
        self.barcos_disponibles = []

        #Crea el diccionario de celdas a partir de las posiciones
        for posicion in posiciones: 
            self.celdas[posicion] = [Celda()]

        #Crea la lista de barcos de la cantidad pedida
        for i in range(cant_barcos):
            self.barcos_disponibles.append(Barco())


    def get_celda(self, posicion):
            """Dada una posicion devuelve la celda correspondiente"""

            if posicion in self.celdas:
                return self.celdas.get(posicion)[0]
            else:
                raise ValueError("La posicion no esta en la lista")


    def agregar_barco(self, posicion):
        """ Recibe una instancia de Posicion y agrega, si es posible, 
            un barco en la celda que corresponda con dicha Posicion"""
  
        if self.get_barcos_disponibles(): 
            celda = self.get_celda(posicion)
            celda.agregar_barco(self.barcos_disponibles.pop())

        else: raise NotEnoughtBoatsError()
        

    def quitar_barco(self, posicion):
        """ Recibe una instancia de Posicion y 
            quita el barco de la celda correspondiente con esta"""

        celda = self.get_celda(posicion)
        self.barcos_disponibles.append(celda.quitar_barco())


    def get_barcos_disponibles(self):
        """ Devuelve un numero que representa la cantidad de barcos 
            que aún no están en una Celda"""

        return len(self.barcos_disponibles)
    

    def ubicacion_aleatoria(self):
        """ Mientras hayan barcos disponibles 
            toma una Posicion aleatoria de su diccionario de celdas e 
            intenta agregar un barco en ella, 
            si falla lo vuelve a intentar con otra Posicion"""

        while self.get_barcos_disponibles():
            posicion = random.choice(list(self.celdas.keys()))

            try:
                self.agregar_barco(posicion)

            except (CellFullError): pass