from view.states import *
from events import EventoGlobal as evento_gb
from events import EventoEstado as evento_estado


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
        for ev in list(eventos):
            if ev.type == evento_gb.ESTADO:

                if ev.tipo == evento_estado.VOLVER_MENU:
                    self._set_estado_actual(self.estados['menu'])
                    # Lo remueve porque los estados no necesitan ese evento.
                    eventos.remove(ev) 

                if ev.tipo == evento_estado.FINALIZAR_ESTADO:
                    if ev.estado == self.estados['menu']:
                        self._set_estado_actual(self.estados['configuracion'])
                    
                    if ev.estado == self.estados['configuracion']:
                        self._set_estado_actual(self.estados['bautizo'])
                    
                    if ev.estado == self.estados['bautizo']:
                        self._set_estado_actual(self.estados['colocacion'])

                    if ev.estado == self.estados['colocacion']:
                        self._set_estado_actual(self.estados['batalla'])

                    eventos.remove(ev)

        self.estado_actual.actualizar(eventos)


    def _set_estado_actual(self, estado):
        """ Cambia el estado actual por otro

            Recibe:
                estado:<Estado>
        """

        self.estado_actual = estado()

