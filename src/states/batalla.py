from . import EstadoJuego

class Batalla(EstadoJuego):
    """ Etapa de ejecución y conclusión de los disparos
        que termina cuando todos los barcos de un jugador se hunden.
    """

    def __init__(self):
        super().__init__()
    