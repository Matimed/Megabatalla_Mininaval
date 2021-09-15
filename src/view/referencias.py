#!/usr/bin/env python

import pygame


FUENTE = pygame.font.Font('resources/fonts/Fuente.ttf', 8)

BOTON_TEXTO = {
    'izquierda':pygame.image.load('resources/graphics/boton_texto/boton_izquierda.png').convert_alpha(),
    'centro':pygame.image.load('resources/graphics/boton_texto/boton_centro.png').convert_alpha(),
    'derecha':pygame.image.load('resources/graphics/boton_texto/boton_derecha_liberado.png').convert_alpha(),
    'derecha_presionado':pygame.image.load('resources/graphics/boton_texto/boton_derecha_presionado.png').convert_alpha()
}

BOTON_FLECHA = {
    'liberado':pygame.image.load('resources/graphics/boton_flecha/boton_liberado.png').convert_alpha(),
    'presionado':pygame.image.load('resources/graphics/boton_flecha/boton_presionado.png').convert_alpha()
}