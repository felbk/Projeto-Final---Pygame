import pygame
from os import path
from Config import WIDTH, HEIGHT
HOME = 0
PLAYING = 1
QUIT = 2
FPS = 30

def inicio_minerfox(tela):
    tempo_fps = pygame.time.Clock()
    tela_inicial = pygame.image.load('Assets/-tela_inicial/-tela_inicio_Miner_Fox (2).jpg').convert()
    tela_inicial = pygame.transform.scale(tela_inicial,(WIDTH,HEIGHT))
    tela_inicial_rect = tela_inicial.get_rect()
    start_text = pygame.font.SysFont(None,48)
    text = start_text.render('Press Enter to Play',True,(255,255,255))

    working = True
    while working:
        tempo_fps.tick(FPS)
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                working = False
        if keys[pygame.K_KP_ENTER]:
            state = PLAYING
            working = False
        if keys[pygame.K_ESCAPE]:
            state = QUIT
            working = False

        tela.blit(tela_inicial,tela_inicial_rect)
        tela.blit(text,(WIDTH/2 - 150, 0.7*HEIGHT))
        pygame.display.flip()
    return state



