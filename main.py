import pygame as pg
from entidades import Bola, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")

game_over = False
bola = Bola(400, 300, color = (255, 255, 255))
raqueta1 = Raqueta(20, 300, w=20, h=120, color = (255, 255, 255))
raqueta2 = Raqueta(780, 300, w=20, h=120, color = (255, 255, 255))

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0, 0, 0))

    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()

