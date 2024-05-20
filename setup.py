
from sprites import Corpo , Player , Chão
from Config import WIDTH,HEIGHT, FPS
import pygame
from pygame.locals import *
from sys import exit
from Fase1 import Fase_1, Fase_3
from Inicio_MinerFox import inicio_minerfox
pygame.init()
tela = pygame.display.set_mode((WIDTH,HEIGHT))

HOME = 0
PLAYING = 1
QUIT = 2
FINAL = 3
state = HOME
fase = 1


while not state == QUIT:
    if state == HOME:
        #Rodar tela inicial
        state = inicio_minerfox(tela)
        #state =  tela inicial( )["state"] -> função que retorna um dicionario com state e N da fase 
    elif state == PLAYING: 
        if fase == 1:
            dici = Fase_3(tela)
            state = dici["state"]
            fase = dici["fase"]
pygame.quit()

        
