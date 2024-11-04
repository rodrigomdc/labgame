import pygame
from sys import exit

# Inicializando módulos de Pygame
pygame.init()

# Criando uma janela com o título “Olá, mundo!”
LARGURA = 640
ALTURA = 480 

#Posicao inicial do objeto
pos_x = 0

janela = pygame.display.set_mode((LARGURA, ALTURA))

#Titulo
pygame.display.set_caption("Olá, mundo!")

# Loop do jogo
while True:
    # Checando a ocorrencia de eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        if event.type == pygame.QUIT:
            # Encerrando módulos de Pygame
           pygame.quit()
           exit()
    
    #pox_x vai ser atualizado a cada rodada de loop       
    pygame.draw.circle(janela, 
                     (255, 255, 255),
                     (pos_x, 240),
                     10                     
                     )
    
    pos_x = pos_x + 1
    
    pygame.display.update()
