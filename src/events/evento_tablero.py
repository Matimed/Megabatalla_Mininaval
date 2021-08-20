from aenum import auto
from events import Evento

class EventoTablero(Evento):
    COLOCAR_BARCO = auto(), 'posicion (Posicion)'
    QUITAR_BARCO = auto(), 'posicion (Posicion)'
    VACIAR_TABLERO = auto()
    UBICAR_ALEATORIAMENTE = auto()
