#!/usr/bin/python3
import pygame

pygame.init()
FUENTE = pygame.font.Font('./resources/fonts/Fuente.ttf', 8)
CELDA = {
    'libre': pygame.image.load('./resources/graphics/Celda_liberada.png').convert(),
    'libre_presionada': pygame.image.load('./resources/graphics/Celda_presionada.png').convert(),
    'marcada': pygame.image.load('./resources/graphics/Celda_marcada_liberada.png').convert(),
    'marcada_presionada': pygame.image.load('./resources/graphics/Celda_marcada_presionada.png').convert()
}
BARCO = {
    'sano':pygame.image.load('./resources/graphics/Barco.png').convert_alpha(),
    'roto':pygame.image.load('./resources/graphics/BarcoRoto.png').convert_alpha()
}


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

SONIDO_BOTON_CLICK = pygame.mixer.Sound('./resources/audio/button_click.mp3')
SONIDO_AGUA = pygame.mixer.Sound('./resources/audio/splash.mp3')
SONIDO_EXPLOSION = pygame.mixer.Sound('./resources/audio/explotion.mp3')

# Musica proporcionado por Eric F. Ricci
MUSICA_MENU = './resources/audio/Arcade_1.mp3'
MUSICA_JUEGO = './resources/audio/Arcade_4.mp3'
