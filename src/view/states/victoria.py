import pygame
from events import EventoGlobal as evento_gb
from view.states import Estado
from view.tools import SpriteCajaTexto
from view.tools import SpriteBotonTexto
from view.referencias import SONIDO_EXPLOSION
from view.referencias import VICTORIA


class Victoria(Estado):
    """ Etapa de ejecución y conclusión de los disparos
        que termina cuando todos los barcos de un jugador se hunden.
    """

    def __init__(self, ganador):
        super().__init__()
        # Sonido del ultimo barco en estallar. ;)
        pygame.mixer.Sound.play(SONIDO_EXPLOSION) 
        pygame.mixer.Sound.play(VICTORIA) 
        self.ganador = ganador
        self.sprites = self._setup_sprites()


    def actualizar(self, eventos):
        for sprite in self.sprites.values():
            if sprite.update(eventos):
                if sprite == self.sprites['bt_salir']:
                    pygame.time.wait(900)
                    salir = pygame.event.Event(evento_gb.SALIR.valor)
                    pygame.event.post(salir)

            sprite.draw(Estado.ventana_sur)

        Estado.ventana.actualizar()


    def _setup_sprites(self):
        """ Crea y ubica todos los elementos de la interfaz y
            devuelve un diccionario de los sprites y el tablero.
        """

        sprites = self._crear_sprites()
        self._posisionar_elementos(sprites)
        return sprites


    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """

        tx_titulo = SpriteCajaTexto('Ha  ganado  la  partida', (0,0,0), 28)
        tx_jugador = SpriteCajaTexto(f'{self.ganador.get_nombre()}', (0,0,0), 28)
        bt_salir = SpriteBotonTexto('Salir', 70, (0,0,0), SONIDO_EXPLOSION)

        sprites = {
            'tx_titulo' : tx_titulo,
            'bt_salir' : bt_salir,
            'tx_jugador': tx_jugador
        }

        return sprites


    def _posisionar_elementos(self, sprites):
        """ Recorre el diccionario de sprites, los ubica y
            devuelve la posiciones de origen y limite para el
            tablero.
        """

        centro_x = Estado.ventana.get_center()[0]
        centro_y = Estado.ventana.get_center()[1]

        # Posiciona los sprites de forma relativa 
        # al centro de la ventana las zonas.

        sprites['tx_titulo'].get_rect().center = (centro_x, centro_y* 1/6)
        sprites['tx_jugador'].get_rect().center = (centro_x, centro_y* 2/6)
        sprites['bt_salir'].get_rect().center = (centro_x, centro_y)
