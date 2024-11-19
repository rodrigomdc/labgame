import pygame
from sys import exit
from math import sqrt

# Inicializando módulos de Pygame
pygame.init()

# Criando uma janela com o título “Olá, mundo!”
LARGURA = 640
ALTURA = 480 
FPS = 60
COR = (255, 255, 0)
BACKGROUND = (0, 0, 0)

janela = pygame.display.set_mode((LARGURA, ALTURA))

#Titulo
pygame.display.set_caption("Olá, mundo!")
clock = pygame.time.Clock()

#Parâmetros do K
raio = 10
massa = 1.0 #kg
rho = 1.293 #densidade do ar
c = 0.47 #coeficiente de arrasto da esfera

#A = PI * R^2
area = 3.14 * (raio / 100) ** 2  # área de seção transversal em m²


VELOCIDADE = 0
g = 9.8
v0 = VELOCIDADE
adj_dt = 0.009
pos_x = 320
pos_y = 10
is_lauch = False

# Loop do jogo
while True:
    
    dt = clock.tick(FPS)     
    
    janela.fill(BACKGROUND)
    
    pygame.draw.circle(janela, COR, (pos_x, pos_y), 10)
    
    # Checando a ocorrencia de eventos
    for event in pygame.event.get():
        # Se for um evento QUIT
        if event.type == pygame.QUIT:
            # Encerrando módulos de Pygame
           pygame.quit()
           exit()
                   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_lauch:               
                is_lauch = True
                                 
       
    if is_lauch:
                                       
        pygame.draw.circle(janela, COR, (pos_x, pos_y), raio)
        
        #Calculando a forca de arrasto
        k = 0.5 * rho * c * area
        
        #Fa = k * v^2
        fa =  k * v0**2
        
        #Calculando a aceleracao (+ precisa)
        
        #Fr = P - Fa
        fr = (massa * g) - fa  
        
        #F = m * a
        a = fr / massa

        #V = v0 + a * t
        v0 = v0  +  (a * dt) * adj_dt
         
        # S = S0 + v0 * t + a (t^2)/2        
        pos_y = pos_y + (v0 * dt)*adj_dt + (0.5) * a * (dt*adj_dt)**2    
        
        #Velocidade limite
        #Vl = Raiz_Quad ((m * g)/k)
        vl = sqrt((massa * g)/k)
        
        print(f"Velocidade limite: {vl} - Velocidade Atual: {v0}")
     
    #Comentado apenas para visualizar a velocidade estabilizando        
    '''if (pos_y >= ALTURA):        
        pos_x = 320
        pos_y = 10
        is_lauch = False
        v0 = VELOCIDADE'''        
                    
    pygame.display.update()
