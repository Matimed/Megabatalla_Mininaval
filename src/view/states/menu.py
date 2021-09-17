import pygame
from events import EventoEstado as evento_estado
from events import EventoGlobal as evento_gb
from view.states import Estado
from view.tools import SpriteCajaTexto
from view.tools import SpriteBotonTexto


class Menu(Estado):
    def __init__(self):
        super().__init__()
        Estado.ventana.set_fondo((255,255,255))
        self.sprites = self._crear_sprites()


    def actualizar(self, eventos):
        for sprite in self.sprites.values():
            if sprite.update():
                if sprite == self.sprites['btJugar']:
                    finalizar_estado = pygame.event.Event(evento_gb.ESTADO.valor, tipo=evento_estado.FINALIZAR_ESTADO, estado=Menu)
                    pygame.event.post(finalizar_estado)


                if sprite == self.sprites['btSalir']:
                    salir = pygame.event.Event(evento_gb.SALIR.valor)
                    pygame.event.post(salir)
            sprite.draw(Estado.ventana_sur)

        Estado.ventana.actualizar()


    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """

        titulo = SpriteCajaTexto('Batalla      Naval', (0,0,0), 36)
        btJugar = SpriteBotonTexto('Jugar', 70)
        btSalir = SpriteBotonTexto('Salir', 70)
        
        centro_x = Estado.ventana.get_center()[0]
        centro_y = Estado.ventana.get_center()[1]

        # Posiciona los sprites de forma
        # relativa al tamaño de la ventana.

        titulo.get_rect().center = (centro_x, centro_y - centro_y* 2/3 )
        btJugar.get_rect().center = (centro_x, centro_y - centro_y* 1/4)
        btSalir.get_rect().center = (centro_x, centro_y + centro_y* 1/4)

        sprites = {
            'titulo' : titulo,
            'btJugar' : btJugar,
            'btSalir' : btSalir
        }

        return sprites

