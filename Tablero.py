import Barco, Celda, Posicion

class Tablero:
    def __init__(self, posiciones):
        """ Recibe una lista de objetos tipo Posicion a los que asignara
            una celda por cada uno"""

        assert type(posiciones) == list
        self.celdas = {}
        self.barcos = []

        for posicion in posiciones:
            self.celdas[posicion] = [Celda()]

        for i in range(8):
            self.barcos.append(Barco())

    def agregar_barco(self, posicion):
        assert isinstance(posicion, Posicion)

    def quitar_barco(self, posicion):
        assert isinstance(posicion, Posicion)

    def estado_celda(self, posicion):
        return None

    def barcos_disponibles(self):
        """Devuelve la cantidad de barcos que no estan asignados a ninguna celda"""

        return len(self.barcos)