from . import EstadoJuego

class Bautizo(EstadoJuego):
    """ Etapa donde se le asigna un nombre a cada uno de los jugadores.
    """

    def __init__(self):
        super().__init__()
