import pygame
pygame.init()

# DEVELOPER MODE
DEV_MODE = 1


WIDTH = 1024
HEIGHT = 768
TILESIZE = 32


screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#comment
pygame.display.update()
pygame.quit()


#teste2



