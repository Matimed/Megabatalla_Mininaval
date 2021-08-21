

class Jugador:
    """ Almacena información relevante 
        relacionada con la persona que juega al juego"""


    def __init__(self):
        self.nombre = ""
        self.mapa = {}


    def set_nombre(self, nombre):
        assert type(nombre) == str, "El argumento nombre debe ser de tipo str"
        assert nombre, "El argumento nombre no puede estar vacío."

        self.nombre = nombre


    def get_nombre(self): return self.nombre

    
    def get_mapa(self): return self.mapa


    def mapa_add(self, posicion, celda):
        """ Añade una clave Posicion con una Celda como valor
            a su diccionario mapa.
            
            Recibe:
                posicion:<Posicion>
                celda:<Celda>
        """

        # Verifica que posicion no este ya en mapa.
        if not posicion in self.mapa: 
            self.mapa[posicion] = celda

