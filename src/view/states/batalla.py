import pygame
from events import EventoGlobal as evento_gb
from events import EventoEstado as evento_et
from view.states import Estado
from view.tablero import TableroView
from view.tools import SpriteCajaTexto
from view.tools import SpriteBotonTexto



class Batalla(Estado):
    """ Etapa de ejecución y conclusión de los disparos
        que termina cuando todos los barcos de un jugador se hunden.
    """

    def __init__(self, juego):
        super().__init__()
        self.juego = juego
        self.jugadores = self.juego.get_jugadores()
        self.modelo_tableros = self.juego.get_tableros()
        self.sprites, self.vista_tablero = self._setup_interfaz()


    def actualizar(self, eventos):
        for ev in eventos:
            if ev.type == evento_et.VICTORIA:
                print('gano:', ev.ganador)

                eventos.remove(ev)


        for sprite in self.sprites.values():
            if sprite.update(eventos):
                pass

            sprite.draw(Estado.ventana_sur)

        barcos = self.vista_tablero.update_batalla(
                    eventos,
                    self._get_pos_barcos_hundidos(),
                    self._get_pos_celdas_marcadas()
                    ) 

        self.vista_tablero.draw(Estado.ventana_sur, barcos)

        Estado.ventana.actualizar()


    def _setup_interfaz(self):
        """ Crea y ubica todos los elementos de la interfaz y
            devuelve un diccionario de los sprites y el tablero.
        """

        sprites = self._crear_sprites()
        origen,limite = self._posisionar_elementos(sprites)
        tablero = self._crear_tablero(origen, limite)
        return sprites, tablero


    def _crear_tablero(self, origen, limite):
        turno = self.get_turno()
        cant_barcos = self.modelo_tableros[turno].get_cant_barcos()
        posiciones =  self.modelo_tableros[turno].get_posiciones()


        return TableroView(cant_barcos, posiciones, origen, limite)

    
    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """


        tx_titulo = SpriteCajaTexto('Dispara a tu enemigo', (0,0,0), 28)
        tx_turno = SpriteCajaTexto('Turno', (0,0,0), 18)
        tx_jugador = SpriteCajaTexto(self.jugadores[0], (0,0,0), 18)

        tx_barcos = SpriteCajaTexto('Barcos', (0,0,0), 18)
        tx_restantes = SpriteCajaTexto('Restantes', (0,0,0), 18)
        tx_cant_barcos = SpriteCajaTexto('5', (0,0,0), 18)

        tx_error = SpriteCajaTexto('', (209, 31, 31), 15)

        sprites = {
            'tx_titulo' : tx_titulo,
            'tx_turno' : tx_turno,
            'tx_jugador' : tx_jugador,
            'tx_barcos' : tx_barcos,
            'tx_restantes' : tx_restantes,
            'tx_cant_barcos' : tx_cant_barcos,
            'tx_error' : tx_error
        }
        return sprites


    def _posisionar_elementos(self, sprites):
        """ Recorre el diccionario de sprites, los ubica y
            devuelve la posiciones de origen y limite para el
            tablero.
        """

        centro_x = Estado.ventana.get_center()[0]
        centro_y = Estado.ventana.get_center()[1]

        origen_tablero = (centro_x*7/12, centro_y * 4/10)
        limite_tablero = (centro_x*17/12, centro_y*17/10)

        centro_zona_botones_x = origen_tablero[0] / 2
        centro_zona_info_x= ((centro_x*2 - limite_tablero[0])/ 2) + limite_tablero[0]

        # Posiciona los sprites de forma relativa 
        # al centro de la ventana las zonas.

        sprites['tx_titulo'].get_rect().center = (centro_x, centro_y* 1/6 )
        
        sprites['tx_turno'].get_rect().center = (
            centro_zona_info_x , centro_y*5/8
            )
        sprites['tx_jugador'].get_rect().center = (
            sprites['tx_turno'].get_rect().centerx, 
            sprites['tx_turno'].get_rect().bottom + centro_y*1/12 
            )

        sprites['tx_barcos'].get_rect().center = (
            centro_zona_info_x , centro_y
            )
        sprites['tx_restantes'].get_rect().center = (
            sprites['tx_barcos'].get_rect().centerx, 
            sprites['tx_barcos'].get_rect().bottom + centro_y*1/12 
            )
        sprites['tx_cant_barcos'].get_rect().center = (
            sprites['tx_restantes'].get_rect().centerx, 
            sprites['tx_restantes'].get_rect().bottom + centro_y*1/12 
            )

        sprites['tx_error'].get_rect().center = (
            centro_x, centro_y*6/20
            )


        return origen_tablero, limite_tablero


    def get_turno(self):
        return self.juego.get_turno()


    def _get_pos_barcos_hundidos(self):
        turno = not self.get_turno()
        return self.modelo_tableros[turno].get_barcos_hundidos()


    def _get_pos_celdas_marcadas(self):
        turno = not self.get_turno()
        posiciones = self.modelo_tableros[turno].get_celdas_marcadas()
        posiciones = posiciones.items()

        pos_celdas_marcadas = [
            pos  for (pos, marca) in posiciones if marca == True
            ]
            
        return pos_celdas_marcadas

    
    def _get_barcos(self):
        return self.modelo_tableros[not self.get_turno()].get_barcos()