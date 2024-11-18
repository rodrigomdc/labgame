import pygame
from sys import exit

pygame.init()

#Definir o tamanho da janela
LARGURA = 640
ALTURA = 480

#Parametros
FPS = 60
COR = (255, 255, 0)
BACKGROUND = (0, 0, 0)

#Criar a janela
janela = pygame.display.set_mode((LARGURA, ALTURA))

#Objeto de tempo
clock = pygame.time.Clock()

#Parametros de mobilidade
VELOCIDADE = 40
g = 9.8
v0 = VELOCIDADE
pos_x = 320
pos_y = 470
is_launch = False

#Funcar de lancamento vertical
def lancamento_vertical(dt, g):
    
    global v0
    
    y = v0 * dt + (0.5) * g * dt**2
    
    v0 = v0 - g * dt
    
    return y

while True:
    
    dt = clock.tick(FPS)
    
    janela.fill(BACKGROUND)
    
    #Primeiro desenho do objeto
    pygame.draw.circle(janela, COR, (pos_x, pos_y), 10)
    
    # Checando a ocorrencia de eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        if event.type == pygame.QUIT:
            # Encerrando módulos de Pygame
           pygame.quit()
           exit()
           
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_SPACE and not is_launch:
                is_launch = True
        
    if is_launch:
        pygame.draw.circle(janela, COR, (pos_x, pos_y), 10)
        
        pos_y = pos_y - lancamento_vertical(dt * 0.0005, g)
        
    if pos_y >= ALTURA:
        pos_x = 320
        pos_y = 470
        v0 = VELOCIDADE
        is_launch = False
            
        
    pygame.display.update() 
            
    

    

