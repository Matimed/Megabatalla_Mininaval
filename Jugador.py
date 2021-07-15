from Programa import Programa
from Tablero import Tablero

class Jugador:
    def __init__(self, tablero, programa):
        assert isinstance(tablero, Tablero), "El argumento tablero debe ser instacia de la clase Tablero"
        assert isinstance(programa, Programa), "El argumento programa debe ser instacia de la clase Programa"

        self.tablero = tablero
        self.programa = programa
        self.nombre = None
        self.mapa = {}


    def set_nombre(self, nombre):
        assert type(nombre) == str, "El argumento nombre debe ser de tipo str"
        assert nombre, "El argumento nombre no puede estar vacio"

        self.nombre = nombre


    def get_nombre(self): return self.nombre

    
    def get_mapa(self): return self.mapa


    def ingresar_posicion(self):
        "De acuerdo a la entrada del usuario devuelve una instancia de Posicion"

        while True:
            y = input("Ingrese la fila: ").strip().upper()
            x = int(input("Ingrese la columna: ").strip())

            if self.programa.validar_posicion(y, x): break

            print("Esa posicion no existe, vuelva a intentar")
        
        return self.programa.traducir_posicion(y, x)
        
    
    def preparar_tablero():
        return NotImplementedError

    
    def vaciar_tablero():
        return NotImplementedError


    def ubicacion_aleatoria():
        return NotImplementedError


    def apuntar(self):
        """ Le pide ingresar una ubicacion al jugador
            hasta que ponga una posicion correcta 
            a la que no le haya disparado antes.
        """

        while True:
            posicion = self.ingresar_posicion()
            if not self.mapa[posicion]:
                return posicion
            print("No esta permitido dispararle dos veces a la misma celda")


    def mapa_add(self, posicion, celda):
        if not self.mapa[posicion]: self.mapa[posicion] = celda


    def recibir_disparo(self, posicion):
        celda = self.tablero.get_celda(posicion)
        celda.marcar()
        return celda
