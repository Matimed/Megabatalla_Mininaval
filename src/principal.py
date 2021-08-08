from . import ControladorEstados

class Principal:
    """ Inicia el juego y lo mantiene en acción."""

    def __init__(self):
        self.controlador_estados = ControladorEstados()


    def actualizar(self):
        self.controlador_estados.actualizar()


    def ejecutar(self):
        while True:
            self.actualizar()

    
if __name__ == '__main__':
    Principal().ejecutar()