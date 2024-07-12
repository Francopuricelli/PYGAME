import pygame
from pygame.locals import *

#from class_enemy import *
WIDTH = 1665
HEIGTH = 600

SCREEN_SIZE = (WIDTH, HEIGTH)
clock = pygame.time.Clock()#reloj
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

SCREEN_CENTER = (WIDTH // 2 , HEIGTH // 2)
RED = (255,0,0)
COLOR_FONDO_ENEMIES = (121,230,234)
MAGENTA =(255, 0, 255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)
x = 0
y = 0
FPS = 30

velocidad = 5
salto = False
izquierda = False
derecha = False
px = 50 #representa la ubicacion del personaje con respecto al eje x
py = 500 # representa la ubicacion del personaje con respecto al eje y
ancho = 40
cuentaPasos = 0
cuentasaltos = 10
contadorquieto_mini = 0
indice_imagen = 0
indice_corre = 0
contador_index = 0
tick = 0

izquierda = False
derecha = True
barra_flotante_speed = 10
barra_flotante = pygame.Rect(800,380,300,10)

def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


def barra_flotante_mover(player):
    global izquierda, derecha, barra_flotante, barra_flotante_speed
    
    if derecha:
        barra_flotante.x += barra_flotante_speed
        if barra_flotante.right >= WIDTH:
            derecha = False
            izquierda = True
    elif izquierda:
        barra_flotante.x -= barra_flotante_speed
        if barra_flotante.left <= 0:
            izquierda = False
            derecha = True

    if player.rect.colliderect(barra_flotante):
        if player.rect.bottom >= barra_flotante.top and player.rect.bottom <= barra_flotante.bottom:
            player.rect.bottom = barra_flotante.top
            player.rect.y = 0
    pygame.draw.rect(SCREEN, (218, 165, 32), barra_flotante, 0, 5)


def draw_text(text, font, color, surface,x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def swap_lista(lista:list,i:int,j:int):
    """swapea lugares

    Args:
        lista (list): _description_
        i (int): _description_
        j (int): _description_
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista [j] = aux



def ordenar_lista_doble(lista, campo1, campo2):
    """ordena lista con doble parametro

    Args:
        lista (_type_): _description_
        campo1 (_type_): Separa el campo
        campo2 (_type_): campo a ordenar

    Raises:
        ValueError: _description_
    """
    if isinstance(lista,list):
            
            tam = len(lista)
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i][campo1] == lista[j][campo1]:
                        if lista[i][campo2] < lista[j][campo2]:
                            swap_lista(lista, i, j)  
                    elif lista[i][campo1] < lista[j][campo1]:
                        swap_lista(lista,i,j)
    else:
        raise ValueError("No se ingreso ninguna lista")
    


def wait_user(tecla):
    continuar = True
    while continuar:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                if evento.key == tecla:
                    continuar = False



def mostrar_rankings(nombre_archivo,nick,time):
    """ Carga un archivo .CSV

    Args:
        nombre_archivo (_type_): _description_
        lista (_type_): _description_

    Returns:
        _type_: me retorna el contenido del archivo en una lista.
    """
    fuente = pygame.font.Font(None,26)
    lista = []
    lista.append({"nick" : nick, "time" : time})
    with open(get_path_actual(nombre_archivo + ".csv"), "r", encoding="utf-8") as archivo :
        encabezado = archivo.readline().strip("\n").split(",")

        for linea in archivo.readlines():
            standing= {}
            linea = linea.strip("\n").split(",")

            nick,time = linea
            standing["nick"] = nick
            standing["time"] = int(time)

            lista.append(standing)



        draw_text(f"ID             TIEMPO", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 2,HEIGTH -HEIGTH // 2 - 170)
        draw_text(f"               1.{lista[0]["name"]}         {lista[0]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 - 130)
        draw_text(f"               2.{lista[1]["name"]}         {lista[1]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 - 100)
        draw_text(f"               3.{lista[2]["name"]}         {lista[2]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 - 70)
        draw_text(f"               4.{lista[3]["name"]}         {lista[3]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 - 40)
        draw_text(f"               5.{lista[4]["name"]}         {lista[4]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 - 10)
        draw_text(f"               6.{lista[5]["name"]}         {lista[5]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 + 20)
        draw_text(f"               7.{lista[6]["name"]}         {lista[6]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 + 50)
        draw_text(f"               8.{lista[7]["name"]}         {lista[7]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 + 80)
        draw_text(f"               9.{lista[8]["name"]}         {lista[8]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 + 110)
        draw_text(f"              10.{lista[9]["name"]}        {lista[9]["second"]:2}", fuente, BLANCO, SCREEN, WIDTH - WIDTH // 1.7,HEIGTH -HEIGTH // 2 + 140)
    return lista