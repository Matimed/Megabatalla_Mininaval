import pygame
from view.sprites.tools import SpriteCajaTexto
from view.referencias import BOTON_TEXTO


class SpriteBotonTexto(pygame.sprite.Sprite):
    """ Un botón interactuable que ajusta su largo según el texto que contenga.
        Posee dos estados que son: precionado y liberado (sin precionar).
        Lo unico que cambia entre estos dos estados es la parte derecha del botón.
    """

    def __init__(self, texto, alto, color=(0,0,0)):
        super().__init__()
        
        self.texto = SpriteCajaTexto(texto, color)
        self.alto = alto

        self.tamaño_nativo = self._get_tamaño_nativo() # Tamaño del boton sin escalar.        
        self.boton = self._crear_imagenes()
        self.index = 0
        self.image = self.boton[self.index]
        self.rect = self.image.get_rect()


    def _get_tamaño_nativo(self):
        """ Obtiene el tamaño del botón según su atributo texto."""

        alto = BOTON_TEXTO['izquierda'].get_size()[1]
        
        ancho = BOTON_TEXTO['izquierda'].get_size()[0]
        ancho += BOTON_TEXTO['centro'].get_size()[0] * (self.texto.get_tamaño()[0] - 1)
        ancho += BOTON_TEXTO['derecha'].get_size()[0]        

        return [ancho, alto]


    def _crear_imagenes(self):
        """ Crea las superficies del botón precionado 
            y el botón sin liberado (sin precionar).
        """

        superficies = [] 
        superficies.append(
            pygame.Surface(self.tamaño_nativo, pygame.SRCALPHA)
            ) 

        self._dibujar_parte_izquierda(superficies[0])
        self._dibujar_parte_central(superficies[0])
        self._dibujar_texto(superficies[0])

        superficies.append(superficies[0].copy()) 

        self._dibujar_parte_derecha(superficies[0])
        self._dibujar_parte_derecha(superficies[1], True)

        for i in range(len(superficies)):
            superficies[i] = self._escalar(superficies[i], self.alto)

        return superficies


    def _dibujar_parte_izquierda(self, superficie):
        """ En la superficie recibida por argumento dibuja 
            la parte izquierda que tendrá el botón.
        """

        superficie.blit(BOTON_TEXTO['izquierda'], (0, 0))


    def _dibujar_parte_central(self, superficie):
        """ En la superficie recibida por argumento dibuja 
            la parte central que tendrá el botón.
        """

        for i in range(
                BOTON_TEXTO['izquierda'].get_size()[0], 
                self.tamaño_nativo[0] - BOTON_TEXTO['derecha'].get_size()[0], 
                BOTON_TEXTO['centro'].get_size()[0]):
            
            superficie.blit(BOTON_TEXTO['centro'], (i, 0))

        
    def _dibujar_parte_derecha(self, superficie, roja=False):
        """ Dependiendo de su argumento 'roja' dibuja 
            en la superficie pasada por argumento la parte derecha
            que tendrá el botón.
        """

        parte = None
                
        if roja:
            parte = BOTON_TEXTO['derecha_presionado']
        else: parte = BOTON_TEXTO['derecha'] 
            
        superficie.blit(
            parte,(self.tamaño_nativo[0] - parte.get_size()[0], 0))
        

    def _dibujar_texto(self, superficie):
        """ En la superficie recibida por argumento dibuja 
            el texto que tendrá el botón.
        """

        self.texto.get_rect().midleft = (
            BOTON_TEXTO['izquierda'].get_size()[0], 
            ((BOTON_TEXTO['centro'].get_size()[1] / 2))
            )
        
        superficie.blit(self.texto.get_surface(), self.texto.get_rect())    


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

    
    def update(self):
        focus = self.rect.collidepoint(pygame.mouse.get_pos())

        if focus:
            if not self.index:
                self.index = 1

        else:
            if self.index:
                self.index = 0
            
        self.image = self.boton[self.index]
    
    
    def get_rect(self):
        return self.rect