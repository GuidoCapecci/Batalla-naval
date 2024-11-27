import pygame
from funciones import *


ANCHO_VENTANA = 900
ALTO_VENTANA = 600

ancho_boton = 215
alto_boton = 70

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

COLOR_FONDO = (20, 50, 153)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)


dificultad = 40
espaciado = 500 / dificultad

# matriz = inicializar_tablero(10)
# colocar_navio(matriz, "submarino", 4) 
# colocar_navio(matriz, "destructor", 3) 
# colocar_navio(matriz, "crucero", 2) 
# colocar_navio(matriz, "acorazado", 1) 
# tablero = matriz


naves = {
        "submarinos": {4, 1},
        "destructores": {3, 2},
        "cruceros": {2, 3},
        "acorazado": {1, 4}
    }
































# # Confing

# ANCHO_VENTANA = 900
# ALTO_VENTANA = 600
# COLOR_FONDO = (20, 50, 153)


# BLANCO = (255, 255, 255)
# ROJO = (255, 0, 0)

# # Matriz 
# cantidad = 10
# espaciado = 500 / cantidad
#                 # ->   x  ,  y, ancho, alto
# rectangulo_cuadrado = [710, 55, 175, 503]
# rectangulo_cuadrado_2 = [400, 250, 130, 50] # Play
# rectangulo_cuadrado_3 = [400, 305, 130, 50] # Nivel
# rectangulo_cuadrado_4 = [400, 360, 130, 50] # Puntaje
# rectangulo_cuadrado_5 = [400, 415, 130, 50] # Salir



# # boton_play = {"nombre": "Jugar"}