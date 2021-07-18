from custom_errors.cell_full_error import CellFullError
from custom_errors.cell_empty_error import CellEmptyError
from custom_errors.not_enought_boats_error import NotEnoughtBoatsError
from os import system


class Jugador:
    def __init__(self, tablero, programa):
        self.tablero = tablero
        self.programa = programa
        self.nombre = None
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
            que le queden disponibles.
        """

        while True:
            print("Barcos disponibles: ", self.tablero.count_barcos_disponibles())
            
            accion = input(
                "¿Desea quitar u agregar un barco, vaciar el tablero o"
                + " ubicar aleatoriamente los barcos restantes? q|a|v|u"
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

        return self.tablero.count_barcos_disponibles()

    

    def agregar_barco(self):
        """ Pide al jugador que ingrese una posición y 
            llama al método de tablero agregar_barco con dicha posición.
        """

        while True:
            posicion = self.ingresar_posicion()

            try:
                self.tablero.agregar_barco(posicion)

            except (NotEnoughtBoatsError or CellFullError) as err:
                print("{0} Inténtelo nuevamente".format(err))

            except: print("Por favor inténtelo nuevamente")
            else: break


    def quitar_barco(self):
        """ Pide al jugador que ingrese una posición y 
            llama al metodo de método quitar_barco con dicha posición.
        """

        while True:
            posicion = self.ingresar_posicion()

            try:
                self.tablero.quitar_barco(posicion)
                
            except (CellEmptyError) as err:
                print("{0} Intentelo nuevamente".format(err))

            except: print("Por favor intentelo nuevamente")
            
            else: break


    def apuntar(self):
        """ Le pide ingresar una ubicación al jugador
            hasta que escriba una posición correcta 
            a la que no se le haya disparado antes.
        """

        while True:
            posicion = self.ingresar_posicion()
            if not posicion in self.mapa: 
                return posicion
            print("No está permitido dispararle dos veces a la misma celda")


    def mapa_add(self, posicion, celda):
        """ Añade una clave Posicion con una Celda como valor
            al diccionario mapa.
            
            Recibe:
                posicion:<Posicion>
                celda:<Celda>
        """

        # Verifica que la posicion pasada por parametro no este ya en mapa.
        if not posicion in self.mapa: self.mapa[posicion] = celda


    def recibir_disparo(self, posicion):
        """ Marca una Celda y devuelve la misma.

            Recibe:
                posicion:<Posicion>
        """

        celda = self.tablero.get_celda(posicion)
        celda.marcar()
        return celda

