from os import system
from src.graphics import visual
from src.entities import jugador
from . import Visual

class InterfazGrafica():
    """Representa en pantalla la información de la partida y
        permite la comunicación con los jugadores
    """

    def __init__(self):
        self.visuales_simples = { }
        self.visuales_complejos = { }
        self.visuales_personales = { }

        self._set_visuales()


    def _set_visuales(self):
        self._set_visuales_simples()
        self._set_visuales_complejos()
        self._set_visuales_personales()


    def _set_visuales_simples(self):
        """ Visuales simples son aquellos que 
            solo constan de un string.
        """

        self.visuales_simples = {
            # Configuracion
            Visual.PEDIR_ORDEN : "Digite el orden del tablero.",

            # Batalla
            Visual.COMIENZO : "Que comience el juego!",
            Visual.TOCADO : "Tocado!",
            Visual.AGUA : "Agua"      
        }


    def _set_visuales_complejos(self):
        """ Visuales complejos son aquellos constan 
            de una funcion sin argumentos.
        """

        self.visuales_complejos = {
            # General
            Visual.LIMPIAR : self._limpiar,
            Visual.CONTINUAR : self._continuar
        }


    def _set_visuales_personales(self):
        """ Visuales personales son aquellos que constan de una funcion 
            que recibe como argumento una instancia de Jugador.
        """

        self.visuales_personales = {
            # Batalla
            Visual.TURNO : self._turno,
            Visual.MAPA : self._mostrar_mapa,
            Visual.VICTORIA : self._victoria,
            # Bautizo
            Visual.PEDIR_NOMBRE : self._pedir_nombre,
            Visual.PEDIR_NOMBRE : self._pedir_nombre
        }


    def visualizar(self, visual, jugador=None):
        """ Según el Visual recibido muestra información en pantalla,
            según el caso, puede recibir tambien un jugador.
        """

        if (visual in self.visuales_simples):       print(self.visuales_simples[visual])

        elif (visual in self.visuales_complejos):   self.visuales_complejos[visual]()

        elif (visual in self.visuales_personales):  self.visuales_personales[visual](jugador)

        else: raise ValueError #Podria ser un custom error

    # General
    def _limpiar(self):
        system('cls')


    # Configuración


    # Bautizo
    def _pedir_nombre(self, jugador):
        print(f'Ingrese nombre de {jugador.get_nombre()}')


    # Colocación


    # Batalla
    def _turno(self, jugador):
        print("Es turno de " + jugador.get_nombre())

   
    def _victoria(self, jugador):
        print("El jugador " + jugador.get_nombre() + " ganó!")


    def _mostrar_mapa(self, jugador):
        mapa = jugador.get_mapa()
        print("mapa")


    def _continuar(self):
        input("Presione Enter para continuar.")
        self.limpiar()


    


    
