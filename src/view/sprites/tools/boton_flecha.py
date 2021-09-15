import pygame
from view.referencias import BOTON_FLECHA


class SpriteBotonFlecha(pygame.sprite.Sprite):
    """ Un boton interactuable con forma de flecha 
        cuyo angulo puede ser modificado.
    """

    def __init__(self, alto, angulo=0):
        super().__init__()
        self.boton = [
            self._ajustar_superficie(BOTON_FLECHA['liberado'], alto, angulo),
            self._ajustar_superficie(BOTON_FLECHA['presionado'], alto, angulo)
            ]

        self.index = 0
        self.image = self.boton[self.index]

        self.rect = self.image.get_rect()

        self._precionado = False


    def _ajustar_superficie(self, superficie, alto, angulo):
        """ Aplica una cierta escala e inclinación 
            según los argumentos recibidos
        """

        superficie = self._escalar(superficie, alto)
        superficie = pygame.transform.rotozoom(superficie, angulo, 1)

        return superficie


    def get_rect(self): return self.rect


    def get_surface(self): return self.image


    def update(self):
        focus = self.rect.collidepoint(pygame.mouse.get_pos())

        if focus:
            if pygame.mouse.get_pressed()[0] and not self._precionado:
                self._precionado = not self._precionado
                self.index = 1
        
        if not pygame.mouse.get_pressed()[0] and self._precionado: 
            self._precionado = not self._precionado
            self.index = 0
            
        self.image = self.boton[self.index]

    
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
