import pygame as pg
from pong.entidades import Bola, Raqueta
from pong import ANCHO, ALTO, BLANCO, MAGENTA, NARANJA, NEGRO, FPS, PRIMER_AVISO, PUNTUACION_GANADORA, ROJO, SEGUNDO_AVISO, TIEMPO_MAXIMO_PARTIDA

class Partida:
    def __init__(self, pantalla, metronomo):
        self.pantalla_principal = pantalla
        self.metronomo = metronomo
        pg.display.set_caption("Pong")
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

        self.contador_fotogramas = 0
        self.cambiar_color = True

    def fijar_fondo(self):
        if self.temporizador > PRIMER_AVISO:
            return NEGRO
        elif self.temporizador > SEGUNDO_AVISO:
            #cada 10 fotogramas cambia de naranja a negro y viceversa
            if self.contador_fotogramas % 10 == 0:
                self.cambiar_color = not(self.cambiar_color)
            if self.cambiar_color == True:
                return NARANJA
            else:
                return NEGRO
        else:
            #cada 5 fotogramas cambia de rojo a negro y viceversa
            if self.contador_fotogramas % 5 == 0:
                self.cambiar_color = not(self.cambiar_color)
            if self.cambiar_color == True:
                return ROJO
            else:
                return NEGRO

    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5
        self.puntuacion1 = 0
        self.puntuacion2 = 0
        self.temporizador = TIEMPO_MAXIMO_PARTIDA

        game_over = False
        self.metronomo.tick()
        while not game_over and \
               self.puntuacion1 < PUNTUACION_GANADORA and \
               self.puntuacion2 < PUNTUACION_GANADORA and \
               self.temporizador > 0:
            
            'Controlamos la tasa de refresco, hace 60 bucles por segundo, uno cada aprox 16 milisegundos'
            salto_tiempo = self.metronomo.tick(FPS)
            self.temporizador -= salto_tiempo
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True

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
            self.contador_fotogramas += 1
            

            pg.display.flip()

class Menu:
    def __init__(self, pantalla, metronomo):
        self.pantalla_principal = pantalla
        self.metronomo = metronomo
        pg.display.set_caption("Menu")
        self.imagenFondo = pg.image.load("pong/images/portada.jpeg")
        self.fuenteComenzar = pg.font.Font("pong/fonts/silkscreen.ttf", 50)
        self.musica = pg.mixer.Sound("pong/sounds/8-Bit.mp3")

    def bucle_ppal(self):
        game_over = False
        self.musica.play(-1)
        
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True

            self.pantalla_principal.blit(self.imagenFondo, (0, 0))
            menu = self.fuenteComenzar.render("Pulsa ENTER para comenzar", True, MAGENTA)
            self.pantalla_principal.blit(menu, (ANCHO // 2, ALTO - 150))
            pg.display.flip()
        self.musica.stop()
