#!/usr/bin/python3
import pygame

pygame.init()
FUENTE = pygame.font.Font('./resources/fonts/Fuente.ttf', 8)
CELDA = {
    'libre': pygame.image.load('./resources/graphics/CeldaLibre.png').convert(),
    'marcada': pygame.image.load('./resources/graphics/CeldaMarcada.png').convert()
}
BARCO = {
    'sano':pygame.image.load('./resources/graphics/Barco.png').convert_alpha(),
    'roto':pygame.image.load('./resources/graphics/BarcoRoto.png').convert_alpha()
}