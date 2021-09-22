import pygame
from pygame.sprite import AbstractGroup
from events import EventoGlobal as evento_gb
from events import EventoTablero as evento_tablero
from view.sprites import SpriteCelda
from view.sprites import SpriteBarco
import string
from view.referencias import SONIDO_AGUA

class TableroView(AbstractGroup):
    def __init__(self, cant_barcos, posiciones, origen, limite):
        assert (origen[0] < limite[0]) and (origen[1] < limite[1]), (
        "El origen y el limite no forman un cuadrilatero"
        )

        assert cant_barcos <= len(posiciones), (
            'No pueden haber mas barcos que posiciones.'
        )

        # La raiz de la cantidad de posiciones es el ancho y alto del tablero.
        orden = int(len(posiciones)**(1/2))
        self.set_size(origen, limite, orden)
        
        self.posiciones = self._generar_matriz_posiciones(posiciones)
        self.celdas = self._generar_celdas(posiciones)
        self.barcos = self._generar_barcos(cant_barcos)

        self._ubicar_celdas(self.celdas, origen)


    def update_batalla(self, eventos, pos_barcos_marcados, pos_celdas_marcadas,):
        """ Actualiza el estado de todos los sprites del tablero en
            base a los argumentos dados y devuelve los barcos visibles. 

            Recibe:
                pos_barcos: Posicion[]    
                pos_celdas_marcadas: Posicion[]

            Devuelve:
                barcos: SpriteBarco[]
        """

        barcos = self._ubicar_barcos(pos_barcos_marcados)

        for barco in barcos:
            barco.update(True)
        
        for fila in self.posiciones:
            for posicion in fila:
                
                marcada = (posicion in pos_celdas_marcadas) and not (posicion in pos_barcos_marcados)
                index=self.convertir_posicion_index(posicion)
                self.celdas[index[0]][index[1]].update(eventos, marcada)
       
        for y,fila in enumerate(self.celdas):
            for x,celda in enumerate(fila):

                # Verifica que la celda no haya sido marcada con anterioridad.
                ya_marcada = (self.posiciones[x][y] in pos_celdas_marcadas)
                if celda.update(eventos,False): 
                    evento = self._disparar(self.posiciones[y][x])

                    if evento: pygame.event.post(evento)

        return barcos


    def update_colocacion(self,eventos, pos_barcos, barco_disponible):
        """ Actualiza el estado de todos los sprites del tablero
            recibiendo una lista de Posiciones con los barcos colocados 
            y un booleano que indica si quedan barcos disponibles para colocar
            y devuelve los barcos visibles. 

            Recibe:
                pos_barcos: Posicion[]   
                barco_disponible: boolean

            Devuelve:
                barcos: SpriteBarco[]
        """

        barcos = self._ubicar_barcos(pos_barcos)
        
        for barco in barcos:
            barco.update(False)
        
        for y,fila in enumerate(self.celdas):
            for x,celda in enumerate(fila):
                if celda.update(eventos,False):
                    evento = self. _interactuar_barco(
                                self.posiciones[y][x], 
                                pos_barcos,
                                barco_disponible
                                )

                    if evento:
                        pygame.mixer.Sound.play(SONIDO_AGUA) 
                        pygame.event.post(evento)

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


    def _generar_celdas(self, posiciones):
        """ Recibe una lista de posiciones y genera 
            una matriz bidimensional de SpritesCeldas ordenadas.
        """

        celdas = []
        # La raiz de la cantidad de posiciones es el ancho y alto del tablero 
        orden = int(len(posiciones)**(1/2))

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


    def convertir_posicion_index(self, posicion):
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
            barco.ubicar(celda.get_rect().centerx, celda.get_rect().centery)
            barcos_visibles.append(barco)
        

        return barcos_visibles
        

    def _interactuar_barco(self, pos_celda, pos_barcos, barco_disponible):
        """ Recibe la posicion de la celda con la que se va a interactuar,
            una la lista de los barcos colocado y un booleano que indica 
            si quedan barcos disponibles para colocar.
        """


        evento = None
        
        if pos_celda in pos_barcos:
            evento = pygame.event.Event(
                            evento_gb.TABLERO.valor, 
                            tipo= evento_tablero.QUITAR_BARCO,
                            posicion = pos_celda
                            )
        else:
            if barco_disponible:
                evento = pygame.event.Event(
                            evento_gb.TABLERO.valor, 
                            tipo= evento_tablero.COLOCAR_BARCO,
                            posicion = pos_celda
                            )
        
        return evento


    def _disparar(self, pos_celda):
        """ Recibe la posicion de la celda donde se pretende disparar.
        """

        return pygame.event.Event(
                        evento_gb.DISPARAR.valor, 
                        posicion= pos_celda
                        )
        

    def set_size(self, origen, limite, orden):
        size_x = int((limite[0] - origen[0]) / orden)
        size_y = int((limite[1] - origen[1]) / orden)
        
        SpriteCelda.set_size((size_x, size_y))
        SpriteBarco.set_size((size_x, size_y))