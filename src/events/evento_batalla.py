from enum import auto
from src.events import Evento

class EventoBatalla(Evento):
    AGUA = auto()
    BARCO_DAÑADO = auto()
    DISPARAR = auto(), 'posicion (Posicion)'