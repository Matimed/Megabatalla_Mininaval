from events import EventosGenerales


class ControladorEventos:
    def __init__(self, juego, gestor_estados):
        self.juego = juego
        self.gestor_estados = gestor_estados


    def iterar_eventos(self):
        eventos_modelo = []
        eventos_visuales = []

        # Event loop

        self.juego.actualizar(eventos_modelo)
        self.gestor_estados.actualizar(eventos_visuales)