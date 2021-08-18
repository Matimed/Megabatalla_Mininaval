from . import Estado


class EstadoJuego(Estado):
    jugadores = []
    def __init__(self):
        super().__init__()

        self.actual = 0 # Indice de jugador


    def pasar_turno(self):
        raise NotImplementedError