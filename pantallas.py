import pygame as pg
from entidades import Bola, Raqueta

ANCHO = 800
ALTO = 600

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)

pg.init()

class Partida:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Pong")
        self.metronomo = pg.time.Clock()

        self.bola = Bola(ANCHO // 2, ALTO // 2, color = BLANCO)
        self.raqueta1 = Raqueta(20, ALTO // 2, w=20, h=120, color = BLANCO)
        self.raqueta1.vy = 5
        self.raqueta2 = Raqueta(ANCHO - 20, ALTO // 2, w=20, h=120, color = BLANCO)
        self.raqueta2.vy = 5

        self.puntuacion1 = 0
        self.puntuacion2 = 0

    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5

        game_over = False

        while not game_over:
            'Controlamos la tasa de refresco, hace 60 bucles por segundo, uno cada aprox 16 milisegundos'
            self.metronomo.tick(60)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            quien = self.bola.mover()
            if quien == 'RIGHT':
                self.puntuacion2 += 1
            elif quien == 'LEFT':
                self.puntuacion1 += 1
            
            self.bola.comprobar_choque(self.raqueta1, self.raqueta2)

            self.pantalla_principal.fill(NEGRO)

            self.bola.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            

            pg.display.flip()