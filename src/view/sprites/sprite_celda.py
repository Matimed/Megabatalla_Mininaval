import pygame
from src.view.referencias import CELDA
from src.events import EventoGlobal as evento_gb
from src.events import EventoEstado as evento_estado

class SpriteCelda(pygame.sprite.Sprite):
    celda_vacia = [CELDA['libre'], CELDA['libre_presionada']]
    celda_marcada = [CELDA['marcada'], CELDA['marcada_presionada']]
    imagenes = [celda_vacia, celda_marcada]

        
    def __init__(self):
        self.image = SpriteCelda.imagenes[0][0]
        self.rect = self.image.get_rect()
        self.posicion = None
        self._presionado = False


    @staticmethod
    def set_size(nuevo_size):
        """ Escala todas las imagenes de la clase al tamaño recibido (x,y).
        """
        
        for i,lista_imagenes in enumerate(SpriteCelda.imagenes):
            lista_imagenes_escaladas = []
            
            for imagen in lista_imagenes:
                imagen_escalada = pygame.transform.scale(imagen,nuevo_size)
                lista_imagenes_escaladas.append(imagen_escalada)

            SpriteCelda.imagenes[i] = lista_imagenes_escaladas


    def update(self,eventos, marca = False):
        """Recibe un booleano que indica si la celda tiene que estar marcada.
        """

        focus = self.rect.collidepoint(pygame.mouse.get_pos())

        if focus:
            for ev in eventos:
                if ev.type == evento_gb.CLICK:
                    if ev.button == 1:
                        return True


        self.image = self.imagenes[marca][focus]
        return False


    def get_rect(self):
        return self.rect


    def set_posicion(self, posicion):
        """Recibe un objeto de tipo Posicion"""

        self.posicion = posicion


    def draw(self, surface):
        """ Recibe una superficie y se dibuja a si misma en ella."""

        surface.blit(self.image, self.rect)