import pygame


class ControladorTics:
    def __init__(self, controlador_eventos):
        self.controlador_eventos = controlador_eventos
        
        self.fps = 60
        self.reloj = pygame.time.Clock()


    def ejecutar(self):
        while True:
            self.controlador_eventos.iterar_eventos()
            self.reloj.tick(60)