from Tablero import Tablero
from os import system

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
        
    
    def preparar_tablero(self):
        posciones_utilizadas = []

        while self.tablero.get_barcos_disponibles():
            print("Barcos disponibles: ", self.tablero.get_barcos_disponibles())

            while True:
                accion = input(
                    "¿Desea quitar u agregar un barco, vaciar el tablero o " +
                    "ubicar aleatoriamente los barcos restantes? q|a|v|u"
                    ).strip().lower()

                system('cls')

                if accion == 'a':
                    posicion = self.ingresar_posicion()
                    if posicion in posciones_utilizadas:
                        print("Ya hay un barco en esa posicion")

                    self.tablero.agregar_barco(posicion)
                    posciones_utilizadas.append(posicion)


                elif accion == 'q':
                    if posicion in posciones_utilizadas:
                        print("Ya hay un barco en esa posicion")

                    self.tablero.quitar_barco(self.ingresar_posicion())
                    posciones_utilizadas.append(posicion)
                    
                elif accion == 'v': self.vaciar_tablero()

                elif accion == 'u': self.ubicacion_aleatoria()

                else:
                    print("La respuesta debe ser 'a' o 'q'. Vuelva a intentar")

    
    def vaciar_tablero():
        return NotImplementedError


    def ubicacion_aleatoria():
        return NotImplementedError


    def disparar():
        return NotImplementedError


    def recibir_disparo(posicion):
        return NotImplementedError
