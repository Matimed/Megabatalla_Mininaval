import pygame
from view.referencias import SONIDO_AGUA
from view.referencias import SONIDO_EXPLOSION
from events import EventoGlobal as evento_gb
from events import EventoBatalla as evento_bt
from view.states import Estado
from view.tablero import TableroView
from view.tools import SpriteCajaTexto


class Batalla(Estado):
    """ Etapa de ejecución y conclusión de los disparos
        que termina cuando todos los barcos de un jugador se hunden.
    """

    def __init__(self, juego):
        super().__init__()
        self.juego = juego
        self.jugadores = self.juego.get_jugadores()
        self.modelo_tableros = self.juego.get_tableros()
        self.sprites, self.vista_tablero = self._setup_interfaz()

        # Se necesita para poder dibujar el tablero por primera vez.
        self.barcos = self.vista_tablero.update_batalla(
                    [],
                    self._get_pos_barcos_hundidos(),
                    self._get_pos_celdas_marcadas()
                    ) 


    def actualizar(self, eventos):
        # Es necesario que el tablero se dibuje antes 
        # de que se actualicen los barcos. Esto para que
        # pueda escucharse un sonido antes de que cambie el turno.
        self.vista_tablero.draw(Estado.ventana_sur, self.barcos)

        for ev in eventos:
            if ev.type == evento_gb.BATALLA:
                if ev.tipo == evento_bt.AGUA:
                    pygame.mixer.Sound.play(SONIDO_AGUA)
                    pygame.time.wait(900)
                    eventos.remove(ev)

                elif ev.tipo == evento_bt.BARCO_DAÑADO:
                    pygame.mixer.Sound.play(SONIDO_EXPLOSION)
                    eventos.remove(ev)


        for sprite in self.sprites.values():
            sprite.update(eventos)
            sprite.draw(Estado.ventana_sur)


        self.barcos = self.vista_tablero.update_batalla(
                    eventos,
                    self._get_pos_barcos_hundidos(),
                    self._get_pos_celdas_marcadas()
                    ) 

        Estado.ventana.actualizar()
        self.actualizar_turno()


    def actualizar_turno(self):
        self.sprites['tx_turno'].set_texto(
            f'Es el turno de {self.jugadores[self.get_turno()]}'
            )


    def _setup_interfaz(self):
        """ Crea y ubica todos los elementos de la interfaz y
            devuelve un diccionario de los sprites y el tablero.
        """

        sprites = self._crear_sprites()
        origen,limite = self._posisionar_elementos(sprites)
        tablero = self._crear_tablero(origen, limite)
        return sprites, tablero


    def _crear_tablero(self, origen, limite):
        turno = self.get_turno()
        cant_barcos = self.modelo_tableros[turno].get_cant_barcos()
        posiciones =  self.modelo_tableros[turno].get_posiciones()


        return TableroView(cant_barcos, posiciones, origen, limite)

    
    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """

        tx_titulo = SpriteCajaTexto('Dispara a tu enemigo', (0,0,0), 28)
        tx_turno = SpriteCajaTexto(
            f'Es el turno de {self.jugadores[self.get_turno()]}', (0,0,0), 18
            )

        sprites = {
            'tx_titulo' : tx_titulo,
            'tx_turno' : tx_turno,
        }
        return sprites


    def _posisionar_elementos(self, sprites):
        """ Recorre el diccionario de sprites, los ubica y
            devuelve la posiciones de origen y limite para el
            tablero.
        """

        centro_x = Estado.ventana.get_center()[0]
        centro_y = Estado.ventana.get_center()[1]

        origen_tablero = (centro_x*7/12, centro_y * 4/10)
        limite_tablero = (centro_x*17/12, centro_y*17/10)

        # Posiciona los sprites de forma relativa 
        # al centro de la ventana las zonas.

        sprites['tx_titulo'].get_rect().center = (centro_x, centro_y* 1/6 )
        
        sprites['tx_turno'].get_rect().center = (
            centro_x, centro_y*6/20
            )

        return origen_tablero, limite_tablero


    def get_turno(self):
        """ Devuelve el turno actual según el modelo."""

        return self.juego.get_turno()


    def _get_pos_barcos_hundidos(self):
        """ Devuelve la Posicion de los barcos hundidos 
            del jugador que no tiene el turno.
        """

        # Toma el turno del contrario.
        # Solo funciona con dos jugadores 0 y 1.
        turno = not self.get_turno() 
        return self.modelo_tableros[turno].get_barcos_hundidos()


    def _get_pos_celdas_marcadas(self):
        """ Devuelve la Posicion de las celdas marcadas."""

        turno = not self.get_turno()
        return self.modelo_tableros[turno].get_celdas_marcadas()


    
    def _get_barcos(self):
        return self.modelo_tableros[not self.get_turno()].get_barcos()