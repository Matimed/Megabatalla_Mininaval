from view.states import *
from events import EventoGlobal as ev


class GestorEstados:
    """ Intermediario en la comunicación con los estados, 
        además realiza operaciones pertinentes a estos.
    """

    def __init__(self):
        self.estados = {
            'menu': Menu,
            'configuracion': Configuracion,
            'bautizo': Bautizo,
            'colocacion': Colocacion,
            'batalla': Batalla
        }

        self.estado_actual = self.estados['menu']()


    def actualizar(self, eventos):
        for evento in list(eventos):
            if evento.type == ev.VOLVER_MENU:
                self._set_estado_actual(self.estados['menu'])
                eventos.remove(evento) # Los estados no necesitan ese evento.

            if evento.type == ev.FINALIZAR_ESTADO:
                if evento.estado == self.estados['menu']:
                    self._set_estado_actual(self.estados['configuracion'])
                
                if evento.estado == self.estados['configuracion']:
                    self._set_estado_actual(self.estados['bautizo'])
                
                if evento.estado == self.estados['bautizo']:
                    self._set_estado_actual(self.estados['colocacion'])

                if evento.estado == self.estados['colocacion']:
                    self._set_estado_actual(self.estados['batalla'])

                eventos.remove(evento)

        self.estado_actual.actualizar(eventos)


    def _set_estado_actual(self, estado):
        """ Cambia el estado actual por otro

            Recibe:
                estado:<Estado>
        """

        self.estado_actual = estado()