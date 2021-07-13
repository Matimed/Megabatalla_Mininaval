class Posicion:
    """ Coordenadas
        
    """
    def __init__(self, x, y):
        self.verificar_formato(x, y)

        self.x = x
        self.y = y.upper()

    def get_posicion(self):
        return self.x, self.y

    def __eq__(self, other):
        assert type(other) == tuple, "no es posible comparar una Posicion con otro objeto"
        assert len(other) == 2, "la tupla pasada por parametro debe constar de dos elementos"
        self.verificar_formato(other[0], other[1])

        return (other[0], other[1].upper()) == self.get_posicion()

    def verificar_formato(self, x, y):
        assert type(x) == int, "type(x) debe ser int"
        assert type(y) == str, "type(y) debe ser str"
        assert len(y) == 1, "y debe ser una cadena de un solo caracter"

posiciones = [Posicion(1, 12), Posicion(1, 'c'), Posicion(1, 'd'), Posicion(1, 'e')]

hola = (1, 'g')

print(Posicion(1, 'g') == (1, 'g'))
print(hola in posiciones)

print(posiciones[1].get_posicion())