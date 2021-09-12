import pygame
from view.referencias import CELDA
from events import EventoPulsacion as evPulsacion
from events import EventoGlobal as evGlobal

class SpriteCelda(pygame.sprite.Sprite):

    def __init__(self):

        self.imagenes = [CELDA['libre'], CELDA['marcada']]
        self.image = self.imagenes[0]
        self.rect = self.image.get_rect()
        self.posicion = None

    def update(self, marca):
        """Recibe un booleano que indica si la celda tiene que estar marcada"""

        self.image = self.imagenes[marca]

        if  pygame.mouse.get_pressed()[0]: 
            pulsar = pygame.event.Event(
                        evGlobal.PULSACION, 
                        tipo = evPulsacion.CELDA, 
                        posicion = self.posicion
                        )
            pygame.post(pulsar)


    def get_rect(self):
        return self.rect

    def set_posicion(self, posicion):
        """Recibe un objeto de tipo Posicion"""

        self.posicion = posicion

