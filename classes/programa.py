import classes as clss
import string as str

class Programa:
    def __init__(self, cant_filas = 10, cant_barcos = 8):
        assert cant_filas <= len(str.ascii_uppercase), "Cantidad de filas mayor a cantidad de letras"

        self.posiciones = self.generar_posiciones(cant_filas)
        self.tableros = []
        self.jugadores = []
        self.cant_barcos = cant_barcos

        #Genera los tableros:
        [self.tableros.append(clss.Tablero(self.posiciones, cant_barcos)) for i in range(2)]

        #Genera los jugadores:
        [self.jugadores.append(clss.Jugador(self.tableros[i], self)) for i in range(2)]
        self.asignar_nombres()
    

    def generar_posiciones(self, cant_filas): 
        "Dada una cantidad de filas genera una lista con esa cantidad al cuadrado de posiciones"

        posiciones = []    
        for i in range(cant_filas): 
            for x in range (cant_filas): # La cantidad de columnas (x) se define a partir de cant_filas
                posiciones.append(
                    clss.Posicion(str.ascii_uppercase[i], x + 1)) # Se usa (x + 1) porque el tablero no tiene 0
        
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
                    if barcos_hundidos == self.cant_barcos: return True

            return False


    def asignar_nombres(self):
            "Turna a los jugadores para que ingresen su nombre"

            nombres = []
            for i in range (self.jugadores):
                while True:
                    nombre = (input("Ingrese el nombre del Jugador "+ i+1)).strip()
                    if nombre: #No es null
                        if not nombre in nombres: #No se repite
                            self.jugadores[i].set_nombre(nombre)
                        else: print("No se puede colocar el mismo nombre a 2 jugadores")


    def preparar_juego(self):
        "Turna a los jugadores para que coloquen sus barcos"

        for jugador in self.jugadores:
            print(jugador.get_nombre() + "Coloca tus barcos!")
            jugador.preparar_tablero()


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

            if not celda.haber_barco(): #Si no toca un barco pierde el turno
                print("Agua")
                atacante, defensor = defensor, atacante
            else:
                print("Tocado!")
                if self.comprobar_ganador(self.jugadores[atacante]): 
                    return self.jugadores[atacante] #Devuelve al jugador ganador


    def mostrar_mapa(self, mapa):
        return NotImplementedError
    

"""Ejecutar programa:
programa = Programa()
programa.preparar_juego()
print("El jugador "+ programa.jugar().get_nombre() + " ha ganado la partida" )
"""