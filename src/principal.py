from src.view import GestorEstados
from src.model import Juego
from src.controller import *

class Principal:
    """ Prepara el juego para ser iniciado y lo ejecuta."""

    def __init__(self, autoejecutar=True):
        juego = Juego()
        gestor_estados = GestorEstados(juego)
        controlador_eventos = ControladorEventos(juego, gestor_estados)
        self.controlador_tics = ControladorTics(controlador_eventos)
        if autoejecutar:
            self.ejecutar()


    def ejecutar(self):
        self.controlador_tics.ejecutar()


    async def ejecutar_async(self):
        """ Punto de entrada para la version web (pygbag)."""

        await self.controlador_tics.ejecutar_async()
