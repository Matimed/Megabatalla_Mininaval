"""Punto de entrada para la version web (pygbag / WebAssembly).

pygbag exige que el archivo se llame main.py, este en la raiz del
proyecto y exponga una corrutina que se lance con asyncio.run().

Para la version de escritorio seguir usando MegabatallaMininaval.py
"""

import asyncio
import pygame

pygame.init()

from src.principal import Principal


async def main():
    # autoejecutar=False para que el constructor no arranque el
    # bucle bloqueante: en el navegador el bucle debe ser asincronico.
    principal = Principal(autoejecutar=False)
    await principal.ejecutar_async()


asyncio.run(main())
