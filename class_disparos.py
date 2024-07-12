import pygame
from settings import *

class Disparos(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad):
        super().__init__()
        self.image = pygame.image.load("src/imagenes/disparo.png")
        self.image.set_colorkey(MAGENTA)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.velocidad = velocidad

    def update(self):
        self.rect.x += self.velocidad
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.kill()

disparos = pygame.sprite.Group()