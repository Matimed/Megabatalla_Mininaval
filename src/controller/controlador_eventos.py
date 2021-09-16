from events.evento_global import EventoGlobal as ev
import pygame


class ControladorEventos:
    def __init__(self, juego, gestor_estados):
        self.juego = juego
        self.gestor_estados = gestor_estados


    def iterar_eventos(self):
        eventos_modelo = []
        eventos_visuales = []

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if evento.type == ev.TECLA_PRESIONADA:
                eventos_visuales.append(evento)

        self.juego.actualizar(eventos_modelo)
        self.gestor_estados.actualizar(eventos_visuales)