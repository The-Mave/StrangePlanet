import pygame
import sys

pygame.init()


WIDTH = 1024
HEIGHT = 768
TILESIZE = 32

GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE

tickrate = pygame.time.get_ticks()
clock = pygame.time.Clock()

# --------------- COMMANDS SETTINGS

keys = pygame.key.get_pressed() #Para capturar as teclas pressionadas

# --------------- DEVELOPER MODE

# FPS CONFIG


draw_grid = True
display_fps = True


# --------------- FONT SETTINGS
font = pygame.font.get_default_font()
theFont = pygame.font.SysFont('arial black', 15)
