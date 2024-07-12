from settings import *
import pygame
from files import *
class Enemies(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        #RECTANGULO PLAYER
        self.image = pygame.image.load(files["images"]["enemigo2"])
        self.image.set_colorkey(COLOR_FONDO_ENEMIES)
        #obtiene el rectangulo (sprite)
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 500
        self.speed = 4
        self.hp = 100

    def update(self,player):
        #actualiza la velocidad del enemigo
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        
        #----------------MARGENES----------------
        #IZQUIERDO
        if self.rect.left < 0:
            self.rect.left = 0
        #DERECHO
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def sacar_hp(self,cant):
        print(self.hp)
        self.hp -= cant
        print(self.hp)
        if self.hp <= 0:
            print("entro kill")
            self.kill()


def crear_enemigos_aleatorios(enemigos,cantidad_min, cantidad_max,width):
    cantidad_enemigos = random.randint(cantidad_min, cantidad_max)
    for _ in range(cantidad_enemigos):
        enemigo = Enemies()
        enemigo.rect.x = random.randint(1500, width - enemigo.rect.width)
        enemigos.add(enemigo)
enemigos = pygame.sprite.Group()
enemigo = Enemies()
enemigos.add(enemigo)