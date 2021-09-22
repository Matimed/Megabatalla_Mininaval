from custom_errors import CellFullError, NotEnoughtBoatsError
from model import Celda, Barco
import random


class Tablero:
    """ Representa una matriz de celdas,
        tiene como atributos la cantidad de barcos a jugar.
    """

    cant_barcos = 8
    posiciones = []
    
    def __init__(self):
        """ Recibe una lista de objetos tipo Posicion a los que asignara
            una celda por cada uno y la cantidad de barcos que se quieren utilizar.
        """

        assert type(Tablero.posiciones) == list
        self.celdas = {}
        self.barcos_disponibles = []

        #Crea el diccionario de celdas a partir de las posiciones.
        for posicion in Tablero.get_posiciones(): 
            self.celdas[posicion] = Celda()

        #Crea la lista de barcos de la cantidad pedida.
        for i in range(Tablero.get_cant_barcos()):
            self.barcos_disponibles.append(Barco())

    # Usamos metodos estaticos para acceder 
    # a los atributos de clase de manera más limpia.

    @staticmethod
    def get_cant_barcos():       
       return Tablero.cant_barcos


    @staticmethod
    def get_posiciones():        
       return Tablero.posiciones


    @staticmethod
    def set_cant_barcos(cant_barcos):       
       Tablero.cant_barcos = cant_barcos


    @staticmethod
    def set_posiciones(posiciones):       
       Tablero.posiciones = posiciones      


    def get_celda(self, posicion):
        """ Dada una posición devuelve la celda correspondiente.
            
            Recibe:
                posicion:<Posicion>
        """

        if posicion in self.celdas:
            return self.celdas.get(posicion)
        else:
            raise ValueError("La posicion no esta en la lista")


    def marcar_celda(self, posicion):
        """ Marca la celda según su posicion.
            
            Recibe:
                posicion:<Posicion>
        """

        self.get_celda(posicion).marcar()


    def agregar_barco(self, posicion):
        """ Recibe una instancia de Posicion y agrega, si es posible, 
            un barco en la celda que corresponda con dicha Posicion.
        """

        # Verifica que hayan barcos disponibles.
        if self.count_barcos_disponibles(): 
            celda = self.get_celda(posicion)
            
            if not celda.haber_barco():
                celda.agregar_barco(self.barcos_disponibles.pop())

            else: raise CellFullError()

        else: raise NotEnoughtBoatsError()
        

    def quitar_barco(self, posicion):
        """ Recibe una instancia de Posicion y 
            quita el barco de la celda correspondiente con esta.
        """

        celda = self.get_celda(posicion)
        self.barcos_disponibles.append(celda.quitar_barco())


    def haber_barco(self, posicion):
        """ Recibe una instancia de Posicion y 
            devuelve un bool que indica si hay un barco en esa celda.
        """
        
        return self.get_celda(posicion).haber_barco()
        

    def count_barcos_disponibles(self):
        """ Devuelve un numero que representa la cantidad de barcos 
            que aún no están en una Celda.
        """

        return len(self.barcos_disponibles)
    

    def ubicar_aleatoriamente(self):
        """ Mientras hayan barcos disponibles 
            toma una Posicion aleatoria de su diccionario de celdas e 
            intenta agregar un barco en ella.
        """

        posiciones = list(self.celdas.keys())  
        while self.count_barcos_disponibles():
            
            posicion = random.choice(posiciones)

            #Si esta ocupada busca una nueva.
            if not self.haber_barco(posicion): 
                self.agregar_barco(posicion)


    def vaciar_celdas(self):
        """Remueve los barcos de todas sus celdas."""

        for posicion in self.celdas:

            if self.haber_barco(posicion):

                self.quitar_barco(posicion)

                if self.count_barcos_disponibles() == Tablero.get_cant_barcos():
                    break


    def get_estado_celdas(self):
        """ Devuelve un diccionario con todas las posiciones 
            y los estados (en cuanto a barco) de las celdas:
            
            estado_celdas<Dict>{
                key = posicion <Posicion>,
                value = celda_ocupada <bool>
            }
        """

        estado_celdas = {}
        for posicion in self.celdas: 
            celda = self.get_celda(posicion)
            estado_celdas[posicion] = celda.haber_barco()
        
        return estado_celdas


    def get_celdas_marcadas(self):
        """ Devuelve un diccionario con todas las posiciones 
            y los estados (en cuanto a marca) de las celdas:
            
            estado_celdas<Dict>{
                key = posicion <Posicion>,
                value = celda_marcada <bool>
            }
        """

        marca_celdas = {}
        for posicion in self.celdas: 
            celda = self.get_celda(posicion)
            marca_celdas[posicion] = celda.get_marca()
        
        return marca_celdas

    
    def get_barcos_hundidos(self):
        """ Devuelve una lista de posiciones de barcos hundidos."""

        pos_barcos_hundidos = []
        for posicion in self.celdas: 
            celda = self.get_celda(posicion)

            if celda.haber_barco() and celda.get_marca():
                pos_barcos_hundidos.append(posicion)
        
        return pos_barcos_hundidos
        

    def get_barcos(self):
        pos_barcos = []
        for posicion in self.celdas: 
            celda = self.get_celda(posicion)

            if celda.haber_barco():
                pos_barcos.append(posicion)
        
        return pos_barcos
        