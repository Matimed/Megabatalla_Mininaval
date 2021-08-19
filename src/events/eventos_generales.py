from enum import IntEnum
from pygame import event
import pygame
from pygame.constants import QUIT

class EventosGenerales(IntEnum):
    
    SALIR = pygame.QUIT
    CONFIGURADO = pygame.event.custom_type() # orden (int), cant_barcos (int)
    CAMBIAR_ESTADO = pygame.event.custom_type() # estado (Estado)