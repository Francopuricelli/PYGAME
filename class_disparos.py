from settings import *
import pygame

class Disparos(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("src/imagenes/disparo.png")
        self.image.set_colorkey(MAGENTA)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x

    def update(self):
        self.rect.x += 15
        if self.rect.right > WIDTH:
            self.kill()
    
disparos = pygame.sprite.Group()