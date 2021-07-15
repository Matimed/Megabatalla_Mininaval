from custom_errors import CellFullError, CellEmptyError

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
        "Recibe una instancia de Barco y la guarda en el atributo homónimo"

        if self.barco:
            self.barco = barco

        else: raise CellFullError()
            

    def quitar_barco(self):
        """Borra el atributo barco de la celda y lo devuelve"""

        if not self.barco:
            barco, self.barco = self.barco, None
            return barco

        else: raise CellEmptyError()