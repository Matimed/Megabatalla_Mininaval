from custom_errors.cell_full_error import CellFullError
from custom_errors.cell_empty_error import CellEmptyError
from custom_errors.not_enought_boats_error import NotEnoughtBoatsError
from os import system


class Jugador:
    """ Documentación"""

    programa = None

    def __init__(self, tablero):
        self.tablero = tablero
        self.nombre = ""
        self.mapa = {}


    def set_nombre(self, nombre):
        assert type(nombre) == str, "El argumento nombre debe ser de tipo str"
        assert nombre, "El argumento nombre no puede estar vacío."

        self.nombre = nombre


    def get_nombre(self): return self.nombre

    
    def get_mapa(self): return self.mapa


    def ingresar_posicion(self):
        """ De acuerdo a la entrada del usuario 
            devuelve una instancia de Posicion.
        """

        while True:
            try:
                y = input("Ingrese la fila: ").strip().upper()
                x = int(input("Ingrese la columna: ").strip())
                if self.programa.validar_posicion(y, x): break

                print("Esa posición no existe, vuelva a intentar.")
            except:
                print("El formato ingresado es invalido.")
                continue
        
        return self.programa.traducir_posicion(y, x)
        
    
    def accion_preparar_tablero(self):
        """ Le permite al usuario realizar una acción para preparar 
            su tablero, y devuelve la cantidad de barcos 
            que le queden disponibles luego de la acción realizada.
        """

        while True: # Hasta que el jugador realice una acción valida.
            barcos_disponibles = self.tablero.count_barcos_disponibles()

            print("Barcos disponibles: ", barcos_disponibles)
            
            accion = input(
                "¿Desea quitar u agregar un barco, vaciar el tablero o"
                + " ubicar aleatoriamente los barcos restantes? q|a|v|u\n"
                ).strip().lower()

            system('cls')

            if accion   == 'a':
                if barcos_disponibles: # Verifica que hayan barcos disponibles.
                    self.agregar_barco()

                else:
                    print("No hay barcos disponibles para agregar.")
                    continue

            elif accion == 'q': self.quitar_barco()
                
            elif accion == 'v': self.tablero.vaciar_celdas()

            elif accion == 'u':
                if barcos_disponibles: # Verifica que hayan barcos disponibles.  
                    self.tablero.ubicacion_aleatoria()
                
                else:
                    print("No hay barcos disponibles para agregar.")
                    continue

            else: 
                print("Respuesta invalida, vuelva a intentar:")
                continue
            
            break

        return self.tablero.count_barcos_disponibles()

    

    def agregar_barco(self):
        """ Permite al jugador agregar un barco 
            según la posicion que el ingrese.
        """

        while True: # Hasta que se termine realizar la operación con exito.
            posicion = self.ingresar_posicion()

            try:
                self.tablero.agregar_barco(posicion)

            except (NotEnoughtBoatsError or CellFullError) as err:
                print("{0} Inténtelo nuevamente".format(err))

            except: print("Por favor inténtelo nuevamente")
            else: break


    def quitar_barco(self):
        """ Permite al jugador quitar un barco 
            según la posicion que el ingrese.
        """

        while True: # Hasta que se termine realizar la operación con exito.
            posicion = self.ingresar_posicion()

            try:
                self.tablero.quitar_barco(posicion)
                
            except (CellEmptyError) as err:
                print("{0} Intentelo nuevamente".format(err))

            except: print("Por favor intentelo nuevamente")
            
            else: break


    def apuntar(self):
        """ Se pide al jugador ingresar una posición
            a la cual no se le haya disparado antes.
        """

        while True:  # Hasta que posicion sea valida para ser disparada.
            posicion = self.ingresar_posicion()

            if not posicion in self.mapa: 
                return posicion

            print("No está permitido dispararle dos veces a la misma celda")


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


    def recibir_disparo(self, posicion):
        """ Marca una Celda y devuelve la misma.

            Recibe:
                posicion:<Posicion>
        """

        self.tablero.marcar_celda(posicion)
        return self.tablero.get_celda(posicion)