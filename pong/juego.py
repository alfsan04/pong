import pygame as pg
from pong import ALTO, ANCHO
from pong.pantallas import Menu, Partida, Records

class Juego:
    def __init__(self):
        self.pantalla_ppal = pg.display.set_mode((ANCHO, ALTO))
        self.metronomo = pg.time.Clock()

        self.escenas = [
            Menu(self.pantalla_ppal, self.metronomo),
            Partida(self.pantalla_ppal, self.metronomo),
            Records(self.pantalla_ppal, self.metronomo)
        ]

    def start(self):
        #TODO: Poner lógica de navegación entre escenas


