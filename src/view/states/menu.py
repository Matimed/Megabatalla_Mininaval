import pygame
from events import EventosGenerales as e
from view.states import Estado
from view.states.colocacion import Colocacion


class Menu(Estado):
    def __init__(self):
        super().__init__()
        

    def actualizar(self, eventos):
        raise NotImplementedError