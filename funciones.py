import pygame
import config
import random

def inicializar_tablero(dificultad:int)->list:
    '''
    Inicializa una matriz vacia y la retorna.
    '''
    matriz = []
    for _ in range(dificultad):
        fila = [0] * dificultad
        matriz += [fila] 

    return matriz

# Mostrar por consola
def mostrar_matriz(matriz:list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],  end=" ")
        print("")


def dibujar_matriz(dificultad:int, ventana, espaciado:int): #Arreglar
    pos_inicio = 200
    pos_y = 55
    for _ in range(dificultad + 1):
        pygame.draw.line(ventana, config.BLANCO, (pos_inicio, 55), (pos_inicio, 555))
        pos_inicio += espaciado
    for _ in range(dificultad + 1):
        pygame.draw.line(ventana, config.BLANCO, (200, pos_y), (700, pos_y))
        pos_y += espaciado

def colocar_navio(matriz:list, tipo_navio:str, cantidad:int):
    """
    Recibe una matriz, un tipo de navio (submarino, destructor, crucero o acorazado)
    y la cantidad de navios que se quiere colocar.
    """

    match tipo_navio:
        case "submarino":
            largo = 1
        case "destructor":
            largo = 2
        case "crucero":
            largo = 3
        case "acorazado":
            largo = 4

    contador_colocados = 0

    while contador_colocados < cantidad:

        fila_inicial = random.randint(0, len(matriz) - (largo))
        columna_inicial = random.randint(0, len(matriz[0]) - (largo))
        orientacion = random.choice(["H", "V"])

        if validar_casilleros(matriz, fila_inicial, columna_inicial, largo, orientacion) == True:
            contador_colocados += 1
            for _ in range(largo):

                matriz[fila_inicial][columna_inicial] = largo

                if orientacion == "H":
                    columna_inicial += 1
                else:
                    fila_inicial += 1
        

def validar_casilleros(matriz:list,fila:int, columna:int, largo:int, orientacion:str):
    """
    recibe una matriz, una fila, una columna, el largo del objeto que se quiere colocar
    y la orientacion del objeto ("H"/"V")
    verifica que todos los espacios necesarios sean del valor 0 y devuelve true.
    si algun casillero es distinto a 0 devuelve false.
    """
    bandera_vacio = True
    contador = 0
    if orientacion == "H" and (columna + largo) < len(matriz[0]):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            columna += 1
            contador += 1

    if orientacion == "V" and (fila + largo) < len(matriz):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            fila += 1
            contador += 1
    
    return bandera_vacio

def dibujar_tablero(ventana, matriz, espaciado, pos_inicial):
    """
    Dibuja la matriz.
    Cada casilla se representa como un rectángulo de un color dependiendo de su valor.
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            valor = matriz[fila][columna]

# Colores según el contenido
            if valor == 0:
                color = (0, 0, 255)  # Azul para el agua
            elif valor == 1:
                color = (128, 128, 128)  # Gris para submarinos
            elif valor == 2:
                color = (255, 0, 0)  # Rojo para destructores
            elif valor == 3:
                color = (0, 255, 0)  # Verde para cruceros
            elif valor == 4:
                color = (255, 255, 0)  # Amarillo para acorazados

            # Calcular posición del rectángulo
            x = pos_inicial[0] + columna * espaciado
            y = pos_inicial[1] + fila * espaciado

            # Dibujar rectángulo
            pygame.draw.rect(ventana, color, (x, y, espaciado - 2, espaciado - 2))

# 4. Puntaje y Estado del Juego
# Faltante:
# Manejo del puntaje en el juego.
# Condiciones de victoria y derrota (e.g., hundir todas las naves).
# Cómo hacerlo:
# Usa un diccionario para rastrear el estado de cada nave y actualiza según los disparos:

# python
# Copiar código
estado_naves = {"submarinos": 4, "destructores": 3, "cruceros": 2, "acorazados": 1}
# Incrementa o decrementa puntajes en la función procesar_disparo:

# python
# Copiar código
def procesar_disparo(tablero, fila, columna, puntaje):
    if tablero[fila][columna] == 1:
        tablero[fila][columna] = 2  # Acertado
        puntaje += 5
        # if nave_hundida(tablero, fila, columna):
        #     puntaje += 10
    elif tablero[fila][columna] == 0:
        tablero[fila][columna] = -1  # Agua
        puntaje -= 1
    return puntaje



# matriz_rectangulos = crear_matriz_rectangulos()



















































# import pygame 
# from config import *
# import random


# def dibujar_matriz(cantidad:int, ventana, espaciado:int):
#     pos_inicio = 200
#     pos_y = 55
#     for _ in range(cantidad + 1):
#         pygame.draw.line(ventana, BLANCO, (pos_inicio, 55), (pos_inicio, 555))
#         pos_inicio += espaciado

#     for _ in range(cantidad + 1):
#         pygame.draw.line(ventana, BLANCO, (200, pos_y), (700, pos_y))
#         pos_y += espaciado

# def crear_matriz(fila:int, columnas:int, desde:int, hasta:int)->list:
#     '''
#     Funcion: crea una matriz 
#     Parametro: Recibe como parametro cant de filas y columnas, y desde que numero hasta que numero tendra
#     Retorno: Retorna una matriz
#     '''
#     matriz = []
    
#     for i in range(fila):
#         fila = []
#         for j in range(columnas):# Aca hicimos una fila  
#             valor = str(random.randint(desde, hasta))
#             fila += [valor]
#         matriz += [fila]
#     return matriz 
        
# def mostrar_matriz(matriz:list)->None:
#     '''
#     Funcion: mostrar una matriz 
#     Parametro: recibe por parametro una matriz y la muestra
#     '''
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             print(matriz[i][j], end=" ")
#         print("")

# def crear_submarinos(filas, columnas, cantidad_de_unos):
#     matriz = []
#     for _ in range(filas):  # Repetir para cada fila
#         matriz.append([0] * columnas)
    
#     colocados = 0
#     while colocados < cantidad_de_unos:
#         fila = random.randint(0, filas - 1)
#         columna = random.randint(0, columnas - 1)
        
#         # Verificar que la posición esté vacía
#         if matriz[fila][columna] == 0:
#             matriz[fila][columna] = 1
#             colocados += 1
    
#     return matriz

# def crear_destructores(filas:int, columnas:int, cantidad_dos:int):
#     #Inicializar la matriz con ceros
#     matriz = []
#     for _ in range(filas):  # Repetir para cada fila
#         matriz.append([0] * columnas)
    
#     colocados = 0
#     while colocados < cantidad_dos:
#         fila = random.randint(0, filas - 1)
#         columna = random.randint(0, columnas - 1)
        
#         # Elegir orientación: horizontal (H) o vertical (V)
#         orientacion = random.choice(["H", "V"])
        
#         if orientacion == "H" and columna + 1 < columnas:  # Verificar que cabe horizontalmente
#             if matriz[fila][columna] == 0 and matriz[fila][columna + 1] == 0:
#                 matriz[fila][columna] = 2
#                 matriz[fila][columna + 1] = 2
#                 colocado = True
        
#         elif orientacion == "V" and fila + 1 < filas:  # Verificar que cabe verticalmente
#             if matriz[fila][columna] == 0 and matriz[fila + 1][columna] == 0:
#                 matriz[fila][columna] = 2
#                 matriz[fila + 1][columna] = 2
#                 colocados += 1

#     return matriz