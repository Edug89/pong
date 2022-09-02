import pygame as pg
from entidades import Bola, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("PONG")
cronometro = pg.time.Clock()


bola = Bola(400, 300, color=(255,255,255))
bola.vx = 3
bola.vy = 3
raqueta1 = Raqueta(20, 300, w=20, h=120, color=(255,255,255))
raqueta2 = Raqueta(780,300, w=20, h=120, color=(255,255,255))
raqueta2.vy = 5
raqueta1.vy = 5
marcador1 = 0
marcador2 = 0

game_over = False

while not game_over:
    dt = cronometro.tick()
    for evento in pg.event.get():
        #eventos que hace el usuario y lo captura pg.event.get() y lo devuelve una lista de eventos
        if evento.type == pg.QUIT:
            game_over = True
    raqueta2.mover(pg.K_UP, pg.K_DOWN)
    raqueta1.mover(pg.K_a, pg.K_z)
    bola.mover()
    bola.comprobar_choque(raqueta1,raqueta2)
    

    pantalla_principal.fill((0, 0, 0))
    bola.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()
    #Manda el aviso a la pantalla, de todo lo editado en el while.