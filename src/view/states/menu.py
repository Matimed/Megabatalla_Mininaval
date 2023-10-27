import pygame
from src.events import EventoEstado as evento_estado
from src.events import EventoGlobal as evento_gb
from src.view.states import Estado
from src.view.tools import SpriteCajaTexto
from src.view.tools import SpriteBotonTexto
from src.view.referencias import SONIDO_EXPLOSION

class Menu(Estado):
    def __init__(self):
        super().__init__()
        Estado.ventana.set_fondo((192, 192, 192))
        self.sprites = self._crear_sprites()


    def actualizar(self, eventos):
        for sprite in self.sprites.values():
            if sprite.update(eventos):
                if sprite == self.sprites['bt_jugar']:
                    finalizar_estado = pygame.event.Event(
                                        evento_gb.ESTADO.valor, 
                                        tipo=evento_estado.FINALIZAR_ESTADO, 
                                        estado=Menu
                                        )
                                        
                    pygame.event.post(finalizar_estado)


                if sprite == self.sprites['bt_salir']:
                    pygame.time.wait(900)
                    salir = pygame.event.Event(evento_gb.SALIR.valor)
                    pygame.event.post(salir)
            sprite.draw(Estado.ventana_sur)

        Estado.ventana.actualizar()


    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """

        tx_titulo = SpriteCajaTexto('Megabatalla Mininaval', (0,0,0), 36)
        bt_jugar = SpriteBotonTexto('Jugar', 70, (0,0,0), SONIDO_EXPLOSION)
        bt_salir = SpriteBotonTexto('Salir', 70, (0,0,0), SONIDO_EXPLOSION)
        
        centro_x = Estado.ventana.get_center()[0]
        centro_y = Estado.ventana.get_center()[1]

        # Posiciona los sprites de forma
        # relativa al centro de la ventana.

        tx_titulo.get_rect().center = (centro_x, centro_y - centro_y* 2/3 )
        bt_jugar.get_rect().center = (centro_x, centro_y - centro_y* 1/6)
        bt_salir.get_rect().center = (centro_x, centro_y + centro_y* 1/3)

        sprites = {
            'tx_titulo' : tx_titulo,
            'bt_jugar' : bt_jugar,
            'bt_salir' : bt_salir
        }

        return sprites

