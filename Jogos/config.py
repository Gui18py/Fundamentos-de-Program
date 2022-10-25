import pygame

class Settings:
    def __init__(self, tamanhox=0, tamanhoy=0):
        self.tamanhox = tamanhox
        self.tamanhoy = tamanhoy
    
    def janela(self):
        self.tamanho_janela = 200
        self.tamanho_pixels = 4
        self.janela = pygame.display.set_mode(
    (self.tamanhox, self.tamanhoy))
        return self.janela
    
        