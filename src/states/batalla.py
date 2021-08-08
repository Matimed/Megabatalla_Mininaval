from . import EstadoJuego

class Batalla(EstadoJuego):
    """ Etapa de ejecución y conclusión de los disparos
        que termina cuando todos los barcos de un jugador se hunden.
    """

    def __init__(self):
        super().__init__()


    def actualizar(self):
        atacante = self.jugadores[self.actual]
        defensor = self.jugadores[not self.actual]

        self.interfaz.visualizar('turno')
        self.interfaz.visualizar('mapa')

        posicion = atacante.apuntar()
        celda = defensor.recibir_disparo(posicion)
        atacante.mapa_add(posicion, celda)
        
        self.interfaz.visualizar('mapa')
        self.interfaz.visualizar('limpiar')

        if not celda.haber_barco(): #Si no toca un barco pierde el turno.
            self.interfaz.visualizar('agua')
            self.pasar_turno()
        else:
            self.interfaz.visualizar('tocado')
            if self.comprobar_ganador(self.jugadores[atacante]): 
                self.interfaz.visualizar('victoria')
            self.interfaz.visualizar('continuar')
            self.finalizar()