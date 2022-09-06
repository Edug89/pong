import pygame as pg
from juego_pong.entidades import Bola, Raqueta
from juego_pong import BLANCO,ANCHO,ALTO, NARANJA,NEGRO,FPS, PRIMER_AVISO, ROJO, SEGUNDO_AVISO, TIEMPO_MAXIMO_PARTIDA,MAGENTA


class Partida():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((800,600))
        pg.display.set_caption("PONG")
        self.metronomo = pg.time.Clock()
        self.cronometro = TIEMPO_MAXIMO_PARTIDA

        self.bola = Bola(ANCHO // 2, ALTO // 2, color=(BLANCO))
        self.raqueta1 = Raqueta(20, ALTO // 2, w=20, h=120, color=(BLANCO))
        self.raqueta1.vy = 5
        self.raqueta2 = Raqueta(780,ALTO // 2, w=20, h=120, color=(BLANCO))
        self.raqueta2.vy = 5

        self.puntuacion1 = 0
        self.puntuacion2 = 0

        self.fuenteMarcador = pg.font.Font("juego_pong/fonts/silkscreen.ttf", 40)
        self.fuenteCronometro = pg.font.Font("juego_pong/fonts/silkscreen.ttf", 20)

        self.contadorFotogramas = 0
        self.fondoPantalla = NEGRO

    def fijar_fondo(self):#fijamos el fondo de pantalla según los segundos
        self.contadorFotogramas += 1
        if self.cronometro > PRIMER_AVISO:
            self.contadorFotogramas = 0
            return NEGRO

        elif self.cronometro > SEGUNDO_AVISO:
            #cada 10 fotogramas cambia de naranja a negro y viceversa
            if self.contadorFotogramas == 10:
                if self.fondoPantalla == NEGRO:
                    self.fondoPantalla = NARANJA
                else:
                    self.fondoPantalla = NEGRO  
                self.contadorFotogramas = 0  
            return  self.fondoPantalla
        else:
            #cada 5 fotogramas cambia de color negro y rojo y viceversa
            if self.contadorFotogramas >= 5:
                if self.fondoPantalla == ROJO:
                    self.fondoPantalla = NEGRO
                else:
                    self.fondoPantalla = ROJO
                self.contadorFotogramas = 0

        return self.fondoPantalla


    def bucle_ppal(self):
        self.bola.vx = 5
        self.bola.vy = -5

        game_over = False

        while not game_over and \
                self.puntuacion1 < 10 and \
                self.puntuacion2 < 10 and \
                self.cronometro > 0:

            salto_tiempo = self.metronomo.tick(FPS)
            self.cronometro -= salto_tiempo



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
            

            self.pantalla_principal.fill(self.fijar_fondo()) #fijamos el color de la pantalla principal con la función self.fijar_fondo
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

class Menu():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((800,600))
        pg.display.set_caption("MENÚ")
        self.metronomo = pg.time.Clock()
        self.imagenFondo = pg.image.load("juego_pong/images/swpong.jpg",)
        self.fuenteComenzar = pg.font.Font("juego_pong/fonts/silkscreen.ttf", 30)


    def bucle_ppal(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                #eventos que hace el usuario y lo captura pg.event.get() y lo devuelve una lista de eventos
                if evento.type == pg.QUIT:
                    game_over = True
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_RETURN:
                        game_over = True
                
            self.pantalla_principal.blit(self.imagenFondo, (0,0)) #sube una imagen a la pantalla principal
            menu = self.fuenteComenzar.render("Pulsa ENTER para comenzar",True,MAGENTA)
            self.pantalla_principal.blit(menu,(ANCHO // 6, ALTO - 100))
            
            pg.display.flip()
            #Manda el aviso a la pantalla, de todo lo editado en el while.



        
