from view.states import Estado

class Configuracion(Estado):
    """ Etapa donde se definen las características generales de la partida
        (tales como el tamaño de los tableros).
    """

    def __init__(self):
        super().__init__()