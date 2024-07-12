import pygame
from pygame.locals import *

import random
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

background = pygame.image.load("src/imagenes/backgroundcronichles1.png")
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


def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

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

def cargar_rankings(nombre_archivo,nick,time):
    """ Carga un archivo .CSV

    Args:
        nombre_archivo (_type_): _description_
        lista (_type_): _description_

    Returns:
        _type_: me retorna el contenido del archivo en una lista.
    """
    lista = []
    lista.append({"nick" : nick, "time" : time})
    with open(get_path_actual(nombre_archivo + ".csv"), "r", encoding="utf-8") as archivo :
        encabezado = archivo.readline().strip("\n").split(",")

        for linea in archivo.readlines():
            standing = {}
            linea = linea.strip("\n").split(",")

            nick,time = linea
            

            standing["nick"] = nick
            standing["time"] = int(time)

            lista.append(standing)
    return lista

def rankings(lista:list):
    """crea un archivo de tipo .CSV filtrando por tipo.

    Args:
        lista (list): _description_
    """

    ordenar_lista_doble(lista,"time","time")
    
    with open(get_path_actual("records" + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista)):
            lista_cargada = ",".join(lista[i]) + "\n"

        for persona in lista:
            values = list(persona.values())
            lista_cargada = []
            for value in values:
                if isinstance(value,int):
                    lista_cargada.append(str(value))
                elif isinstance(value,float):
                    lista_cargada.append(str(value))
                else:
                    lista_cargada.append(value)
            linea = ",".join(lista_cargada) + "\n"
            archivo.write(linea)

def recargapantalla():
    global cuentaPasos
    global x
    


    x_relativa = x % background.get_rect().width #obtengo el ancho del background y lo divido por x
    #x_relativa - background.get_rect().width hace que se reproduzca el fondo en bucle
    SCREEN.blit(background,(x_relativa - background.get_rect().width ,y)) #el (0,0) representa la x y la y
    if x_relativa < WIDTH:
        SCREEN.blit(background,(x_relativa,y))
    x -= 2

