from events.evento_global import EventoGlobal as evento_gb
import pygame


class ControladorEventos:
    def __init__(self, juego, gestor_estados):
        self.juego = juego
        self.gestor_estados = gestor_estados


    def iterar_eventos(self):
        eventos_modelo = []
        eventos_visuales = []

        for ev in pygame.event.get():
            if ev.type == evento_gb.SALIR:
                pygame.quit()
                exit()
            
            if ev.type == evento_gb.CONFIGURADO:
                eventos_modelo.append(ev)

            if ev.type == evento_gb.TECLA_PRESIONADA:
                eventos_visuales.append(ev)
            
            if ev.type == evento_gb.ESTADO:
                eventos_visuales.append(ev)

        self.juego.actualizar(eventos_modelo)
        self.gestor_estados.actualizar(eventos_visuales)