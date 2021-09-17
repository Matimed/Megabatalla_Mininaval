from functools import singledispatchmethod


class Posicion:
    """ Sistema de coordenadas que utiliza la notación 'x', 'y'
        para representar unívocamente una ubicación particular 
        en cualquier instancia de Tablero. 
    """

    def __init__(self, y, x):
        """ Recibe:
                y:<str> len = 1
                x:<int>
        """

        self._verificar_formato(y, x)

        self.x = x
        self.y = y.upper()


    def get_posicion(self):
        return self.y, self.x


    @singledispatchmethod
    def __eq__(self, other):
        """ Iguala dos instancias de Posicion utilizando 
            el método get_posicion.
        """

        # Metodo del pato para saber si other es de tipo Posicion:
        try:
            other_get_posicion = other.get_posicion
        except AttributeError:
            raise NotImplementedError()

        return self.get_posicion() == other_get_posicion()


    @__eq__.register(tuple)
    def _(self, other):
        """ Iguala una instancia de Posicion con una tupla 
            utilizando el método get_posicion de Posicion.
        """

        assert len(other) == 2, ("La tupla pasada por parámetro" 
            + " debe constar de dos elementos.")

        self._verificar_formato(other[0], other[1])

        return (other[0].upper(), other[1]) == self.get_posicion()


    def __hash__(self):
        return hash((self.y, self.x))

    def __lt__(self, other):
        """ Compara dos instancias de Posicion utilizando 
            el método get_posicion y devuelve True si la segunda
            es mayor que si misma.
        """

        # Metodo del pato para saber si other es de tipo Posicion:
        try:
            other_get_posicion = other.get_posicion
        except AttributeError:
            raise NotImplementedError()

        return self.get_posicion() < other.get_posicion()

    def __gt__(self, other):
        """ Compara dos instancias de Posicion utilizando 
            el método get_posicion y devuelve True si la segunda
            es menor que si misma.
        """

        # Metodo del pato para saber si other es de tipo Posicion:
        try:
            other_get_posicion = other.get_posicion
        except AttributeError:
            raise NotImplementedError()

        return self.get_posicion() > other.get_posicion()

    def _verificar_formato(self, y, x):
        assert type(x) == int, "'x' debe ser int."
        assert type(y) == str, "'y' debe ser str."
        assert len(y) == 1, "'y' debe constar de un solo caracter."


    def __repr__(self):
        return f"({self.y}, {self.x})"


    def convertir_tupla(self):
        return (self.y, self.x)
