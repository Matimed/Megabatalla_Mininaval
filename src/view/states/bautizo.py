from view.states import Estado

class Bautizo(Estado):
    """ Etapa donde se le asigna un nombre a cada uno de los jugadores.
    """

    def __init__(self):
        super().__init__()