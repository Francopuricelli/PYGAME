import pygame
from settings import *
from files import *

def game_over(segundos,score,nick):
    game_over_is_running = True
    font = pygame.font.Font(None,36)
    font_score =  pygame.font.Font(files["font"]["font_time"],36)
    while game_over_is_running:
        SCREEN.fill(NEGRO)
        draw_text(f" Segundos: {segundos} ",font_score,BLANCO,SCREEN,832,300)
        draw_text(f" Nick: {nick}      Score: {score}",font_score,BLANCO,SCREEN,832,200)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                game_over_is_running = False# (pygame.event.get()) retorna lista de eventos
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_over_is_running = False
                        records = cargar_rankings("records",nick,segundos)
                        rankings(records)
        pygame.display.flip()