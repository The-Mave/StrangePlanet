import pygame
import math
from settings import *

pygame.init()

# AS CONFIGURAÇÕES GERAIS ESTAO EM SETTINGS.PY

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

while True:
    screen.fill((50,50,50))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
# DEBUG options
    
    if draw_grid:
        for x in range (0,WIDTH, TILESIZE):
            pygame.draw.line(screen,(100,100,100),(x,0),(x, HEIGHT))
        for y in range (0,WIDTH, TILESIZE):
            pygame.draw.line(screen,(100,100,100),(0,y),(WIDTH, y))

    if display_fps:
        rounded_fps = int(clock.get_fps())
        FPS = str(rounded_fps)
        screen.blit(theFont.render(FPS + ' - FPS', 1, (255, 255, 255)),(5, 5))


    pygame.display.flip()
    




