

def Fase_1(tela):
    from Config import WIDTH, HEIGHT , FPS
    mapa = pygame.Surface((2000,2000))
    play = True
    

    Chão((tela.get_width(),50),(800,tela.get_height() - 50 ),"Assets\provisorios\chao.png")
    Chão((tela.get_width()/2,120),(0,tela.get_height() - 120 ),"Assets\provisorios\chao.png")
    Chão((tela.get_width()/2,50),(500,tela.get_height() - 320 ),"Assets\provisorios\chao.png")

    player = Player((150,150),(tela.get_width()/2,0))

    vel = 2
    clock = pygame.time.Clock()
    clock.tick(FPS)
    while play:
     
        mapa.fill((255,255,255))
        
        
        #Analisa eventos
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_0:
                    mostracls = not mostracls

        keys = pygame.key.get_pressed()
        
            
        if keys[pygame.K_d]: 
            player.vx = vel
            player.flip = False   
        elif keys[pygame.K_a]: 
            player.vx = -vel 
            player.flip = True  
        else:
            player.vx = 0          
            
        if keys[pygame.K_ESCAPE]:
             pygame.quit()
        if keys[pygame.K_SPACE ] and not player.Fall :
            player.vy = -5
            player.jump = True
        if not keys[pygame.K_SPACE ]:
            player.jump = False

        #nao ultrapassa limites do mapa
        if player.rect.left < 0 :
            player.vx =1         
        if player.rect.rightt > mapa.get_width() :
            player.vx=-1
                    
                    
        elementos.update()
        
    
        
        mostra_mapa_na_tela(tela,mapa,player)

        pygame.display.flip()

    return {"state": QUIT , "fase": 1}


#==============IMPORTS===============

import pygame
from pygame.locals import *
from sys import exit
from sprites import *
from setup import QUIT , PLAYING , HOME
