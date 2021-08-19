from custom_errors import CellFullError, CellEmptyError

class Celda:
    def __init__(self):
        self.marca = False
        self.barco = None

    def marcar(self):
        """Cambia el atributo marca a True y si tiene un barco lo hunde."""

        assert self.marca != True, "No se puede marcar múltiples veces una misma celda."

        self.marca = True
        if (self.haber_barco()):
            self.barco.hundir()

    def get_marca(self):
        return self.marca

    def haber_barco(self):
        """Devuelve True si hay un barco en la celda."""

        return self.barco != None

    def agregar_barco(self, barco):
        """Recibe una instancia de Barco y la guarda en el atributo homónimo."""

        if not self.barco:
            self.barco = barco

        else: raise CellFullError()
            

    def quitar_barco(self):
        """Borra el objeto Barco de su atributo homónimo para devolverlo."""

        if self.barco:
            barco, self.barco = self.barco, None
            return barco

        else: raise CellEmptyError()