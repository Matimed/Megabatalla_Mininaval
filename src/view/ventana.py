import pygame


class Ventana:
    """ Implementa todo lo que concierne a la clase display de pygame
        mas un fondo.
    """

    def __init__(self):
        pygame.display.set_caption('Batalla naval')
        
        self.escala = 3 # Escala por defecto.

        # Resolución minima y por defecto.
        self.resolucion_nativa = (480, 270)

        # Resolución actual.
        self.resolucion = self.get_resolucion(self.escala)

        self.ventana_sur = pygame.display.set_mode(self.resolucion)

        self.resolucion_maxima = (
            pygame.display.Info().current_w,
            pygame.display.Info().current_h
        ) # Obtiene la resolucion de la pantalla.

        self.fondo
        self.set_fondo((0,0,0))


    def get_surface(self):
        """ Obtiene la superficie del display."""
        return self.ventana_sur

        
    def actualizar(self):
        """ Actualiza el diplay y dibuja el fondo."""

        pygame.display.update()
        self.ventana_sur.blit(self.fondo, (0,0))


    def get_resolucion(self, escala):
        """ Recibe:
                escala:<int>

            Devuelve:
                resolucion:<tuple> resolución nativa escalada.
        """

        resolucion = [
            self.resolucion_nativa[0] * escala, 
            self.resolucion_nativa[1] * escala
            ]
        
        return resolucion


    def ajustar_resolucion(self, escala, flags = 0):
        """ Cambia el tamaño del display a otra escala.
            
            Recibe:
                escala:<int> nueva escala
                flags:<int> enum de pygame.
        """

        assert (
            self.get_resolucion(escala)[0] > self.resolucion_maxima[0]
            or self.get_resolucion(escala)[1] > self.resolucion_maxima[1]), (
            'La resolucion que se obtiene de la escala es demasiado grande.'
        )
        assert escala >= 1,(
            'La resolucion que se obtiene de la escala es demasiado pequeña.'
            )

        self.escala = escala
        self.resolucion = self.get_resolucion(escala)

        self.ventana_sur = pygame.display.set_mode(self.resolucion, flags)

        self._resetear_fondo() # El fondo debe adaptarse a la resolución actual.

    
    def set_fondo(self, color=(0,0,0)):
        """ Crea una superficie del tamaño del diplay
            y la colorea según su argumento.
            
            Recibe:
                color:<tuple>
        """

        fondo_sur = pygame.Surface(self.resolucion)
        fondo_sur.fill(color)
        
        self.fondo = fondo_sur


    def _resetear_fondo(self):
        """ Escala el fondo según la resolución del display."""

        self.fondo = pygame.transform.scale(self.fondo, (self.resolucion))