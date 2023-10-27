import pygame
from src.view.referencias import FUENTE


class SpriteCajaTexto(pygame.sprite.Sprite):
    """ Clase para representar un texto en pantalla."""

    def __init__(self, texto, color=(0,0,0), alto=8):
        super().__init__()
        self.color = color
        self.alto = alto

        self.rect = None
        self.image = None

        self.set_texto(texto) 
        self.texto = self.get_texto()
        
        


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


    def set_texto(self, texto):


        if texto == '': texto = ' '
        
        # Le agrega espacios a las palabras 
        # porque la fuente tiene espacios muy cortos.
        self.texto = texto
        texto_tabulado = texto.replace(' ', '    ')
        
        self.image = self._escalar(FUENTE.render(texto_tabulado, True, self.color), self.alto)
        
        if self.rect:   
            ubicacion= self.rect.center
        else :  
            ubicacion = (0,0)
        
        self.rect = self.image.get_rect()
        self.rect.center = ubicacion

    
    def get_texto(self):
        texto = self.texto
        if texto == ' ': texto = ''
        return texto