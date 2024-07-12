from settings import *
import pygame
import json
from files import *
from class_disparos import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # RECTANGULO PLAYER
        self.quieto = [pygame.image.load(files["images"]["quieto"]),
                    pygame.image.load(files["images"]["quieto2"]),
                    pygame.image.load(files["images"]["quieto3"]),
                    pygame.image.load(files["images"]["quieto4"]),
                    pygame.image.load(files["images"]["quieto5"])]
        self.right = [pygame.image.load(files["images"]["quieto"]),
                    pygame.image.load(files["images"]["derecha"]),
                    pygame.image.load(files["images"]["derecha1"]),
                    pygame.image.load(files["images"]["derecha2"]),
                    pygame.image.load(files["images"]["derecha3"]),
                    pygame.image.load(files["images"]["derecha4"]),
                    pygame.image.load(files["images"]["derecha5"])]
        self.left = [pygame.image.load(files["images"]["izquierda"]),
                    pygame.image.load(files["images"]["izquierda1"]),
                    pygame.image.load(files["images"]["izquierda2"]),
                    pygame.image.load(files["images"]["izquierda3"]),
                    pygame.image.load(files["images"]["izquierda4"]),
                    pygame.image.load(files["images"]["izquierda5"])]
        self.salto = [pygame.image.load(files["images"]["derecha4"])]
        self.frame_index = 0
        self.image = self.quieto[self.frame_index]
        self.rect = self.image.get_rect()
        self.jump = False
        self.cuentaPasos = 0
        self.cuentaSaltos = 10
        self.damage = 1
        self.attack_speed = 1100  
        self.ultimo_lanzamiento = pygame.time.get_ticks()
        self.escudo = False
        self.escudo_contador = 0
        self.parpadeo_contador = 0
        self.visible = True
        
        self.speed = 0
        self.rect.x = 400
        self.rect.y = 500
        self.vidas = 3
        
    
    def get_frame(self, frame_set):
        if self.frame_index >= len(frame_set):
            self.frame_index = 0
        frame = frame_set[self.frame_index]
        self.frame_index += 1
        return frame
    
    def saltar(self, teclas):
        if not self.jump:
            if teclas[pygame.K_SPACE]:
                self.jump = True
                self.cuentaPasos = 0
        else:
            self.image = self.get_frame(self.salto)
            if self.cuentaSaltos >= -10:
                self.rect.y -= (self.cuentaSaltos * abs(self.cuentaSaltos)) * 0.6
                self.cuentaSaltos -= 1
            else:
                self.cuentaSaltos = 10
                self.jump = False

    def update(self):
        # Actualiza esto cada vuelta de bucle.
        self.speed = 0

        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
        # Mueve el personaje hacia la izquierda
        if teclas[pygame.K_a]:
            self.image = self.get_frame(self.left)
            self.speed = -20
            
            
        elif teclas[pygame.K_d]:
            self.image = self.get_frame(self.right)
            self.speed = 20
            
            
        else:
            self.image = self.get_frame(self.quieto)
        
        self.saltar(teclas)
        # Actualiza la posición del personaje
        self.rect.x += self.speed

        # IZQUIERDO
        if self.rect.left < 0:
            self.rect.left = 0
        # DERECHO
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.escudo:
            self.parpadeo_contador += 1
            if self.parpadeo_contador >= 5:  # Cambia el valor para ajustar la frecuencia de parpadeo
                self.visible = not self.visible
                self.parpadeo_contador = 0
        else:
            self.visible = True

        if self.visible:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(0)

    def disparo_derecha(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_lanzamiento > self.attack_speed:
            bala = Disparos(self.rect.centerx, self.rect.centery, 15)  
            disparos.add(bala)
            self.ultimo_lanzamiento = tiempo_actual
    def disparo_izquierda(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_lanzamiento > self.attack_speed:# Disparo hacia la derecha
            bala = Disparos(self.rect.centerx, self.rect.centery, -15)  # Disparo hacia la izquierda
            disparos.add(bala)
            self.ultimo_lanzamiento = tiempo_actual
    def Powerup(self):
        powerup = Fireball()
        power_up.add(powerup)

class Fireball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("src/imagenes/FIREBALL.png")
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 500
        self.speed = 0

    def update(self):
        self.colision_player_powerup = pygame.sprite.spritecollide(player, power_up, False)
        if self.colision_player_powerup:
            player.speed = 50
            
        player.rect.x += player.speed




power_up = pygame.sprite.Group()
powerup = Fireball()
power_up.add(powerup)

sprites = pygame.sprite.Group()  # Jugador
player = Jugador()
sprites.add(player)



