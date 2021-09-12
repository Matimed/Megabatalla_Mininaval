import pygame
from view.referencias import BARCO

class SpriteBarco(pygame.sprite.Sprite): 
    def __init__(self):
        self.imagenes = [BARCO['sano'], BARCO['roto']]
        self.image = self.imagenes[0]
        self.rect = self.image.get_rect()
        self.posicion = None


    def update(self, hundido):
        """Recibe un booleano que indica si el barco esta hundido"""
         
        self.image = self.imagenes[hundido]


    def set_posicion(self, posicion):
        """Recibe un objeto de tipo Posicion y lo almacena"""
        self.posicion = posicion


    def ubicar(self, posX, posY):
        """ Recibe una posicion en X y una posicion en Y (int)
            y coloca el centro del barco en esa posicion"""
        
        self.rect.center(posX,posY)

