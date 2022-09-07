import pygame as pg
from pong.pantallas import Menu, Partida
from pong import ANCHO,ALTO

class Controlador():
    def __init__(self):#init empaqueta todo
        pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        metronomo = pg.time.Clock()

        self.menu = Menu(pantalla_principal,metronomo)#instancia el paquete menu
        self.partida = Partida(pantalla_principal,metronomo)# instancia el paquete partida

    def jugar(self):
        salida = False
        while not salida: #bucle infinito
            salida = self.menu.bucle_ppal() #el bucle que inicia la pantalla menú
            if not salida:
                salida = self.partida.bucle_ppal() #el bucle que inicia la pantalla partida
            

