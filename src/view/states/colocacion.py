import pygame
from src.events import EventoGlobal as evento_gb
from src.events import EventoTablero as evento_tablero
from src.events import EventoEstado as evento_estado
from src.view.states import Estado
from src.view.tablero import TableroView
from src.view.tools import SpriteCajaTexto
from src.view.tools import SpriteBotonTexto
from src.view.referencias import SONIDO_BOTON_CLICK

class Colocacion(Estado):
    """ Etapa donde los jugadores distribuyen sus barcos
        en posiciones determinadas de sus tableros
        que termina cuando todos los barcos de ambos jugadores
        fueron colocados de manera satisfactoria.
    """

    def __init__(self, tableros, jugadores):
        """ Recibe la referencia del tablero del modelo 
            para poder comunicarse con él."""

        super().__init__()
        self.turno = 0
        self.jugadores = jugadores
        self.modelo_tableros = tableros
        self.sprites, self.vista_tablero = self._setup_interfaz()


    def actualizar(self, eventos):
        for ev in eventos:
            if ev.type == evento_gb.CAMBIAR_TURNO:
                self.turno = ev.nuevo_turno
                self.sprites['tx_jugador'].set_texto(
                    self.jugadores[self.turno])

                eventos.remove(ev)
            

        
        self.sprites['tx_cant_barcos'].set_texto(
            str(self._get_barcos_disponibles()))

        for sprite in self.sprites.values():
            if sprite.update(eventos):
                if sprite == self.sprites['bt_vaciar']:
                    vaciar = pygame.event.Event(
                                evento_gb.TABLERO.valor, 
                                tipo=evento_tablero.VACIAR_TABLERO
                                )
                                        
                    pygame.event.post(vaciar)
                
                if sprite == self.sprites['bt_automatico']:
                    ubicar_aleatorio = pygame.event.Event(
                                        evento_gb.TABLERO.valor, 
                                        tipo=evento_tablero.UBICAR_ALEATORIAMENTE
                                        )

                    pygame.event.post(ubicar_aleatorio)
                
                if sprite == self.sprites['bt_continuar']:
                    if not self._get_barcos_disponibles():
                        if self.turno == 0:
                            cambiar_turno = pygame.event.Event(
                                evento_gb.CAMBIAR_TURNO.valor, 
                                nuevo_turno=not self.turno
                                )                                
                            pygame.event.post(cambiar_turno)
                            self.sprites['tx_error'].set_texto('')

                        else:
                            finalizar_estado = pygame.event.Event(
                                                evento_gb.ESTADO.valor, 
                                                tipo=evento_estado.FINALIZAR_ESTADO, 
                                                estado=Colocacion
                                                )
                                        
                            pygame.event.post(finalizar_estado)
                    else:
                        self.sprites['tx_error'].set_texto('Debe posicionar todos sus barcos para continuar')
            
            sprite.draw(Estado.ventana_sur)



        barcos = self.vista_tablero.update_colocacion(
                    eventos,
                    self._get_pos_barcos(),
                    bool(self._get_barcos_disponibles())
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
        cant_barcos = self.modelo_tableros[self.turno].get_cant_barcos()
        posiciones =  self.modelo_tableros[self.turno].get_posiciones()


        return TableroView(cant_barcos, posiciones, origen, limite)

    
    def _crear_sprites(self):
        """ Crea y ubica todos las instancias de Sprite
            y devuelve un diccinario que los contiene.
        """


        tx_titulo = SpriteCajaTexto('Coloca tus barcos', (0,0,0), 28)
        tx_turno = SpriteCajaTexto('Turno', (0,0,0), 18)
        tx_jugador = SpriteCajaTexto(self.jugadores[0], (0,0,0), 18)

        tx_barcos = SpriteCajaTexto('Barcos', (0,0,0), 18)
        tx_restantes = SpriteCajaTexto('Restantes', (0,0,0), 18)
        tx_cant_barcos = SpriteCajaTexto('5', (0,0,0), 18)


        bt_vaciar = SpriteBotonTexto('Vaciar', 40, (0,0,0), SONIDO_BOTON_CLICK)
        bt_automatico = SpriteBotonTexto('Automatico', 40, (0,0,0), SONIDO_BOTON_CLICK)
        bt_continuar = SpriteBotonTexto('Continuar', 50, (0,0,0), SONIDO_BOTON_CLICK)

        tx_error = SpriteCajaTexto('', (209, 31, 31), 15)

        sprites = {
            'tx_titulo' : tx_titulo,
            'tx_turno' : tx_turno,
            'tx_jugador' : tx_jugador,
            'tx_barcos' : tx_barcos,
            'tx_restantes' : tx_restantes,
            'tx_cant_barcos' : tx_cant_barcos,
            'bt_vaciar' : bt_vaciar,
            'bt_automatico' : bt_automatico,
            'bt_continuar' : bt_continuar,
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

        sprites['bt_vaciar'].get_rect().center = (
            centro_zona_botones_x, centro_y*6/8
            )
        sprites['bt_automatico'].get_rect().center = (
            centro_zona_botones_x,  centro_y*7/6
            )
        sprites['bt_continuar'].get_rect().center = (
            centro_zona_info_x, centro_y * 22/12
            )

        sprites['tx_error'].get_rect().center = (
            centro_x, centro_y*6/20
            )


        return origen_tablero, limite_tablero


    def _get_pos_barcos(self):
        posiciones = self.modelo_tableros[self.turno].get_estado_celdas()
        posiciones = posiciones.items()
        pos_barcos = [pos  for (pos, barco) in posiciones if barco == True]
        return pos_barcos


    def _get_barcos_disponibles(self):
        return self.modelo_tableros[self.turno].count_barcos_disponibles()
