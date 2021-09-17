from view.states import Estado
from view.tablero import TableroView
from view.tools import SpriteCajaTexto
from view.tools import SpriteBotonTexto

class Colocacion(Estado):
    """ Etapa donde los jugadores distribuyen sus barcos
        en posiciones determinadas de sus tableros
        que termina cuando todos los barcos de ambos jugadores
        fueron colocados de manera satisfactoria.
    """

    def __init__(self, tableros):
        """ Recibe la referencia del tablero del modelo 
            para poder comunicarse con él."""

        super().__init__()
        self.modelo_tableros = tableros


    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """


        tx_titulo = SpriteCajaTexto('Colocacion   de   barcos', (0,0,0), 28)
        tx_turno = SpriteCajaTexto('Turno', (0,0,0), 18)
        tx_jugador = SpriteCajaTexto('Nombre', (0,0,0), 18)

        tx_barcos = SpriteCajaTexto('Barcos', (0,0,0), 18)
        tx_restantes = SpriteCajaTexto('Restantes', (0,0,0), 18)
        tx_cant_barcos = SpriteCajaTexto('5', (0,0,0), 18)


        bt_vaciar = SpriteBotonTexto('Vaciar   tablero ', 40)
        bt_ubicar = SpriteBotonTexto('Ubicar   Barcos', 40)
        bt_continuar = SpriteBotonTexto('Continuar', 50)

        sprites = {
            'tx_titulo' : tx_titulo,
            'tx_turno' : tx_turno,
            'tx_jugador' : tx_jugador,
            'tx_barcos' : tx_barcos,
            'tx_restantes' : tx_restantes,
            'tx_cant_barcos' : tx_cant_barcos,
            'bt_vaciar' : bt_vaciar,
            'bt_ubicar' : bt_ubicar,
            'bt_continuar' : bt_continuar
        }
        return sprites




    def _crear_tablero(self):
        cant_barcos = self.modelo_tableros[0].cant_barcos
        posiciones =  self.modelo_tableros[0].posiciones
         
        return TableroView(cant_barcos, posiciones, (0,0),(50,50))