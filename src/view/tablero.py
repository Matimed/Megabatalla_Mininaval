import pygame
from pygame.sprite import AbstractGroup
from view.sprites import SpriteCelda
from view.sprites import SpriteBarco
import string

class TableroView(AbstractGroup):
    def __init__(self, cant_barcos, posiciones, origen, limite):
        # Verifica que el origen y el limite formen un cuadrado.
        assert (origen[0] < limite[0]) and (origen[1] < limite[1])

        
        self.posiciones = self._generar_matriz_posiciones(posiciones)
        self.celdas = self._preparar_celdas(posiciones, origen, limite)
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
            
            for fila in self.posiciones:
                for posicion in fila:
                    
                    marcada = posicion in pos_celdas_marcadas
                    index=self.convertir_posicion_index(posicion)
                    self.celdas[index[0]][index[1]].update(marcada)
        else:
            for barco in barcos:
                barco.update(False)
            
            for fila in self.celdas:
                for celda in fila:
                    celda.update(False)

        return barcos


    def draw(self, surface, barcos):
        """ Recibe una superficie (Surface) y una lista de objetos SpriteBarco
            y coloca en ella todos los sprites del tablero.
        """

        for fila in self.celdas:
            for celda in fila:
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


    def _preparar_celdas(self, posiciones, origen, limite):
        """ Segun la lista de objetos tipo Posicion dada genera y ubica
            una celda por cada posicion y devuelve dicha lista.
        """
        
        celdas = self._generar_celdas(posiciones, origen, limite)
        self._ubicar_celdas(celdas, origen)
        return celdas


    def _ubicar_celdas(self, celdas, origen):
        """ Recorre todas las celdas y las posiciona de manera ordenada.
            
            Recibe:
                celdas:<SpriteCelda> matriz[*][*]
                origen: <Tuple> (x: <int>, y: <int>)
        """ 
        
        for fila in celdas:
            for celda in fila:
                celda.rect.topleft = origen
                origen = celda.rect.topright
            
            origen = fila[0].rect.bottomleft


    def _generar_celdas(self, posiciones, origen, limite):
        """ Recibe una lista de posiciones y genera 
            una matriz bidimensional de SpritesCeldas ordenadas.
        """

        celdas = []
        # La raiz de la cantidad de posiciones es el ancho y alto de la matriz 
        orden = int(len(posiciones)**(1/2))

        SpriteCelda.set_tamaño((
            int((limite[0] - origen[0]) / orden), 
            int((limite[1] - origen[1]) / orden)
            ))

        for y in range(orden):
            lista_columnas = []

            for x in range(orden):
                celda = SpriteCelda()

                index_actual = x + y * orden
                celda.set_posicion(posiciones[index_actual])
                lista_columnas.append(celda)
            
            celdas.append(lista_columnas)

        return celdas


    def _generar_matriz_posiciones(self, posiciones):
        matriz = []
        orden = int(len(posiciones)**(1/2))
        for y in range(orden):
            lista_columnas = []

            for x in range(orden): 
                index_actual = x + y * orden
                lista_columnas.append(posiciones[index_actual])
            
            matriz.append(lista_columnas)

        return matriz

    def convertir_posicion_index(posicion):
        """ Recibe un objeto tipo Posicion y 
            devuelve el index de matriz donde se encuentra.
        """

        pos = posicion.convertir_tupla()
        pos_y = string.ascii_uppercase.find(pos[0])
        pos_x = pos[1] - 1
        return (pos_y, pos_x)


    def _ubicar_barcos(self, posiciones):
        """ Recibe una lista de objetos de tipo Posicion que ubican
            todos los barcos que deben visualizarse en pantalla
            y devuelve una lista con todos los objetos tipo SpriteBarco
            que se deben dibujar en pantalla."""

        barcos = iter(self.barcos)
        barcos_visibles = []
        
        for posicion in posiciones:
            index = self.convertir_posicion_index(posicion)
            self.celdas[index[0]][index[1]]
        
        for posicion in posiciones:
            index = self.convertir_posicion_index(posicion)
            celda = self.celdas[index[0]][index[1]]
            barco = next(barcos)

            # Ubica el barco en el medio de la celda correspondiente.
            barco.ubicar(celda.get_rect().center)
            barcos_visibles.append(barco)
        

        return barcos_visibles
        


    def set_size(self, origen, limite, orden):
        size_x = int((limite[0] - origen[0]) / orden)
        size_y = int((limite[1] - origen[1]) / orden)
        
        SpriteCelda.set_size((size_x, size_y))
        SpriteBarco.set_size((size_x, size_y))

