from events import Evento
import pygame

class EventoGlobal(Evento):
    SALIR = pygame.QUIT
    CLICK = pygame.MOUSEBUTTONDOWN, 'pos (x (int), y (int))', 'button (int)'
    TECLA_PRECIONADA = pygame.KEYDOWN

    CONFIGURADO = pygame.event.custom_type(), 'orden (int)', 'cant_barcos (int)'
    VOLVER_MENU = pygame.event.custom_type()
    FINALIZAR_ESTADO = pygame.event.custom_type(), 'estado (Estado)'
    ASIGNAR_NOMBRES = pygame.event.custom_type(), 'nombre_j1 (string)', 'nombre_j2 (string)'
    TABLERO = pygame.event.custom_type(), 'tipo (EventoTablero)'
    DISPARAR = pygame.event.custom_type(), 'posicion (Posicion)'
    VICTORIA = pygame.event.custom_type(), 'ganador (Jugador)'

