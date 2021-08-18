from . import Estado

class Configuracion(Estado):
    """ Etapa donde se definen las características generales de la partida
        (tales como el tamaño de los tableros).
    """

    def __init__(self):
        super().__init__()

    def actualizar(self):
            self.visuales()
            orden = input()

            if type(orden) != int and orden > 0:
                print('El orden debe ser un entero mayor que cero')

            else:
                self.finalizar()

        
    def visuales(self):
        print('Digite el orden del tablero.')


    def finalizar(self):
        self.controlador_estados().siguiente_estado()