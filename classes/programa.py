from tablero import Tablero
from jugador import Jugador
from posicion import Posicion
import string
from os import system


class Programa:
    def __init__(self, orden = 10, cant_barcos = 8):
        assert orden <= len(string.ascii_uppercase), (
            "Cantidad de filas mayor a cantidad de letras")

        self.posiciones = self._generar_posiciones(orden)
        self.tableros = []
        self.jugadores = []

        Tablero.cant_barcos = cant_barcos
        # Genera los tableros:
        [self.tableros.append(Tablero(self.posiciones)) for i in range(2)]

        # Se asigna a si mismo como programa de los jugadores que genere.
        Jugador.programa = self

        # Genera los jugadores:
        [self.jugadores.append(Jugador(self.tableros[i])) for i in range(2)]
        self._asignar_nombres() # Asigna los nombres de los jugadores.
    

    def _generar_posiciones(self, orden): 
        """ Dado un orden genera una lista con ese numero 
            de filas y columnas posiciones.

            Recibe:
                orden:<int>
        """

        assert type(orden) == int, (
            "La cantidad de filas y columnas"
             + " debe determinarse a través de un valor entero")

        posiciones = []    
        for i in range(orden): 
            for x in range (orden):
                posiciones.append(
                    # Se usa (x + 1) porque el tablero no tiene 0
                    Posicion(string.ascii_uppercase[i], x + 1)) 
        
        return posiciones
                

    def validar_posicion(self, y, x):
        """ Devuelve un booleano según si una posicion
            coincide con los valores (y, x).
        """

        # La validacion de los argumentos se lleva a cabo en Posicion.
        return (y, x) in self.posiciones


    def traducir_posicion(self, y, x):
        return self.posiciones[self.posiciones.index((y, x))]


    def comprobar_ganador(self, jugador):
            """ Dado un jugador, devuelve True 
                si este hundió todos los barcos de su rival.

                Recibe:
                    jugador:<Jugador>
            """
            
            barcos_hundidos = 0
            celdas = list(jugador.get_mapa().values())

            for celda in celdas:
                if (celda.haber_barco()):
                    barcos_hundidos += 1
                    if barcos_hundidos == Tablero.cant_barcos: return True

            return False


    def _asignar_nombres(self):
        """Turna a los jugadores para que ingresen sus nombres."""

        nombres = []
        for i in range(len(self.jugadores)):
            while True: # Hasta que se ingrese un nombre valido.
                nombre = (
                    input(
                        "Ingrese el nombre del Jugador " + str(i + 1) + ": "
                         )).strip().title()
                
                # No es null y no se repite.
                if nombre and not nombre in nombres: 
                    if nombre and not nombre in nombres: 
                if nombre and not nombre in nombres: 
                    if nombre and not nombre in nombres: 
                if nombre and not nombre in nombres: 
                    self.jugadores[i].set_nombre(nombre)
                    break

                else: 
                    print("No se puede colocar el mismo nombre a 2 jugadores")

        system('cls')


    def preparar_juego(self):
        """Turna los jugadores para que coloquen sus barcos."""

        for jugador in self.jugadores:
            system('cls')
            print(jugador.get_nombre() + " coloca tus barcos!")

            
            while True: # Hasta que jugador decida terminar su turno.  

                # Si se acaban los barcos.
                if jugador.accion_preparar_tablero() == 0: 
                    resp = input("¿Desea terminar su turno?. s|n").strip().lower()
                    if resp == 's': break

                system('cls')


    def jugar(self):
        """ Turna a los jugadores para que se disparen entre si
            hasta que alguno hunda todos los barcos del rival.
            Devuelve el jugador ganador.
        """

        # 0 y 1 son las posiciones de los jugadores en la lista de jugadores.
        atacante = 0 
        defensor = 1

        print("Que comience el juego!")

        while True: #Hasta que el juego termine.

            print("Es turno de " + self.jugadores[atacante].get_nombre())
            
            self.mostrar_mapa(self.jugadores[atacante].get_mapa())
            posicion = self.jugadores[atacante].apuntar()
            celda = self.jugadores[defensor].recibir_disparo(posicion)
            self.jugadores[atacante].mapa_add(posicion, celda)
            self.mostrar_mapa(self.jugadores[atacante].get_mapa())
            system('cls')

            if not celda.haber_barco(): #Si no toca un barco pierde el turno.
                print("Agua")
                atacante, defensor = defensor, atacante
            else:
                print("Tocado!")
                if self.comprobar_ganador(self.jugadores[atacante]): 
                    #Devuelve al jugador ganador.
                    return self.jugadores[atacante] 


    def mostrar_mapa(self, mapa):
        return NotImplementedError()     


#Ejecutar programa:
"""programa = Programa(4, 4)
programa.preparar_juego()
print("El jugador "+ programa.jugar().get_nombre() + " ha ganado la partida" )"""
