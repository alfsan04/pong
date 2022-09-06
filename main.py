import pygame as pg
from entidades import Bola, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")
'creamos un cronometro obteniendo el objeto time.clock propio de pygame'
cronometro = pg.time.Clock()

game_over = False
bola = Bola(400, 300, color = (255, 255, 255))
raqueta1 = Raqueta(20, 300, w=20, h=120, color = (255, 255, 255))
raqueta2 = Raqueta(780, 300, w=20, h=120, color = (255, 255, 255))
raqueta1.vy = 5
raqueta2.vy = 5

while not game_over:
    'Controlamos la tasa de refresco, hace 60 bucles por segundo, uno cada aprox 16 milisegundos'
    dt = cronometro.tick(60)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    raqueta1.mover(pg.K_w, pg.K_s)
    raqueta2.mover(pg.K_UP, pg.K_DOWN)

    pantalla_principal.fill((0, 0, 0))

    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()

