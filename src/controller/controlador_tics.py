import asyncio
import pygame


class ControladorTics:
    def __init__(self, controlador_eventos):
        self.controlador_eventos = controlador_eventos

        self.fps = 60
        self.reloj = pygame.time.Clock()


    def ejecutar(self):
        while True:
            self.controlador_eventos.iterar_eventos()
            self.reloj.tick(self.fps)


    async def ejecutar_async(self):
        """ Version del bucle principal para el navegador.

            El `await` le devuelve el control al navegador en cada
            frame; sin el la pestaña se congela.
        """

        while True:
            self.controlador_eventos.iterar_eventos()
            self.reloj.tick(self.fps)
            await asyncio.sleep(0)
