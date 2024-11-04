import pygame
from sys import exit

# Inicializando módulos de Pygame
pygame.init()

# Criando uma janela com o título “Olá, mundo!”
LARGURA = 640
ALTURA = 480 

#Posicao inicial do objeto
pos_x = 15
pos_y = 470
step = 1 

janela = pygame.display.set_mode((LARGURA, ALTURA))

#Titulo
pygame.display.set_caption("Olá, mundo!")

clock = pygame.time.Clock()

# Loop do jogo
while True:
    
    janela.fill((0,0,0))
    
    clock.tick(60)
    
    # Checando a ocorrencia de eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        if event.type == pygame.QUIT:
            # Encerrando módulos de Pygame
           pygame.quit()
           exit()
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:  
        pos_x = pos_x - step
    if pygame.key.get_pressed()[pygame.K_RIGHT]: 
        pos_x = pos_x + step
    if pygame.key.get_pressed()[pygame.K_UP]:   
        pos_y = pos_y - step
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        pos_y = pos_y + step
    
    #pox_x vai ser atualizado a cada rodada de loop       
    pygame.draw.circle(janela, 
                     (255, 255, 255),
                     (pos_x, pos_y),
                     10                     
                     )
    
    #pos_x = pos_x + 1
    
    if pos_x > LARGURA:
        pos_x = 0
    
    pygame.display.update()
