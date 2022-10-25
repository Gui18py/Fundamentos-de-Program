import pygame
import random
import time
from config import Settings

tamanho_x = 1000
tamanho_y = 600
fps = pygame.time.Clock()
score = 0
velocidade_cobra = 15

pygame.init()
settings = Settings(tamanho_x, tamanho_y)
settings.janela()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
    pygame.display.flip()