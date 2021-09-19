import pygame
from view.referencias import FUENTE
from events import EventoGlobal as ev
from view.tools import SpriteCajaTexto

class SpriteCajaEntrada(pygame.sprite.Sprite):
    """ Rectángulo en el cual se puede digitar texto y acceder a este."""

    def __init__(self, texto_inicial = '', margen=(5,20), tamaño=(350,50), color_texto=(255,255,255), color_caja=(0,0,0), solo_lectura=False):
        super().__init__()
        self.solo_lectura = solo_lectura

        self.caja_sur = pygame.Surface(tamaño)
        self.caja_sur.fill(color_caja)

        self.margen = margen
        self.alto_texto = tamaño[1] - margen[1]
        self.color_texto = color_texto
        self.texto_sprite  = SpriteCajaTexto('', self.color_texto, self.alto_texto)
        self.set_texto(texto_inicial)
        
        self.rect = self.caja_sur.get_rect()

        self._presionado = False


    def update(self):
        focus = self.rect.collidepoint(pygame.mouse.get_pos())

        if focus:
            if pygame.mouse.get_pressed()[0] and not self._presionado:
                self._presionado = True
        else:
            if pygame.mouse.get_pressed()[0] and self._presionado: 
                self._presionado = False

        return self._presionado


    def escribir(self, eventos):
        if not self.solo_lectura:
            for evento in eventos:
                if evento.type == ev.TECLA_PRESIONADA:
                    texto = self.get_texto()
                    if evento.key == pygame.K_BACKSPACE:
                        self.set_texto(texto[:-1])
                    elif evento.key == pygame.K_SPACE:
                        continue
                    else:
                        texto += evento.unicode
                        self.set_texto(texto)


    def draw(self, surface):
        """ Recibe una superficie y dibuja  la superficie de la caja y del texto en ella."""

        surface.blit(self.caja_sur, self.rect)
        
        self.texto_sprite.get_rect().center = self.get_rect().center

        surface.blit(self.texto_sprite.get_surface(), self.texto_sprite.get_rect())


    def set_texto(self, texto):
        self.texto_sprite.set_texto(texto)

        if  not self._verificar_largo_texto(self.texto_sprite):
            self.set_texto(texto[:-1])


    def get_texto(self):
        return self.texto_sprite.get_texto()


    def get_rect(self):
        return self.rect


    def _verificar_largo_texto(self, texto_sprite):
        """ Verifica que la longitud de la superficie de un texto sea 
            adecuada para la superfice del fondo rectangular.
        """

        return texto_sprite.get_tamaño()[0] < self.caja_sur.get_size()[0] - self.margen[0]



