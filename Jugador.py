#from Programa import Programa
from Tablero import Tablero

class Jugador:
    def __init__(self, tablero, programa):
        assert isinstance(tablero, Tablero), "El argumento tablero debe ser instacia de la clase Tablero"
        
        self.nombre = ''
        self.tablero = tablero
        self.mapa = {}
        self.programa = programa

    def set_nombre(self, nombre):
        assert type(nombre) == str, "El argumento nombre debe ser de tipo str"
        assert nombre, "El argumento nombre no puede estar vacio"

        self.nombre = nombre


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


    def disparar():
        return NotImplementedError


    def recibir_disparo(posicion):
        return NotImplementedError

    
    def vaciar_tablero():
        return NotImplementedError


    def ubicacion_aleatoria():
        return NotImplementedError

