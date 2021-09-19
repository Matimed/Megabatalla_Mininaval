from events import Evento
import pygame

class EventoGlobal(Evento):
    SALIR = pygame.QUIT
    CLICK = pygame.MOUSEBUTTONUP, 'pos (x (int), y (int))', 'button (int)'
    TECLA_PRESIONADA = pygame.KEYDOWN

    ESTADO = pygame.event.custom_type(), 'tipo (EventoEstado)', '*args'
    TABLERO = pygame.event.custom_type(), 'tipo (EventoTablero)', '*args'
    
    CONFIGURADO = pygame.event.custom_type(), 'orden (int)', 'cant_barcos (int)'
    ASIGNAR_NOMBRES = pygame.event.custom_type(), 'nombre_j1 (string)', 'nombre_j2 (string)'
    DISPARAR = pygame.event.custom_type(), 'posicion (Posicion)'

    CAMBIAR_TURNO = pygame.event.custom_type(), 'nuevo_turno (int)'
