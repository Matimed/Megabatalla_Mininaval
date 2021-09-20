from view.states import *
from events import EventoGlobal as evento_gb
from events import EventoEstado as evento_estado
from view.referencias import MUSICA_MENU
from view.referencias import MUSICA_JUEGO
from pygame.mixer import music

class GestorEstados:
    """ Intermediario en la comunicación con los estados, 
        además realiza operaciones pertinentes a estos.
    """

    def __init__(self, juego):
        """ Recibe una instancia de Juego para poder comunicarse con ella.
        """

        self.juego = juego

        self.estados = {
            'menu': Menu,
            'configuracion': Configuracion,
            'bautizo': Bautizo,
            'colocacion': Colocacion,
            'batalla': Batalla
        }

        music.load(MUSICA_MENU)
        music.set_volume(0.5)
        music.play(loops = -1)

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
                        music.load(MUSICA_JUEGO)
                        music.play(loops = -1)
                        self._set_estado_actual(
                            self.estados['colocacion'],
                            self.juego.get_tableros(),
                            self.juego.get_jugadores()
                        )
                    
                    if ev.estado == self.estados['colocacion']:
                         self._set_estado_actual(self.estados['batalla'])

                    eventos.remove(ev)

        self.estado_actual.actualizar(eventos)


    def _set_estado_actual(self, estado, *args):
        """ Cambia el estado actual por otro

            Recibe:
                estado:<Estado>
                args: <Any>[*] Atributos extra dependiendo del estado.
        """

        if args:
            self.estado_actual = estado(*args)
        else:
            self.estado_actual = estado()

