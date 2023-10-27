from src.view import GestorEstados
from src.model import Juego
from src.controller import *

class Principal:
    """ Prepara el juego para ser iniciado y lo ejecuta."""
    
    def __init__(self):
        juego = Juego()
        gestor_estados = GestorEstados(juego)
        controlador_eventos = ControladorEventos(juego, gestor_estados)
        self.controlador_tics = ControladorTics(controlador_eventos)
        self.ejecutar()


    def ejecutar(self):
        self.controlador_tics.ejecutar()
