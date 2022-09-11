import pygame as pg
from pong.pantallas import Menu, Partida
from pong import ANCHO, ALTO

class Controlador:
    def __init__(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        metronomo = pg.time.Clock()

        self.pantallas = [Menu(pantalla_principal, metronomo), Partida(pantalla_principal, metronomo)]

        self.menu = Menu(pantalla_principal, metronomo)
        self.partida = Partida(pantalla_principal, metronomo)
        
    def jugar(self):
        salida = False
        ix = 0
        while not salida:
            salida = self.pantallas[ix].bucle_ppal()
            ix = (ix + 1) % len(self.pantallas)
