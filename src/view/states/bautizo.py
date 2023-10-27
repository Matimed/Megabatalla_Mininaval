import pygame
from src.view.states import Estado
from src.events import EventoEstado as evento_estado
from src.events import EventoGlobal as evento_gb
from src.view.tools import SpriteCajaTexto
from src.view.tools import SpriteBotonTexto
from src.view.tools import SpriteCajaEntrada
from src.view.referencias import SONIDO_BOTON_CLICK
from src.view.referencias import SONIDO_TECLA_PRESIONADA
from src.view.referencias import SONIDO_TECLA_RETROCESO


class Bautizo(Estado):
    """ Etapa donde se le asigna un nombre a cada uno de los jugadores.
    """

    def __init__(self):
        super().__init__()
        self.sprites = self._crear_sprites()


    def actualizar(self, eventos):
        for sprite in self.sprites.values():
            if sprite.update(eventos):
                if (sprite == self.sprites['in_jugador_1'] or 
                    sprite == self.sprites['in_jugador_2']):
                    
                    sprite.escribir(eventos)

                if sprite == self.sprites['bt_jugar']:
                    nombre_j1 = self.sprites['in_jugador_1'].get_texto()
                    nombre_j2 = self.sprites['in_jugador_2'].get_texto()

                    if self._validar_entradas(nombre_j1, nombre_j2):
                        
                        asignar_nombres = pygame.event.Event(
                                            evento_gb.ASIGNAR_NOMBRES.valor, 
                                            nombre_j1 = nombre_j1,
                                            nombre_j2 = nombre_j2
                                            )
                        
                        finalizar_estado = pygame.event.Event(
                                            evento_gb.ESTADO.valor, 
                                            tipo=evento_estado.FINALIZAR_ESTADO, 
                                            estado=Bautizo
                                            )

                        pygame.event.post(asignar_nombres)
                        pygame.event.post(finalizar_estado)

            sprite.draw(Estado.ventana_sur)

        Estado.ventana.actualizar()


    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """

        tx_titulo = SpriteCajaTexto('Ingrese su nombre', (0,0,0), 30)
        tx_jugador_1 = SpriteCajaTexto('Jugador 1', (0,0,0), 26)
        tx_jugador_2 = SpriteCajaTexto('Jugador 2', (0,0,0), 26)
        in_jugador_1 = SpriteCajaEntrada('',(5,20),(350,50),(255,255,255),(44, 44, 44),False, SONIDO_TECLA_PRESIONADA, SONIDO_TECLA_RETROCESO)
        in_jugador_2 = SpriteCajaEntrada('',(5,20),(350,50),(255,255,255),(44, 44, 44),False, SONIDO_TECLA_PRESIONADA, SONIDO_TECLA_RETROCESO)
        bt_jugar = SpriteBotonTexto('Jugar', 55, (0,0,0), SONIDO_BOTON_CLICK)
        tx_error = SpriteCajaTexto('', (209, 31, 31), 15)
        
        centro_x = Estado.ventana.get_center()[0]
        centro_y = Estado.ventana.get_center()[1]

        # Posiciona los sprites de forma
        # relativa al centro de la ventana.

        tx_titulo.get_rect().center = (centro_x, centro_y* 1/4 )
        
        tx_jugador_1.get_rect().center = ( centro_x*1/2 , centro_y*4/5)
        in_jugador_1.get_rect().center = (centro_x*1/2 , centro_y)
        
        tx_jugador_2.get_rect().center = (centro_x*3/2 , centro_y*4/5)
        in_jugador_2.get_rect().center = (centro_x*3/2 , centro_y)

        bt_jugar.get_rect().center = (centro_x*7/4 , centro_y*9/5)
        
        tx_error.get_rect().center = (centro_x, centro_y*1/2)

        sprites = {
            'tx_titulo'     : tx_titulo,
            'tx_jugador_1'  : tx_jugador_1,
            'tx_jugador_2'  : tx_jugador_2,
            'in_jugador_1'  : in_jugador_1,
            'in_jugador_2'  : in_jugador_2,
            'bt_jugar'      : bt_jugar,
            'tx_error'      : tx_error
        }

        return sprites


    def _validar_entradas(self, nombre_j1, nombre_j2):
        if not (nombre_j1 and nombre_j2):
            self.sprites['tx_error'].set_texto('Ambos jugadores deben tener nombre')
            return False

        if (nombre_j1 == nombre_j2):
            self.sprites['tx_error'].set_texto('Ambos jugadores deben tener nombre distinto')
            return False

        return True
