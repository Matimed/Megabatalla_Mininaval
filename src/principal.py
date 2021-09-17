#!/usr/bin/env python

class Principal:
    """ Prepara el juego para ser iniciado y lo ejecuta."""
    
    def __init__(self):
        gestor_estados = GestorEstados()
        juego = Juego()
        controlador_eventos = ControladorEventos(juego, gestor_estados)
        self.controlador_tics = ControladorTics(controlador_eventos)


    def ejecutar(self):
        self.controlador_tics.ejecutar()

    
if __name__ == '__main__':
    import pygame
    pygame.init()
    from view import GestorEstados
    from model import Juego
    from controller import *

    principal = Principal()
    principal.ejecutar()