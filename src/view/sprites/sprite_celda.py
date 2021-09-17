import pygame
from view.referencias import CELDA
from events import EventoGlobal as evento_gb
from events import EventoEstado as evento_estado

class SpriteCelda(pygame.sprite.Sprite):

    def __init__(self):

        self.imagenes = [CELDA['libre'], CELDA['marcada']]
        self.image = self.imagenes[0]
        self.rect = self.image.get_rect()
        self.posicion = None
        self._presionado = False


    def update(self, marca = False):
        """Recibe un booleano que indica si la celda tiene que estar marcada"""

        self.image = self.imagenes[marca]

        if pygame.mouse.get_pressed()[0] and not self._presionado:
            self._presionado = not self._presionado
            pulsar = pygame.event.Event(
                        evento_gb.ESTADO, 
                        tipo = evento_estado.CELDA, 
                        posicion = self.posicion
                        )
            pygame.post(pulsar)

        if not pygame.mouse.get_pressed()[0] and self._presionado: 
            self._presionado = not self._presionado


    def get_rect(self):
        return self.rect


    def set_posicion(self, posicion):
        """Recibe un objeto de tipo Posicion"""

        self.posicion = posicion


    def draw(self, surface):
        """ Recibe una superficie y se dibuja a si misma en ella."""

        surface.blit(self.image, self.rect)

