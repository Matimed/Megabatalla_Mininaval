import pygame
from events import EventoEstado as evento_estado
from events import EventoGlobal as evento_gb
from view.states import Estado
from view.tools import SpriteCajaTexto
from view.tools import SpriteBotonTexto
from view.tools import SelectorNumerico
from view.referencias import SONIDO_BOTON_CLICK

class Configuracion(Estado):
    """ Etapa donde se definen las características generales de la partida
        (tales como el tamaño de los tableros).
    """

    def __init__(self):
        super().__init__()
        self.sprites = self._crear_sprites()


    def actualizar(self, eventos):
        for sprite in self.sprites.values():
            if sprite.update(eventos):
                if sprite == self.sprites['bt_continuar']:
                    if not (self.sprites['sn_orden'].get_numero()**2) < self.sprites['sn_barcos'].get_numero():
                        configurado = pygame.event.Event(
                                            evento_gb.CONFIGURADO.valor, 
                                            orden = self.sprites['sn_orden'].get_numero(), 
                                            cant_barcos = self.sprites['sn_barcos'].get_numero()
                                            )
                                            
                        pygame.event.post(configurado)


                        finalizar_estado = pygame.event.Event(
                                            evento_gb.ESTADO.valor, 
                                            tipo = evento_estado.FINALIZAR_ESTADO, 
                                            estado=Configuracion
                                            )
                                            
                        pygame.event.post(finalizar_estado)
                        
                    else:
                        self.sprites['tx_error'].set_texto('No pueden haber mas barcos que posiciones')

            sprite.draw(Estado.ventana_sur)

        Estado.ventana.actualizar()


    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """

        tx_titulo = SpriteCajaTexto('Configuracion', (0,0,0), 30)

        tx_orden = SpriteCajaTexto('Orden', (0,0,0), 26)
        sn_orden = SelectorNumerico(26, 2, (90,55), (255,255,255), (0,0,0),SONIDO_BOTON_CLICK)
        tx_barcos = SpriteCajaTexto('Barcos', (0,0,0), 26)
        sn_barcos = SelectorNumerico(99, 4, (90,55), (255,255,255), (0,0,0),SONIDO_BOTON_CLICK)
        bt_continuar = SpriteBotonTexto('Continuar', 55, (0,0,0), SONIDO_BOTON_CLICK)
        tx_error = SpriteCajaTexto('', (209, 31, 31), 15)
        centro_x = Estado.ventana.get_center()[0]
        centro_y = Estado.ventana.get_center()[1]

        # Posiciona los sprites de forma
        # relativa al centro de la ventana.

        tx_titulo.get_rect().center = (centro_x, centro_y* 1/4 )

        tx_orden.get_rect().center = (centro_x * 6/10, centro_y*13/20)
        sn_orden.get_rect().center = (centro_x* 6/10, centro_y*22/20)
        
        tx_barcos.get_rect().center = (centro_x *14/10, centro_y*13/20)
        sn_barcos.get_rect().center = (centro_x *14/10, centro_y*22/20)
        
        bt_continuar.get_rect().center = (centro_x*8/5 , centro_y*9/5)        
        tx_error.get_rect().center = (centro_x, centro_y*9/20)
        

        sprites = {
            'tx_titulo' : tx_titulo,
            'tx_orden' : tx_orden,
            'sn_orden' : sn_orden,
            'tx_barcos' : tx_barcos,
            'sn_barcos' : sn_barcos,
            'bt_continuar' : bt_continuar,
            'tx_error' : tx_error
        }

        return sprites