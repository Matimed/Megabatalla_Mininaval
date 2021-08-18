from vista import Ventana, GestorEstados
from modelo import Juego
from controlador import *


class Principal:
    """ Prepara el juego para ser iniciado y lo ejecuta."""
    
    def __init__(self):
        ventana = Ventana()
        gestor_estados = GestorEstados(ventana)
        juego = Juego()
        controlador_eventos = ControladorEventos(ventana, gestor_estados, juego)
        self.controlador_tics = ControladorTics(controlador_eventos)


    def ejecutar(self):
        self.controlador_tics.ejecutar()

    
if __name__ == '__main__':
    principal = Principal()
    principal.ejecutar()