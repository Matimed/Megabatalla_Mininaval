import pygame
from view.states import Estado


class Menu(Estado):
    def __init__(self):
        super().__init__()
        Estado.ventana.set_fondo((255,255,255))


    def actualizar(self, eventos):
        Estado.ventana.actualizar()