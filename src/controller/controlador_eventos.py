from events import EventoGlobal
import pygame


class ControladorEventos:
    def __init__(self, juego, gestor_estados):
        self.juego = juego
        self.gestor_estados = gestor_estados


    def iterar_eventos(self):
        eventos_modelo = []
        eventos_visuales = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.juego.actualizar(eventos_modelo)
        self.gestor_estados.actualizar(eventos_visuales)