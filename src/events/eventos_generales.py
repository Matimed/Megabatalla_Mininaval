from enum import Enum
from pygame import event
import pygame
from pygame.constants import QUIT

class EventosGenerales(Enum):
    
    SALIR = pygame.QUIT
    CONFIGURADO = pygame.event.custom_type() # orden (int), cant_barcos (int)
    


