from classes import tablero
from custom_errors.cell_full_error import CellFullError
from custom_errors.cell_empty_error import CellEmptyError
from custom_errors.not_enought_boatsError import NotEnoughtBoatsError
from os import system

class Jugador:
    def __init__(self, tablero, programa):

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
            try:
                y = input("Ingrese la fila: ").strip().upper()
                x = int(input("Ingrese la columna: ").strip())
            except:
                print("El formato ingresado es invalido.")
                continue

            if self.programa.validar_posicion(y, x): break

            print("Esa posicion no existe, vuelva a intentar")
        
        return self.programa.traducir_posicion(y, x)
        
    
    def preparar_tablero(self):
        while self.tablero.get_barcos_disponibles():
            print("Barcos disponibles: ", self.tablero.get_barcos_disponibles())
            
            accion = input(
                "¿Desea quitar u agregar un barco, vaciar el tablero o " +
                "ubicar aleatoriamente los barcos restantes? q|a|v|u"
                ).strip().lower()

            system('cls')

            if accion   == 'a': self.agregar_barco()

            elif accion == 'q': self.quitar_barco()
                
            elif accion == 'v': self.tablero.vaciar_celdas()

            elif accion == 'u': self.tablero.ubicacion_aleatoria()

            else: 
                print("Respuesta invalida, vuelva a intentar:")
                continue
            
            break

    

    def agregar_barco(self):
        while True:
            posicion = self.ingresar_posicion()

            try:
                self.tablero.agregar_barco(posicion)

            except (NotEnoughtBoatsError or CellFullError) as error:
                print(error + " Intentelo nuevamente")

            except: print("Por favor intentelo nuevamente")
            else: break


    def quitar_barco(self):
        while True:
            posicion = self.ingresar_posicion()

            try:
                self.tablero.quitar_barco(posicion)

            except (CellEmptyError) as error:
                print(error + " Intentelo nuevamente")

            except: print("Por favor intentelo nuevamente")
            
            else:break

    
    def vaciar_tablero(self):
        return NotImplementedError()


    def apuntar(self):
        """ Le pide ingresar una ubicacion al jugador
            hasta que ponga una posicion correcta 
            a la que no le haya disparado antes.
        """

        while True:
            posicion = self.ingresar_posicion()
            if not posicion in self.mapa: 
                return posicion
            print("No esta permitido dispararle dos veces a la misma celda")


    def mapa_add(self, posicion, celda):
        if not posicion in self.mapa: self.mapa[posicion] = celda


    def recibir_disparo(self, posicion):
        celda = self.tablero.get_celda(posicion)
        celda.marcar()
        return celda
