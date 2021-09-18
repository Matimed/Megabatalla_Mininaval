import pygame
from view.referencias import BARCO

class SpriteBarco(pygame.sprite.Sprite): 
    imagenes = [BARCO['sano'], BARCO['roto']]
    
    def __init__(self):
        self.image = self.imagenes[0]
        self.rect = self.image.get_rect()
        self.posicion = None


    @staticmethod
    def set_size(nuevo_size):
        """ Escala todas las imagenes de la clase al tamaño recibido (x,y).
        """

        lista_imagenes_escaladas = []

        for imagen in SpriteBarco.imagenes:
            imagen_escalada = pygame.transform.scale(imagen,nuevo_size)
            lista_imagenes_escaladas.append(imagen_escalada)
        
        SpriteBarco.imagenes = lista_imagenes_escaladas


    def update(self, hundido = False):
        """Recibe un booleano que indica si el barco esta hundido"""
         
        self.image = self.imagenes[hundido]


    def set_posicion(self, posicion):
        """Recibe un objeto de tipo Posicion y lo almacena"""
        self.posicion = posicion


    def ubicar(self, posX, posY):
        """ Recibe una posicion en X y una posicion en Y (int)
            y coloca el centro del barco en esa posicion"""
        
        self.rect.center=(posX,posY)


    def draw(self, surface):
        """ Recibe una superficie y se dibuja a si mismo en ella."""

        surface.blit(self.image, self.rect)

        