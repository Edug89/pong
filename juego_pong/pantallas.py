import pygame as pg
from juego_pong.entidades import Bola, Raqueta
from juego_pong import BLANCO,ANCHO,ALTO,NEGRO,FPS,TIEMPO_MÁXIMO_PARTIDA


class Partida():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((800,600))
        pg.display.set_caption("PONG")
        self.metronomo = pg.time.Clock()
        self.cronometro = TIEMPO_MÁXIMO_PARTIDA

        self.bola = Bola(ANCHO // 2, ALTO // 2, color=(BLANCO))
        self.raqueta1 = Raqueta(20, ALTO // 2, w=20, h=120, color=(BLANCO))
        self.raqueta1.vy = 5
        self.raqueta2 = Raqueta(780,ALTO // 2, w=20, h=120, color=(BLANCO))
        self.raqueta2.vy = 5

        self.puntuacion1 = 0
        self.puntuacion2 = 0

        self.fuenteMarcador = pg.font.Font("juego_pong/fonts/silkscreen.ttf", 40)
        self.fuenteCronometro = pg.font.Font("juego_pong/fonts/silkscreen.ttf", 20)
        

    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5

        game_over = False

        while not game_over:
            self.metronomo.tick(FPS)

            for evento in pg.event.get():
                #eventos que hace el usuario y lo captura pg.event.get() y lo devuelve una lista de eventos
                if evento.type == pg.QUIT:
                    game_over = True
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.raqueta1.mover(pg.K_a, pg.K_z)
            quien = self.bola.mover()
            if quien == "DERECHA":
                self.puntuacion2 += 1
                print(f"{self.puntuacion1} - {self.puntuacion2}")
            elif quien == "IZQUIERDA":
                self.puntuacion1 += 1
                print(f"{self.puntuacion1} - {self.puntuacion2}")

            if self.puntuacion1 > 9 or self.puntuacion2 > 9:
                game_over = True



            self.bola.comprobar_choque(self.raqueta1,self.raqueta2)
            

            self.pantalla_principal.fill(NEGRO)
            self.bola.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            p1 = self.fuenteMarcador.render(str(self.puntuacion1),True, BLANCO)#se renderiza el marcador con las características
            self.pantalla_principal.blit(p1,(10,10))#se indica donde se coloca el marcador
            p2 = self.fuenteMarcador.render(str(self.puntuacion2),True, BLANCO)#se renderiza el marcador con las características
            self.pantalla_principal.blit(p2,(ANCHO - 40, 10))#se indica donde se coloca el marcador

            contador = self.fuenteCronometro.render(str(self.cronometro / 1000),True, BLANCO)
            self.pantalla_principal.blit(contador,(ANCHO // 2 , 10))

            pg.display.flip()
            #Manda el aviso a la pantalla, de todo lo editado en el while.