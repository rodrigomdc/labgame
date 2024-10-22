import pygame
from sys import exit

# Inicializando módulos de Pygame
pygame.init()

# Criando uma janela com o título “Olá, mundo!”
LARGURA = 640
ALTURA = 480 

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
           
    pygame.draw.line(janela, 
                     (0, 255, 0), 
                     (100, 200), 
                     (300, 200), 
                     10)
    pygame.display.update()
    
