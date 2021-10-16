import pygame
from pygame.constants import KEYDOWN, K_a, K_d, K_s, K_w
from settings import *

pygame.init()
# AS CONFIGURAÇÕES GERAIS ESTAO EM SETTINGS.PY

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

while True:
    screen.fill((50,50,50)) #Preenchendo o fundo com a cor acinzentada
    clock.tick(60) #Defininfo clock de processamento para 60 Frames per Second

    for event in pygame.event.get(): #captura de eventos pygame
        if event.type == pygame.QUIT:
            pygame.joystick.quit() 

        #MOVIMENTAÇÃO DO PLAYER
        if event.event.type == KEYDOWN:
            if keys[K_w]:
                print("Key 'W' has been pressed")
               
            if keys[K_a]:
                print("Key 'A' has been pressed")

            if keys[K_s]:
                print("Key 'S' has been pressed")

            if keys[K_d]:
                print("Key 'D' has been pressed")   


# DEBUG options   
    if draw_grid: #Desenha o Grid na tela (Ladrilhos)
        for x in range (0,WIDTH, TILESIZE):
            pygame.draw.line(screen,(100,100,100),(x,0),(x, HEIGHT))
        for y in range (0,WIDTH, TILESIZE):
            pygame.draw.line(screen,(100,100,100),(0,y),(WIDTH, y))

    if display_fps: #Mostra o FPS na tela
        rounded_fps = int(clock.get_fps())
        FPS = str(rounded_fps)
        screen.blit(theFont.render(FPS + ' - FPS', 1, (255, 255, 255)),(5, 5))

    pygame.display.flip()
    




