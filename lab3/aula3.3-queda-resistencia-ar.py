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

VELOCIDADE = 0

#Cicle
raio = 10
massa = 1.0 #kg
rho = 1.293 #kg/m^3
c = 0.47 #esfera

area = 3.14 * (raio/100) ** 2

g = 9.8
fa = 0.0
v0 = VELOCIDADE
pos_x = 320
pos_y = 10
dt = 0.09
is_launch = False

while True:
    
    #dt = clock.tick(FPS)     
    
    janela.fill((0, 0, 0))
    
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
        
        pygame.draw.circle(janela, COR, (pos_x, pos_y), raio)
        
        #Fa = k * V^2
        
        #k
        k = 0.5 * rho * c * area
        
        #fa
        #fa = k * v0**2
        
        #aceleracao
        a = g - (k * (v0**2/2.0))
        
        #velocidade
        v0 = v0 + a * dt
        
        print(v0)
        
        #
        pos_y = pos_y + v0 * dt + (0.5) * a * dt ** 2
        
    clock.tick(FPS)
                    
    pygame.display.update()
