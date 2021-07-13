import Barco

class Celda:
    def __init__(self):
        self.marca = False
        self.barco = None

    def marcar(self):
        """Marca la celda y si tiene un barco lo hunde"""

        self.marca = True
        if (self.haber_barco()):
            self.barco.hundir()

    def get_marca(self):
        return self.marca

    def haber_barco(self):
        """"Devuelve True si hay un barco en la celda"""

        return self.barco != None

    def agregar_barco(self, barco):
        assert isinstance(barco, Barco), "Solo recibe objetos tipo Barco"
        self.barco = barco

    def quitar_barco(self):
        self.barco = None
    
