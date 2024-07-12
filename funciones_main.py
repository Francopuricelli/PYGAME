import pygame
from settings import *
from class_player import *
from class_enemy import *
from class_disparos import *
import random
background = pygame.image.load("src/imagenes/backgroundcronichles1.png")

def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

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
            print(linea, lista,encabezado)

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
    x -= 0





def barra_hp(surface, x, y, vida)-> None:
    largo= 200
    ancho= 15
    calculo_largo_barra= int((vida / 100) * largo) # se calcula la longitud del largo de la barra como porcentaje
    borde = pygame.Rect(x,y, calculo_largo_barra, ancho)
    rectangulo= pygame.Rect(x, y, calculo_largo_barra, ancho)

    pygame.draw.rect(surface, (80, 100, 55), rectangulo)
    pygame.draw.rect(surface, (0, 0, 0), borde, 3)

    if vida <= 50:
        pygame.draw.rect(surface, (255, 160, 0), rectangulo)
        pygame.draw.rect(surface, (0, 0, 0), borde, 3)
    if vida <= 10:
        pygame.draw.rect(surface, (255, 40, 0), rectangulo)
        pygame.draw.rect(surface, (0, 0, 0), borde, 3)



def crear_enemigos_aleatorios(enemigos,cantidad_min, cantidad_max,width):
    cantidad_enemigos = random.randint(cantidad_min, cantidad_max)
    for _ in range(cantidad_enemigos):
        enemigo = Enemies()
        enemigo.rect.x = random.randint(1500, width - enemigo.rect.width)
        enemigos.add(enemigo)



def mostrar_nicks_tabla(lista:list):
    """muestras los ciclistas de la coleccion

    Args:
        lista (list): recibe una lista de diccionarios y los  muestra las claves del campo solicitado
    """
    if isinstance(lista,list):

        tam = len(lista)
        print("                      LISTA DE CICLISTAS")
        print("ID     User           likes        dislikes       followers ")
        print("------------------------------------------------------------------------")
        for user in lista:
            print(f"{user["nick"]}    {user["time"]:15}")   
    else:
        raise ValueError("No se ingreso ninguna lista")
