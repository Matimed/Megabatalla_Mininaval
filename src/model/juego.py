import pygame
from events import EventoGlobal as evento_gb
from events import EventoEstado  as evento_et
from events import EventoBatalla  as evento_bt
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
            if ev.type == evento_gb.CONFIGURADO:
                Tablero.set_cant_barcos(ev.cant_barcos)
                Tablero.set_posiciones(self._generar_posiciones(ev.orden))

                # Genera los tableros:
                [self.tableros.append(Tablero()) for i in range(2)]
                
            if ev.type == evento_gb.ASIGNAR_NOMBRES:
                self.jugadores[0].set_nombre(ev.nombre_j1)
                self.jugadores[1].set_nombre(ev.nombre_j2)

            if ev.type == evento_gb.CAMBIAR_TURNO:
                self.turno = ev.nuevo_turno

            if ev.type == evento_gb.TABLERO:
                if ev.tipo == evento_tablero.COLOCAR_BARCO: 
                    self.tableros[self.turno].agregar_barco(ev.posicion)

                if ev.tipo == evento_tablero.QUITAR_BARCO:
                    self.tableros[self.turno].quitar_barco(ev.posicion)

                if ev.tipo == evento_tablero.VACIAR_TABLERO:
                    self.tableros[self.turno].vaciar_celdas()
                
                if ev.tipo == evento_tablero.UBICAR_ALEATORIAMENTE:
                    self.tableros[self.turno].ubicar_aleatoriamente()
            
            if ev.type == evento_gb.BATALLA:
                if ev.tipo == evento_bt.DISPARAR:
                    self._disparar(ev.posicion)
        
                
    def get_turno(self):
        return self.turno
                

    def get_tableros(self):
        return self.tableros


    def get_jugadores(self):
        """ Devuelve una lista con el nombre de cada jugador.
        """

        nombre_jugadores = []
        for jugador in self.jugadores:
            nombre_jugadores.append(jugador.get_nombre())
        return nombre_jugadores


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

        if not celda.haber_barco():
            agua = pygame.event.Event(
                            evento_gb.BATALLA.valor, 
                            tipo = evento_bt.AGUA
                            )
            pygame.event.post(agua)

            self.turno = not self.turno
        else:
            barco_dañado = pygame.event.Event(
                            evento_gb.BATALLA.valor, 
                            tipo= evento_bt.BARCO_DAÑADO
                            )
            pygame.event.post(barco_dañado)

            if self._comprobar_ganador(self.jugadores[self.turno]): 
                ganar = pygame.event.Event(
                            evento_gb.ESTADO.valor, 
                            tipo= evento_et.VICTORIA,
                            ganador = self.jugadores[self.turno]
                            )
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
                if barcos_hundidos == Tablero.get_cant_barcos(): return True

        return False


