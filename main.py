








import pygame
from funciones import *
from config import *
import pygame.mixer as mixer



pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
# mixer.music.play()

icono = pygame.image.load("Segundo_parcial_grupo.py\Archivos/fondo_agua.jpg")
pygame.display.set_icon(icono)

pygame.display.set_caption("Batalla Naval")

fondo_principal = pygame.image.load("Segundo_parcial_grupo.py\Archivos/fondo_agua.jpg")
fondo_principal = pygame.transform.scale(fondo_principal, (ANCHO_VENTANA, ALTO_VENTANA))

fondo = pygame.image.load("Segundo_parcial_grupo.py\Archivos\imagen_mar.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

fondo_puntajes = pygame.image.load("Segundo_parcial_grupo.py\Archivos\imagen_puntaje.jpg")
fondo_puntajes = pygame.transform.scale(fondo_puntajes, (ANCHO_VENTANA, ALTO_VENTANA))



# mixer.music.load("assets\\sounds\\musica_fondo.mp3")
# ruido_bala = mixer.Sound("assets\\sounds\\Efecto_disparo.mp3")
# ruido_bala.set_volume(0.3)

imagen_nivel = pygame.image.load("Segundo_parcial_grupo.py\Archivos\imagen_nivel.jpg")
imagen_jugar = pygame.image.load("Segundo_parcial_grupo.py\Archivos\imagen_jugar.jpg")
imagen_puntaje = pygame.image.load("Segundo_parcial_grupo.py\Archivos\imagen_puntaje.jpg")
imagen_salir = pygame.image.load("Segundo_parcial_grupo.py\Archivos\imagen_salir.jpg")
imagen_reiniciar = pygame.image.load("Segundo_parcial_grupo.py\Archivos\imagen_nivel.jpg") #ESTE ESTA MAL

imagen_nivel = pygame.transform.scale(imagen_nivel, (ancho_boton, alto_boton))
imagen_jugar = pygame.transform.scale(imagen_jugar, (ancho_boton, alto_boton))
imagen_puntaje = pygame.transform.scale(imagen_puntaje, (ancho_boton, alto_boton))
imagen_salir = pygame.transform.scale(imagen_salir, (ancho_boton, alto_boton))
imagen_reiniciar = pygame.transform.scale(imagen_reiniciar, (ancho_boton - 60, alto_boton - 20))




boton_jugar = imagen_jugar.get_rect()
boton_jugar.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_jugar.y = (ALTO_VENTANA / 6)

boton_nivel = imagen_nivel.get_rect()
boton_nivel.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_nivel.y = (ALTO_VENTANA / 3)

boton_puntaje = imagen_puntaje.get_rect()
boton_puntaje.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_puntaje.y = (ALTO_VENTANA / 2)

boton_salir = imagen_salir.get_rect()
boton_salir.x = (ANCHO_VENTANA / 2 - ancho_boton / 2)
boton_salir.y = (ALTO_VENTANA - ALTO_VENTANA / 3)

boton_volver = imagen_reiniciar.get_rect()
boton_volver.x = 10
boton_volver.y = 460

boton_reiniciar = imagen_reiniciar.get_rect()
boton_reiniciar.x = 10
boton_reiniciar.y = 515


bandera_pantallas = 0

corriendo = True
bandera = True

while corriendo == True:

    if bandera_pantallas == 0:
        ventana.blit(fondo_principal, (0, 0))
        ventana.blit(imagen_jugar, boton_jugar)
        ventana.blit(imagen_nivel, boton_nivel)
        ventana.blit(imagen_puntaje, boton_puntaje)
        ventana.blit(imagen_salir, boton_salir)

    elif bandera_pantallas == 1:        #click en boton jugar
        ventana.blit(fondo, (0, 0))
        ventana.blit(imagen_reiniciar, boton_reiniciar)
        ventana.blit(imagen_reiniciar, boton_volver)
        #dibujar_matriz(dificultad, ventana, espaciado) 
    
    elif bandera_pantallas == 2:        #click en boton ver puntajes
        ventana.blit(fondo_puntajes, (0, 0))
        ventana.blit(imagen_reiniciar, boton_volver)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                corriendo = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            if bandera_pantallas == 0:
                if boton_salir.collidepoint(pos_mouse):
                    corriendo = False

                elif boton_jugar.collidepoint(pos_mouse):
                    bandera_pantallas = 1 
                
                elif boton_puntaje.collidepoint(pos_mouse):
                    bandera_pantallas = 2
        
            elif bandera_pantallas == 1:
                if boton_reiniciar.collidepoint(pos_mouse):   # resetear barcos
                    pass
                elif boton_volver.collidepoint(pos_mouse):
                    bandera_pantallas = 0
            
                

        # mixer.music.set_volume(10)
        

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     ruido_bala.play()

        # pygame.draw.line(ventana, ROJO, (200, 0), (200, ALTO_VENTANA))
        # pygame.draw.line(ventana, ROJO, (ANCHO_VENTANA - 200, 0), (ANCHO_VENTANA - 200, ALTO_VENTANA))

    
    pygame.display.flip()

pygame.quit()
















































# # main -> xq aca es donde se ejecuta.
# from funciones import *
# import pygame
# from config import *
# import pygame.mixer as mixer



# pygame.init()
# pygame.mixer.init()


# ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
# pygame.display.set_caption("Batalla Naval")


# fondo_azul = pygame.image.load("Segundo_parcial_grupo.py/fondo_agua.jpg")
# fondo_azul = pygame.transform.scale(fondo_azul, (ANCHO_VENTANA, ALTO_VENTANA))


# imagen_logo = pygame.image.load("Segundo_parcial_grupo.py\logo_barco.jpg")
# pygame.display.set_icon(imagen_logo)

# fondo = pygame.image.load("Segundo_parcial_grupo.py/fondo_barco.jpg")
# fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

# # mixer.music.load("Clase_19/audio_baat_naval.mp3")
# # mixer.music.play()

# # sonido_efecto = pygame.mixer.Sound("Clase_19/sonido-agua-gota.mp3")
# # sonido_efecto.set_volume(0.2)

# boton_play = pygame.Rect(400, 250, 130, 50)
# boton_nivel = pygame.Rect(400, 305, 130, 50)
# boton_puntaje = pygame.Rect (400, 360, 130, 50)
# boton_salir = pygame.Rect(400, 415, 130, 50)

# fuente = pygame.font.Font(None, 25)


# corriendo = True
# contador = 0

# while corriendo == True:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             corriendo = False
#         if evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_q: # Esto es para que apretando "q" cierre la ventana
#                 corriendo = False
     
#         if evento.type == pygame.MOUSEBUTTONDOWN:
#             posicion = (evento.pos)
#             print(posicion)

#         if evento.type == pygame.MOUSEBUTTONDOWN:
#             fondo_azul.set_alpha(0,0)
#         # if evento.type == pygame.MOUSEBUTTONDOWN:
#             # sonido_efecto.play()
           

    
    
    
#     ventana.blit(fondo, (0, 0))


#     dibujar_matriz(cantidad, ventana, 50)
#     pygame.draw.rect(ventana, (0, 0, 0), rectangulo_cuadrado, width=2, border_radius=7)



#     ventana.blit(fondo_azul, (0,0))
#     pygame.draw.rect(ventana, (46, 64, 83),boton_play,0)
#     pygame.draw.rect(ventana, (46, 64, 83), boton_puntaje,0)
#     pygame.draw.rect(ventana, (46,64,83), boton_nivel,0 )
#     pygame.draw.rect(ventana, (46, 64, 83),boton_salir,0)
#     mensaje_play = fuente.render("Play", True, (255,255,255))
#     mensaje_nivel = fuente.render("Nivel", True, (255,255,255))
#     mensaje_puntaje = fuente.render("Puntaje", True, (255,255,255))
#     mensaje_salir = fuente.render("Salir", True, (255,255,255))
#     ventana.blit(mensaje_play, boton_play)
#     ventana.blit(mensaje_nivel, boton_nivel)
#     ventana.blit(mensaje_puntaje, boton_puntaje)
#     ventana.blit(mensaje_salir, boton_salir)

#     if evento.type == pygame.MOUSEBUTTONDOWN:
#         fondo_azul.set_alpha(0,0)

#     mixer.music.set_volume(20)
#     pygame.display.flip()
