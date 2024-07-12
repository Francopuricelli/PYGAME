import pygame
from settings import *
import random
from class_player import *
from class_enemy import *
from class_disparos import *
from game_over import *
from files import *

def menu():
    global nick
    menu_ = pygame.image.load(files["images"]["menu"])
    menu_ = pygame.transform.scale(menu_,(WIDTH,HEIGTH))
    pygame.mixer.music.load(files["music"]["menu_music"])
    pygame.mixer.music.play(-1,4)
    fuente = pygame.font.Font(None,36)
    menu_running = True
    nick = "ID"
    print_nick = False
    nick_ready = False
    quit_game = True
    while menu_running:
        global x
        x_relativa = x % menu_.get_rect().width #obtengo el ancho del background y lo divido por x
    #x_relativa - background.get_rect().width hace que se reproduzca el fondo en bucle
        SCREEN.blit(menu_,(x_relativa - menu_.get_rect().width ,y)) #el (0,0) representa la x y la y
        if x_relativa < WIDTH:
            SCREEN.blit(menu_,(x_relativa,y))
        x -= 0
        for event in pygame.event.get():  # (pygame.event.get()) retorna lista de eventos
            if event.type == pygame.QUIT: 
                menu_running = None
            elif event.type == pygame.KEYDOWN:
                if print_nick and nick_ready == False:
                    if event.key == pygame.K_RETURN:
                        nick_ready = True
                    elif event.key == pygame.K_BACKSPACE:
                        nick = nick[:-1] 
                    else:
                        nick += event.unicode #escribe cada caracter


        mouse_x, mouse_y = pygame.mouse.get_pos()
        boton_nombre = pygame.Rect((40,170),(140,50))
        boton_play = pygame.Rect((40,250),(140,50))
        boton_quit = pygame.Rect((40,450),(140,50))
        
        if nick_ready == False:
            pygame.draw.rect(SCREEN,NEGRO,boton_nombre)
        else:
            pygame.draw.rect(SCREEN,NEGRO,boton_play)

        pygame.draw.rect(SCREEN,NEGRO,boton_quit)

        if nick_ready == False:
            texto_visible = fuente.render(nick,True,RED)
        SCREEN.blit(texto_visible,(100,180))
        draw_text("PLAY",fuente,RED,SCREEN,110,270)
        draw_text("QUIT",fuente,RED,SCREEN,110,470)
        
        if boton_nombre.collidepoint((mouse_x,mouse_y)):
            if pygame.mouse.get_pressed()[0]:
                print_nick = True
                nick = ""
        if boton_play.collidepoint((mouse_x,mouse_y)) and nick_ready == True:
            if pygame.mouse.get_pressed()[0]:
                menu_running = False
                game(nick)
        if boton_quit.collidepoint((mouse_x,mouse_y)):
            if pygame.mouse.get_pressed()[0]:
                menu_running = False
                quit_game = False




        pygame.display.flip()


    pygame.mixer_music.stop()
    if menu_running == True:
        pass
    elif menu_running == False:
        if quit_game == False:
            return False
        else:
            return True 
            

def game(nick):
    is_running = True
    fuente_time = pygame.font.Font(files["font"]["font_time"],27)
    #escudo = False
    escudo_contador = 0
    milisegundos = 0
    colisiono = False
    tiempo_ultimo_enemigo = pygame.time.get_ticks()
    intervalo_enemigos = 5000
    #crear_enemigos_aleatorios(enemigos,3,5,WIDTH)
    pygame.mixer.music.load(files["music"]["main_music"])
    pygame.mixer_music.play(-1,2)
    pygame.mixer_music.set_volume(0.5)
    segundos = 0
    minutos = 0
    score = 0
    player.rect.x = 400
    player.rect.y = 500
    player.vidas = 3

    for enemigo in enemigos:
        enemigo.rect.x = 1500
        enemigo.rect.y = 500 


    if not colisiono:
        if is_running:
            pygame.mixer.music.load(files["music"]["main_music"])
            pygame.mixer.music.play(-1, 2)
        while is_running: #esto corre el juego
            clock.tick(FPS)
            for event in pygame.event.get():  # (pygame.event.get()) retorna lista de eventos
                if event.type == pygame.QUIT: 
                    is_running = False #para quitear del juego
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        player.disparo_derecha()
                    elif event.key == pygame.K_q:
                        player.disparo_izquierda()
                    elif event.key == pygame.K_ESCAPE:
                        wait_user(K_ESCAPE)

            
            milisegundos += 0.5
            if milisegundos == 17:
                segundos += 1
                milisegundos = 0
            
            escudo_contador += 1




            draw_text(f"Time: {segundos}",fuente_time,BLANCO,SCREEN,125,60)
            draw_text(f"HP: {player.vidas}", fuente_time,BLANCO,SCREEN,125,97)




            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - tiempo_ultimo_enemigo >= intervalo_enemigos:
                crear_enemigos_aleatorios(enemigos,3,5,WIDTH)
                tiempo_ultimo_enemigo = tiempo_actual

            sprites.update()
            enemigos.update(player)
            disparos.update()
            #power_up.update()


            enemigos.draw(SCREEN) 
            sprites.draw(SCREEN)
            disparos.draw(SCREEN)
                    #power_up.draw(SCREEN)

            
            #--------------------COLISIONES--------------------------------------------#
            colision_player = pygame.sprite.spritecollide(player,enemigos,False) 
            colision_balas = pygame.sprite.groupcollide(enemigos,disparos,True,True)
            if colision_balas:
                score += 10

            
            if player.escudo == False:
                if colision_player:
                    escudo_contador = -1
                    player.vidas -= 1
                    player.escudo = True


                    if player.vidas == 0:
                        is_running = False
                        colisiono = True
                        game_over(segundos,score,nick)
                        menu()

            else:
                if escudo_contador >= 90:
                    player.escudo = False



            pygame.display.flip() # actualiza la pantalla
            recargapantalla()








pygame.init() #INICIALIZA


pygame.display.set_caption("Shadows Of Evil") #cambia el nombre de la ventana
icono = pygame.image.load("src/imagenes/pj.png")
pygame.display.set_icon(icono)


menu()


pygame.quit()#DESCONECTA


