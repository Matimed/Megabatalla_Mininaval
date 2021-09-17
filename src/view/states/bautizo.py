from view.states import Estado
from view.tools import SpriteCajaTexto
from view.tools import SpriteBotonTexto
from view.tools import SpriteCajaEntrada


class Bautizo(Estado):
    """ Etapa donde se le asigna un nombre a cada uno de los jugadores.
    """

    def __init__(self):
        super().__init__()
        self.sprites = self._crear_sprites()


    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """

        tx_titulo = SpriteCajaTexto('Ingrese   su   nombre', (0,0,0), 30)
        tx_jugador_1 = SpriteCajaTexto('Jugador   1', (0,0,0), 26)
        tx_jugador_2 = SpriteCajaTexto('Jugador   2', (0,0,0), 26)
        in_jugador_1 = SpriteCajaEntrada()
        in_jugador_2 = SpriteCajaEntrada()
        bt_jugar = SpriteBotonTexto('Jugar', 55)
        bt_volver = SpriteBotonTexto('Vover', 55)
        
        centro_x = Estado.ventana.get_center()[0]
        centro_y = Estado.ventana.get_center()[1]

        # Posiciona los sprites de forma
        # relativa al tamaño de la ventana.

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

