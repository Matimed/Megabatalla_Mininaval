class Posicion:
    """ Coordenadas
        
    """

    def __init__(self, y, x):
        self.verificar_formato(x, y)

        self.x = x
        self.y = y.upper()

    def get_posicion(self):
        return self.y, self.x

    def __eq__(self, other):
        assert (isinstance(other, Posicion) or type(other) == tuple), "No es posible comparar una Posicion con otro objeto"
        assert len(other) == 2, "La tupla pasada por parametro debe constar de dos elementos"
        self.verificar_formato(other[0], other[1])
        
        if isinstance(other, Posicion):
            return other.get_posicion() == self.get_posicion()
        elif type(other) == tuple:
            return (other[0], other[1].upper()) == self.get_posicion()

    def verificar_formato(self, x, y):
        assert type(x) == int, "'x' debe ser int"
        assert type(y) == str, "'y' debe ser str"
        assert len(y) == 1, "'y' debe ser una cadena de un solo caracter"

    def __repr__(self):
        return f"({self.y}, {self.x})"


print(Posicion('a', 3) == Posicion('a', 4))