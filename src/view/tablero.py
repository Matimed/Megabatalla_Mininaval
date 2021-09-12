from pygame.sprite import AbstractGroup
from model import barco
from view.sprites import SpriteCelda
from view.sprites import SpriteBarco

class TableroView(AbstractGroup):
    def __init__(self):
        self.celdas = {}
        self.barcos = []

    
    def generar_celdas(self, orden):
        """ Recibe el orden del tablero y genera 
            los SpritesCeldas necesarios para llenarlo."""

        celdas = []
        [celdas.append(SpriteCelda()) for i in range (orden**2)]
        return celdas


    def generar_barcos(self, cant_barcos):
        """ Recibe la cantidad de barcos requerida y llena la lista de
            barcos ocultos con esa cantidad de SpriteBarcos."""

        [self.barcos.append(SpriteBarco()) for i in range (cant_barcos)]


    def ubicar_celdas(self, posiciones, celdas, origen):
        """ Recorre todas las Posiciones y asigna un SpriteCelda
            a cada una de manera ordenada.
            
            Recibe:
                posiciones:<Posicion>[]
                celdas:<SpriteCelda>[]
                origen: <Tuple> (x: <int>, y: <int>)
        """ 

        # La raiz de la cantidad de posiciones es el ancho y alto de la matriz 
        orden = len(posiciones)**(1/2) 
        celdas = iter(celdas)
        posiciones = iter(posiciones)

        for fila in range(orden):
            celda_actual = next(celdas)         
            self.celdas[next(posiciones)] = celda_actual

            # La celda inicial es la primer celda de cada fila
            celda_inicial = celda_actual

            # La celda anterior es la última celda ubicada
            celda_anterior = celda_actual
            

            # Si es la primera celda la pone en el origen, de lo contrario 
            # la pone debajo de la primera celda de la fila anterior.
            if (celda_actual == posiciones[0]):
                celda_actual.get_rect().topleft = origen
            else:
                celda_actual.get_rect().midtop = celda_inicial.get_rect().midbottom
            

            for columna in range(orden-1): # -1 porque la primera celda la pone la fila
                celda_actual = next(celdas)
                self.celdas[next(posiciones)] = celda_actual

                celda_actual.get_rect().midleft = celda_anterior.get_rect().midright
                celda_anterior = celda_actual


    def asignar_posiciones_celdas(self):
        """ Recorre el diccionario de celdas y le indica
            a cada una de ellas cual es su posición."""

        for posicion in self.celdas:
            celda = self.celdas[posicion]
            celda.set_posicion(posicion)


    def ubicar_barcos(self, posiciones):
        """ Recibe una lista de objetos de tipo Posicion que ubican
            todos los barcos que deben visualizarse en pantalla
            y devuelve una lista con todos los objetos tipo SpriteBarco
            que se deben dibujar en pantalla."""

        barcos = iter(self.barcos)
        barcos_visibles = []
        for posicion in posiciones:
            celda = self.celdas[posicion]
            barco = next(barcos)

            # Ubica el barco en el medio de la celda correspondiente.
            barco.ubicar(celda.get_rect().center)
            barcos_visibles.append(barco)
        
        return barcos_visibles






                
            
