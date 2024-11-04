import pygame
import math
from sys import exit

# Inicializando módulos de Pygame
pygame.init()

# Criando uma janela com o título “Olá, mundo!”
LARGURA = 640
ALTURA = 480 
FPS = 60
COR = (255, 255, 0)
janela = pygame.display.set_mode((LARGURA, ALTURA))

#Titulo
pygame.display.set_caption("Olá, mundo!")

pos_x = 0
pos_y = 0


# Loop do jogo
while True:
    
   
    janela.fill((0, 0, 0))    
        
    # Checando a ocorrencia de eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        if event.type == pygame.QUIT:
            # Encerrando módulos de Pygame
           pygame.quit()
           exit()
                   
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()       
            
                            
            pos_x =   pos_mouse[0] 
            pos_y =   pos_mouse[1]   
              
    pygame.draw.circle(janela, COR, (pos_x, pos_y), 10)                     
                       
    pygame.display.update()
