import pygame
from events import EventoGlobal as evento_gb
from events import EventoTablero as evento_tablero
from events import EventoEstado as evento_estado
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
                self.actualizar_turno(ev.nuevo_turno)
        
        self.actualizar_cant_barcos()

        for sprite in self.sprites.values():
            if sprite.update():
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
                    if self.turno == 0:
                        cambiar_turno = pygame.event.Event(
                            evento_gb.CAMBIAR_TURNO.valor, 
                            nuevo_turno=not self.turno
                            )                                
                        pygame.event.post(cambiar_turno)
                    else:
                    
                        finalizar_estado = pygame.event.Event(
                                            evento_gb.ESTADO.valor, 
                                            tipo=evento_estado.FINALIZAR_ESTADO, 
                                            estado=Colocacion
                                            )
                                        
                        pygame.event.post(finalizar_estado)
            
            sprite.draw(Estado.ventana_sur)



        barcos = self.vista_tablero.update(self._get_pos_barcos()) 
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


        tx_titulo = SpriteCajaTexto('Coloca   tus   barcos', (0,0,0), 28)
        tx_turno = SpriteCajaTexto('Turno', (0,0,0), 18)
        tx_jugador = SpriteCajaTexto(self.jugadores[0], (0,0,0), 18)

        tx_barcos = SpriteCajaTexto('Barcos', (0,0,0), 18)
        tx_restantes = SpriteCajaTexto('Restantes', (0,0,0), 18)
        tx_cant_barcos = SpriteCajaTexto('5', (0,0,0), 18)


        bt_vaciar = SpriteBotonTexto('Vaciar', 40)
        bt_automatico = SpriteBotonTexto('Automatico', 40)
        bt_continuar = SpriteBotonTexto('Continuar', 50)

        sprites = {
            'tx_titulo' : tx_titulo,
            'tx_turno' : tx_turno,
            'tx_jugador' : tx_jugador,
            'tx_barcos' : tx_barcos,
            'tx_restantes' : tx_restantes,
            'tx_cant_barcos' : tx_cant_barcos,
            'bt_vaciar' : bt_vaciar,
            'bt_automatico' : bt_automatico,
            'bt_continuar' : bt_continuar
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


        return origen_tablero, limite_tablero


    def _get_pos_barcos(self):
        posiciones = self.modelo_tableros[self.turno].get_estado_celdas()
        posiciones = posiciones.items()
        pos_barcos = [pos  for (pos, barco) in posiciones if barco == True]
        return pos_barcos

    
    def actualizar_cant_barcos(self):
        """ Actualiza el tx_cant_barcos para que la información
            que aparece en el coincida con la del modelo.
        """

        cant_barcos = str(self.modelo_tableros[self.turno].count_barcos_disponibles())
        pos_tx = self.sprites['tx_cant_barcos'].get_rect().center 
        tx_nuevo = SpriteCajaTexto(cant_barcos, (0,0,0), 18)
        tx_nuevo.get_rect().center = pos_tx
        self.sprites['tx_cant_barcos'] = tx_nuevo
    

    def actualizar_turno(self, turno):
        """ Actualiza el tx_jugador para que la información
            que aparece en el coincida con la del modelo.
        """

        self.turno = turno
        jugador = self.jugadores[turno]
        pos_tx = self.sprites['tx_jugador'].get_rect().center 
        tx_nuevo = SpriteCajaTexto(jugador, (0,0,0), 18)
        tx_nuevo.get_rect().center = pos_tx
        self.sprites['tx_jugador'] = tx_nuevo