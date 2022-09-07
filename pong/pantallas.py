import pygame as pg
from pong.entidades import Bola, Raqueta
from pong import ANCHO, ALTO, BLANCO, NARANJA, NEGRO, FPS, PRIMER_AVISO, ROJO, SEGUNDO_AVISO, TIEMPO_MAXIMO_PARTIDA

class Partida:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Pong")
        self.metronomo = pg.time.Clock()
        self.temporizador = TIEMPO_MAXIMO_PARTIDA

        self.bola = Bola(ANCHO // 2, ALTO // 2, color = BLANCO)
        self.raqueta1 = Raqueta(20, ALTO // 2, w=20, h=120, color = BLANCO)
        self.raqueta1.vy = 5
        self.raqueta2 = Raqueta(ANCHO - 20, ALTO // 2, w=20, h=120, color = BLANCO)
        self.raqueta2.vy = 5

        self.puntuacion1 = 0
        self.puntuacion2 = 0

        self.fuenteMarcador = pg.font.Font("pong/fonts/silkscreen.ttf", 40)
        self.fuenteTemporizador = pg.font.Font("pong/fonts/silkscreen.ttf", 20)

    def fijar_fondo(self):
        if self.temporizador > PRIMER_AVISO:
            return NEGRO
        elif self.temporizador > SEGUNDO_AVISO:
            return NARANJA
        else:
            return ROJO

    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5

        game_over = False

        while not game_over and self.puntuacion1 < 10 and self.puntuacion2 < 10 and self.temporizador > 0:
            'Controlamos la tasa de refresco, hace 60 bucles por segundo, uno cada aprox 16 milisegundos'
            salto_tiempo = self.metronomo.tick(FPS)
            self.temporizador -= salto_tiempo
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            quien = self.bola.mover()
            if quien == 'RIGHT':
                self.puntuacion1 += 1
                print(f'{self.puntuacion1} - {self.puntuacion2}')
            elif quien == 'LEFT':
                self.puntuacion2 += 1
                print(f'{self.puntuacion1} - {self.puntuacion2}')
            
            self.bola.comprobar_choque(self.raqueta1, self.raqueta2)

            self.pantalla_principal.fill(self.fijar_fondo())
            self.bola.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            p1 = self.fuenteMarcador.render(str(self.puntuacion1), True, BLANCO)
            p2 = self.fuenteMarcador.render(str(self.puntuacion2), True, BLANCO)
            contador = self.fuenteTemporizador.render(str(self.temporizador / 1000), True, BLANCO)
            self.pantalla_principal.blit(p1,(10,10))
            self.pantalla_principal.blit(p2, (ANCHO - 40,10))
            if self.temporizador >= 0:
                self.pantalla_principal.blit(contador, (ANCHO // 2, 10))
            

            pg.display.flip()