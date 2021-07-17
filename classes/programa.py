from tablero import *
from jugador import *
from posicion import * 
import string
from os import system

class Programa:
    def __init__(self, orden = 10, cant_barcos = 8):
        assert orden <= len(string.ascii_uppercase), "Cantidad de filas mayor a cantidad de letras"

        self.posiciones = self.generar_posiciones(orden)
        self.tableros = []
        self.jugadores = []

        #Genera los tableros:
        [self.tableros.append(Tablero(self.posiciones, cant_barcos)) for i in range(2)]
        Tablero.cant_barcos = cant_barcos
        Tablero.orden = orden

        #Genera los jugadores:
        [self.jugadores.append(Jugador(self.tableros[i], self)) for i in range(2)]
        self.asignar_nombres()
    

    def generar_posiciones(self, orden): 
        "Dada una cantidad de filas genera una lista con esa cantidad al cuadrado de posiciones"

        posiciones = []    
        for i in range(orden): 
            for x in range (orden): # La cantidad de columnas es la misma que de filas
                posiciones.append(
                    Posicion(string.ascii_uppercase[i], x + 1)) # Se usa (x + 1) porque el tablero no tiene 0
        
        return posiciones
                

    def validar_posicion(self, y, x):
        return (y, x) in self.posiciones


    def traducir_posicion(self, y, x):
        return self.posiciones[self.posiciones.index((y, x))]


    def comprobar_ganador(self, jugador):
            "Dado un jugador, devuelve True si este hundio todos los barcos del rival"
            
            barcos_hundidos = 0
            celdas = list(jugador.get_mapa().values())

            for celda in celdas:
                if (celda.haber_barco()):
                    barcos_hundidos += 1
                    if barcos_hundidos == Tablero.cant_barcos: return True

            return False


    def asignar_nombres(self):
            "Turna a los jugadores para que ingresen su nombre"

            nombres = []
            for i in range(len(self.jugadores)):
                while True:
                    nombre = (input("Ingrese el nombre del Jugador "+ str(i + 1) + ": ")).strip()

                    if nombre and not nombre in nombres: #No es null y no se repite 
                        self.jugadores[i].set_nombre(nombre)
                        break

                    else: print("No se puede colocar el mismo nombre a 2 jugadores")

            system('cls')


    def preparar_juego(self):
        "Turna a los jugadores para que coloquen sus barcos"

        for jugador in self.jugadores:
            system('cls')
            print(jugador.get_nombre() + " coloca tus barcos!")

            while True: # Hasta que el jugador decida terminar su turno
                if jugador.accion_preparar_tablero() == 0: # Si se le acaban los barcos
                    resp = input("Desea terminar su turno (S/N)").strip().lower()
                    if resp == 's': break
                system('cls')

    def jugar(self):
        """ Turna a los jugadores para que se disparen entre si
            hasta que alguno hunda todos los barcos del rival
            y devuelve al ganador."""

        print("Que comience el juego!")

        # 0 y 1 son las posiciones de los jugadores en la lista de jugadores
        atacante = 0 
        defensor = 1

        while True: #Hasta que el juego termine

            print("Es turno de " + self.jugadores[atacante].get_nombre())
            
            self.mostrar_mapa(self.jugadores[atacante].get_mapa())
            posicion = self.jugadores[atacante].apuntar()
            celda = self.jugadores[defensor].recibir_disparo(posicion)
            self.jugadores[atacante].mapa_add(posicion, celda)
            self.mostrar_mapa(self.jugadores[atacante].get_mapa())
            system('cls')

            if not celda.haber_barco(): #Si no toca un barco pierde el turno
                print("Agua")
                atacante, defensor = defensor, atacante
            else:
                print("Tocado!")
                if self.comprobar_ganador(self.jugadores[atacante]): 
                    return self.jugadores[atacante] #Devuelve al jugador ganador


    def mostrar_mapa(self, mapa):
        return NotImplementedError()     


#Ejecutar programa:
"""programa = Programa(4, 4)
programa.preparar_juego()
print("El jugador "+ programa.jugar().get_nombre() + " ha ganado la partida" )"""
