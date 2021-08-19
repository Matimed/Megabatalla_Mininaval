from view.states import *
from events import EventosGenerales as e


class GestorEstados:
    """ Intermediario en la comunicación con los estados, 
        además realiza operaciones pertinentes a estos.
    """

    def __init__(self):
        self.estado_inicial = MenuPrincipal # Primer estado del juego.
        self.estado_actual = self.estado_inicial()


    def actualizar(self, eventos):
        for evento in list(eventos):
            if evento.type == e.CAMBIAR_ESTADO:
                self._set_estado_actual(evento.estado)
                eventos.remove(evento) # Los estados no necesitan ese evento.
        
        self.estado_actual.actualizar(eventos)


    def _set_estado_actual(self, estado):
        """ Cambia el estado actual por otro

            Recibe:
                estado:<Estado>
        """

        self.estado_actual = estado()