import pygame
from view.referencias import FUENTE


class SpriteCajaTexto(pygame.sprite.Sprite):
    """ Clase para representar un texto en pantalla."""

    def __init__(self, texto, color=(0,0,0), alto=8):
        super().__init__()
        
        self.image = self._escalar(FUENTE.render(texto, True, color), alto)
        self.rect = self.image.get_rect()


    def _escalar(self, superficie, alto):
        """ Escala una superficie a un cierto alto.
            
            Recibe:
                superficie:<Surface>
                alto:<int>
        """

        largo_nativo = superficie.get_size()[0]
        alto_nativo = superficie.get_size()[1]

        escala = alto // alto_nativo

        return pygame.transform.scale(
            superficie, (largo_nativo * escala, alto_nativo  * escala)
            )


    def get_rect(self): return self.rect


    def get_surface(self): return self.image


    def get_tamaño(self): return self.image.get_size()

    
    def draw(self, surface):
        """ Recibe una superficie y se dibuja a si misma en ella."""

        surface.blit(self.image, self.rect)
