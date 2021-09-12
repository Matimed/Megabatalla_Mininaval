from pygame.sprite import AbstractGroup
from view.sprites import SpriteCelda
from view.sprites import SpriteBarco

class TableroView(AbstractGroup):
    def __init__(self, cant_barcos, posiciones):
        self.celdas = self._preparar_celdas(posiciones)
        self.barcos = self._generar_barcos(cant_barcos)


    def update(self, pos_barcos, pos_celdas_marcadas = []):
        """ Actualiza el estado de todos los sprites del tablero en
            base a los argumentos dados y devuelve los barcos visibles. 

            Recibe:
                pos_barcos: Posicion[]    
                pos_celdas_marcadas: Posicion[]

            Devuelve:
                barcos: SpriteBarco[]
        """

        barcos = self._ubicar_barcos(pos_barcos)
        if pos_celdas_marcadas:
            for barco in barcos:
                barco.update(True)
            for posicion in self.celdas.keys:
                marcada = posicion in pos_celdas_marcadas
                self.celdas[posicion].update(marcada)
        else:
            for barco in barcos:
                barco.update(False)
            for celda in self.celdas.values:
                celda.update(False)
        
        return barcos


    def draw(self, surface, barcos):
        """ Recibe una superficie (Surface) y una lista de objetos SpriteBarco
            y coloca en ella todos los sprites del tablero.
        """

        for celda in self.celdas.values():
            celda.draw(surface)
        for barco in barcos:
            barco.draw(surface)


    def _generar_barcos(self, cant_barcos):
        """ Genera la cantidad pedida de objetos tipo SpriteBarco
            y devuelve una lista con todos los objetos creados.
        """

        barcos = []
        [barcos.append(SpriteBarco()) for i in range (cant_barcos)]
        return barcos


    def _preparar_celdas(self, posiciones):
        """ Segun la lista de objetos tipo Posicion dada genera y ubica
            una celda por cada posicion y devuelve dicha lista.
        """
        
        celdas = self._generar_celdas(posiciones)
        self._ubicar_celdas(posiciones, celdas)
        self._asignar_posiciones_celdas(celdas)
        return celdas


    def _generar_celdas(self, posiciones):
        """ Recibe una lista de posiciones y genera 
            un SpritesCelda por cada una."""

        celdas = []
        [celdas.append(SpriteCelda()) for i in range (len(posiciones))]
        return celdas


    def _ubicar_celdas(self, posiciones, celdas, origen):
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


    def _asignar_posiciones_celdas(self, celdas):
        """ Recorre un diccionario de celdas y le indica
            a cada una de ellas cual es su posición."""

        for posicion in celdas:
            celda = celdas[posicion]
            celda.set_posicion(posicion)


    def _ubicar_barcos(self, posiciones):
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
        
