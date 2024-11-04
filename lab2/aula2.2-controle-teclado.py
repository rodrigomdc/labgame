import pygame
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
clock = pygame.time.Clock()

step = 1
pos_x = 15
pos_y = 470

# Loop do jogo
while True:
    
    dt = clock.tick(FPS)    
    
    janela.fill((0, 0, 0))
    
    # Checando a ocorrencia de eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        if event.type == pygame.QUIT:
            # Encerrando módulos de Pygame
           pygame.quit()
           exit()
                   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pos_y = pos_y - step
                
            if event.key == pygame.K_DOWN:
                pos_y = pos_y + step
                
            if event.key == pygame.K_RIGHT:
                pos_x  = pos_x + step    
                
            if event.key == pygame.K_LEFT:
                pos_x  = pos_x - step         
                   
    pygame.draw.circle(janela, COR, (pos_x, pos_y), 10)       
            
    if (pos_x > LARGURA or pos_x < 0) or (pos_y >= ALTURA or pos_y < 0):        
        pos_x = 15
        pos_y = 470
                    
    pygame.display.update()
