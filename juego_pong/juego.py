import pygame as pg
from juego_pong import ANCHO,ALTO
from juego_pong.pantallas import Menu,Partida

class Juego():
    def __init__(self):
        self.pantalla_ppal = pg.display.set_mode((800,600))
        self.metronomo = pg.time.Clock()

        self.escenas = [
            Menu(),
            Partida()
        ]

    def star(self):
        pass
