import pygame
from view.referencias import FUENTE
from events import EventoGlobal as ev
from view.tools import SpriteCajaTexto

class SpriteCajaEntrada(pygame.sprite.Sprite):
    """ Rectángulo en el cual se puede digitar texto y acceder a este."""

    def __init__(self, texto_inicial = '', margen=(2,2), tamaño=(200,40), color_texto=(255,255,255), color_caja=(0,0,0)):
        super().__init__()

        self.caja_sur = pygame.Surface(tamaño)
        self.caja_sur.fill(color_caja)

        self.margen = margen
        self.alto_texto = tamaño[1] - margen[1]
        self.color_texto = color_texto
        self.texto = texto_inicial
        self.texto_sprite  = None
        self._generar_texto_sprite()
        
        self.rect = self.caja_sur.get_rect()

        self.precionado = False
    

    def get_rect(self):
        return self.rect


    def _verificar_largo_texto(self, texto_sprite):
        """ Verifica que la longitud de la superficie de un texto sea 
            adecuada para la superfice del fondo rectangular.
        """

        return texto_sprite.get_tamaño()[0] > self.caja_sur.get_size()[0] - self.margen[0]


    def _generar_texto_sprite(self):
        """ Genera una instancia de SpriteCajaTexto según
            el texto en su atributo homonimo.
        """

        texto_sprite = SpriteCajaTexto(self.texto, self.color_texto, self.alto_texto)

        if  not self._verificar_largo_texto(texto_sprite):
            self.texto_sprite = texto_sprite

        else:
            self.texto = self.texto[:-1]
