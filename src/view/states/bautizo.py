from view.states import Estado
import pygame
from events import EventoEstado as evento_estado
from events import EventoGlobal as evento_gb
from view.tools import SpriteCajaTexto
from view.tools import SpriteBotonTexto
from view.tools import SpriteCajaEntrada


class Bautizo(Estado):
    """ Etapa donde se le asigna un nombre a cada uno de los jugadores.
    """

    def __init__(self):
        super().__init__()
        self.sprites = self._crear_sprites()


    def actualizar(self, eventos):
        for sprite in self.sprites.values():
            if sprite.update():
                if (sprite == self.sprites['in_jugador_1'] or 
                    sprite == self.sprites['in_jugador_2']):
                    
                    sprite.escribir(eventos)

                if sprite == self.sprites['bt_jugar']:
                    nombre_j1 = self.sprites['in_jugador_1'].get_texto()
                    nombre_j2 = self.sprites['in_jugador_2'].get_texto()
                    # ToDo: Validar que se hayan escrito los nombres.

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

                if sprite == self.sprites['bt_volver']:
                    volver = pygame.event.Event(
                                evento_gb.ESTADO.valor, 
                                tipo=evento_estado.VOLVER_MENU
                                )
                    
                    pygame.event.post(volver)

            sprite.draw(Estado.ventana_sur)

        Estado.ventana.actualizar()


    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """

        tx_titulo = SpriteCajaTexto('Ingrese   su   nombre', (0,0,0), 30)
        tx_jugador_1 = SpriteCajaTexto('Jugador   1', (0,0,0), 26)
        tx_jugador_2 = SpriteCajaTexto('Jugador   2', (0,0,0), 26)
        in_jugador_1 = SpriteCajaEntrada('',(5,20),(350,50),(255,255,255),(44, 44, 44))
        in_jugador_2 = SpriteCajaEntrada('',(5,20),(350,50),(255,255,255),(44, 44, 44))
        bt_jugar = SpriteBotonTexto('Jugar', 55)
        bt_volver = SpriteBotonTexto('Vover', 55)
        
        centro_x = Estado.ventana.get_center()[0]
        centro_y = Estado.ventana.get_center()[1]

        # Posiciona los sprites de forma
        # relativa al centro de la ventana.

        tx_titulo.get_rect().center = (centro_x, centro_y - centro_y* 3/4 )
        
        tx_jugador_1.get_rect().center = (centro_x - centro_x*1/2 , centro_y - centro_y*1/5)
        in_jugador_1.get_rect().center = (centro_x - centro_x*1/2 , centro_y)
        
        tx_jugador_2.get_rect().center = (centro_x + centro_x*1/2 , centro_y - centro_y*1/5)
        in_jugador_2.get_rect().center = (centro_x + centro_x*1/2 , centro_y)

        bt_jugar.get_rect().center = (centro_x + centro_x*3/4 , centro_y + centro_y*4/5)
        bt_volver.get_rect().center = (centro_x - centro_x*3/4 , centro_y + centro_y*4/5)
        

        sprites = {
            'tx_titulo' :    tx_titulo,
            'tx_jugador_1' : tx_jugador_1,
            'tx_jugador_2' : tx_jugador_2,
            'in_jugador_1' : in_jugador_1,
            'in_jugador_2' : in_jugador_2,
            'bt_jugar' :     bt_jugar,
            'bt_volver' :    bt_volver
        }

        return sprites

