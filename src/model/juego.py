import pygame
from events import EventoGlobal as evento
from events import EventoTablero  as evento_tablero
from model import Posicion, Tablero, Jugador
import string


class Juego:
    def __init__(self):
        self.tableros = []
        self.jugadores = []
        self.turno = 0

        # Genera los jugadores:
        [self.jugadores.append(Jugador()) for i in range(2)]
        

    def actualizar(self, eventos):
        for ev in eventos:
            if ev.type == evento.CONFIGURADO:
                Tablero.posiciones = self._generar_posiciones(ev.orden)
                Tablero.cant_barcos = ev.cant_barcos

                # Genera los tableros:
                [self.tableros.append(Tablero()) for i in range(2)]
                
            if ev.type == evento.ASIGNAR_NOMBRES:
                self.jugadores[0].set_nombre(ev.nombre_j1)
                self.jugadores[1].set_nombre(ev.nombre_j2)

            if ev.type == evento.TABLERO:
                if ev.tipo == evento_tablero.COLOCAR_BARCO: 
                    self.tableros[self.turno].agregar_barco(ev.posicion)

                if ev.tipo == evento_tablero.QUITAR_BARCO:
                    self.tableros[self.turno].quitar_barco(ev.posicion)

                if ev.tipo == evento_tablero.VACIAR_TABLERO:
                    self.tableros[self.turno].vaciar_celdas()
                
                if ev.tipo == evento_tablero.UBICAR_ALEATORIAMENTE:
                    self.tableros[self.turno].ubicar_aleatoriamente()
            
            if ev.type == evento.DISPARAR:
                self._disparar()
                


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


    def _disparar(self, posicion):
        self.tableros[not self.turno].marcar_celda(posicion)
        celda = self.tableros[not self.turno].get_celda(posicion)
        self.jugadores[self.turno].mapa_add(posicion, celda)

        if not celda.haber_barco(): self.turno = not self.turno
        else:
            if self.comprobar_ganador(self.jugadores[self.turno]): 
                ganar = pygame.Event(evento.VICTORIA.valor, ganador = self.jugadores[self.turno])
                pygame.event.post(ganar)
                

    def _comprobar_ganador(self, jugador):
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