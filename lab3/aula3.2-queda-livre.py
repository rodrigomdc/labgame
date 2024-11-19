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
VELOCIDADE = 0
g = 9.8
v0 = VELOCIDADE

pos_x = 320
pos_y = 10

is_launch = False

#Funcao de queda livre
def queda_livre(dt, g):
    
    global v0

    #S = v0*t + g(t^2/2)
    y = v0 * dt + (0.5) * g * dt**2

    #v = v0 + g*t
    v0 = v0 + g * dt
    
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

        #S = S0 + v*t + g*(t^2/2)
        pos_y = pos_y + queda_livre(dt * 0.005, g)
        
    if pos_y >= ALTURA:
        pos_x = 320
        pos_y = 10
        v0 = VELOCIDADE
        is_launch = False
                 
    pygame.display.update() 
            
    

    

