from aenum import auto
from events import Evento

class EventoEstado(Evento):
    
    VOLVER_MENU = auto()
    FINALIZAR_ESTADO = auto(), 'estado (Estado)'
    VICTORIA = auto(), 'ganador (Jugador)'
