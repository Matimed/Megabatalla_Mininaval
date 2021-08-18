from . import EstadoJuego
from graphics import Visual as v

class Batalla(EstadoJuego):
    """ Etapa de ejecución y conclusión de los disparos
        que termina cuando todos los barcos de un jugador se hunden.
    """

    def __init__(self):
        super().__init__()
        self.interfaz.visualizar('comienzo')


    def actualizar(self):
        atacante = self.jugadores[self.actual]
        defensor = self.jugadores[not self.actual]

        self.interfaz.visualizar(v.TURNO, atacante)
        self.interfaz.visualizar(v.MAPA, atacante)

        posicion = atacante.apuntar()
        celda = defensor.recibir_disparo(posicion)
        atacante.mapa_add(posicion, celda)
        
        self.interfaz.visualizar(v.MAPA, atacante)
        self.interfaz.visualizar(v.LIMPIAR)

        if not celda.haber_barco(): #Si no toca un barco pierde el turno.
            self.interfaz.visualizar(v.AGUA)
            self.interfaz.visualizar(v.CONTINUAR)
            self.pasar_turno()
        else:
            self.interfaz.visualizar(v.TOCADO)
            if self.comprobar_ganador(atacante): 
                self.interfaz.visualizar(v.VICTORIA, atacante)
            self.interfaz.visualizar(v.CONTINUAR)
            self.finalizar()