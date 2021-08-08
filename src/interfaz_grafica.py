from os import system

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
        self.visuales_simples['comienzo'] = "Que comience el juego!"
        self.visuales_simples['tocado'] = "Tocado!"
        self.visuales_simples['agua'] = "Agua"
        
        self.visuales_complejos['limpiar'] = self._limpiar
        self.visuales_complejos['continuar'] = self._continuar

        self.visuales_personales['turno'] = self._turno
        self.visuales_personales['mapa'] = self._mostrar_mapa
        self.visuales_personales['victoria'] =  self._victoria


    def visualizar(self, visual, jugador=None):
        """ Según el nombre del visual recibido 
            muestra determinada información en pantalla,
            según el caso, puede recibir tambien un jugador
        """

        if (visual in self.visuales_simples):       print(self.visuales_simples[visual])

        elif (visual in self.visuales_complejos):   self.visuales_complejos[visual]()

        elif (visual in self.visuales_personales):  self.visuales_personales[visual](jugador)

        else: raise ValueError #Podria ser un custom error


    def _turno(self, jugador):
        print("Es turno de " + jugador.get_nombre())


    def _victoria(self, jugador):
        print("El jugador " + jugador.get_nombre() + " ganó!")


    def _limpiar(self):
        system('cls')


    def _mostrar_mapa(self, jugador):
        mapa = jugador.get_mapa()
        print("mapa")


    def _continuar(self):
        input("Presione Enter para continuar.")
        self.limpiar()
