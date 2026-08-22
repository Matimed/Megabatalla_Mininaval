import sys
import pygame
from src.events import EventoGlobal as evento_gb
from src.events import EventoEstado as evento_et


# En el navegador no hay a donde salir: cerrar el juego solo deja el
# canvas congelado. Ahi "Salir" vuelve al menu principal.
EN_WEB = sys.platform == 'emscripten'


class ControladorEventos:
    def __init__(self, juego, gestor_estados):
        self.juego = juego
        self.gestor_estados = gestor_estados


    def iterar_eventos(self):
        eventos_modelo = []
        eventos_visuales = []

        for ev in pygame.event.get():
            if ev.type == evento_gb.SALIR:
                if EN_WEB:
                    volver_menu = pygame.event.Event(
                        evento_gb.ESTADO.valor,
                        tipo=evento_et.VOLVER_MENU
                    )
                    pygame.event.post(volver_menu)
                    continue

                pygame.quit()
                sys.exit()

            if ev.type == evento_gb.CONFIGURADO:
                eventos_modelo.append(ev)

            if ev.type == evento_gb.TABLERO:
                eventos_modelo.append(ev)

            if ev.type == evento_gb.TECLA_PRESIONADA:
                eventos_visuales.append(ev)
            
            if ev.type == evento_gb.ESTADO:
                eventos_visuales.append(ev)

            if ev.type == evento_gb.CAMBIAR_TURNO:
                eventos_modelo.append(ev)
                eventos_visuales.append(ev)

            if ev.type == evento_gb.ASIGNAR_NOMBRES:
                eventos_modelo.append(ev)

            if ev.type == evento_gb.CLICK:
                eventos_visuales.append(ev)
            
            if ev.type == evento_gb.BATALLA:
                eventos_visuales.append(ev)
                eventos_modelo.append(ev)


        self.juego.actualizar(eventos_modelo)
        self.gestor_estados.actualizar(eventos_visuales)