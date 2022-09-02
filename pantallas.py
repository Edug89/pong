from string import punctuation
import pygame as pg
from entidades import Bola, Raqueta

ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 255)
AMARILLO = (255, 255, 0)

class Partida():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((800,600))
        pg.display.set_caption("PONG")
        self.cronometro = pg.time.Clock()

        self.bola = Bola(ANCHO // 2, ALTO // 2, color=(BLANCO))
        self.raqueta1 = Raqueta(20, ALTO // 2, w=20, h=120, color=(BLANCO))
        self.raqueta1.vy = 5
        self.raqueta2 = Raqueta(780,ALTO // 2, w=20, h=120, color=(BLANCO))
        self.raqueta2.vy = 5

        self.puntuacion1 = 0
        self.puntuacion2 = 0

    def bucle_ppal(self):
        self.bola_vx = 3
        self.bola_vy = -3

        while not game_over:
            self.cronometro.tick()
            for evento in pg.event.get():
                #eventos que hace el usuario y lo captura pg.event.get() y lo devuelve una lista de eventos
                if evento.type == pg.QUIT:
                    game_over = True
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.raqueta1.mover(pg.K_a, pg.K_z)
            quien =self.bola.mover()
            if quien == "DERECHA":
                puntuacion1 += 1
            elif quien == "IZQUIERDA":
                puntuacion2 += 1


            self.bola.comprobar_choque(self.raqueta1,self.raqueta2)
            

            self.pantalla_principal.fill(NEGRO)
            self.bola.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            pg.display.flip()
            #Manda el aviso a la pantalla, de todo lo editado en el while.