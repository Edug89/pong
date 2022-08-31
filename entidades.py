import pygame as pg

class Bola:
    def __init__(self, center_x, center_y, radio = 10, color=(255,255,0)):
        self.center_x = center_x
        self.center_y = center_y
        self.radio = radio
        self.color = color

        self.vx = 0
        self.vy = 0

    def dibujar(self,pantalla):
        pg.draw.circle(pantalla, self.color, (self.center_x , self.center_y), self.radio)

class Raqueta:
    def __init__(self, center_x, center_y, w=120, h=20, color=(255,255,0)):
        self.center_x = center_x
        self.center_y = center_y
        self.h = h
        self.w = w
        self.color = color

        self.vx = 0
        self.vy = 0

    def dibujar(self, pantalla):
        pg.draw.rect(pantalla, self.color, (self.center_x - self.w // 2, self.center_y - self.h //2, self.w, self.h))
        #Se hace la formula de rectarle 
    
    def mover(self,tecla_arriba,tecla_abajo, y_max=600):
        estado_teclas = pg.key.get_pressed()
        if estado_teclas[tecla_arriba]:
            self.center_y -= self.vy
        if self.center_y < self.h // 2:
            self.center_y = self.h // 2

        if estado_teclas[tecla_abajo]:
            self.center_y += self.vy
        if self.center_y > y_max - self.h // 2:
            self.center_y = y_max - self.h // 2
            





    

