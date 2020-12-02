import pygame
#o pygame.init serve para iniciar os módulos do pygame 
pygame.init()
gameExit = False
global maze, size_quad, contour

#matriz que estrutura o labirinto
maze = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 1, 32, 1, 1, 7, 1, 1, 1, 0, 0, 3],
    [3, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 3],
    [3, 1, 0, 0, 5, 4, 0, 0, 1, 1, 1, 3],
    [3, 1, 1, 0, 1, 1, 1, 1, 0, 0, 7, 3],
    [3, 0, 1, 0, 0, 0, 0, 11, 4, 1, 1, 3], 
    [3, 1, 1, 10, 1, 1, 1, 0, 1, 1, 1, 3],
    [3, 1, 1, 4, 0, 1, 0, 12, 4, 0, 7, 3],
    [3, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 3],
    [3, 1, 1, 7, 1, 0, 0, 1, 0, 0, 1, 3], 
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
]

#definição de algumas variáveis importantes
size_quad = 64
contour = (139, 58, 58)
display_width = size_quad * len(maze[0])
display_height = size_quad * len(maze)
contador_perdeu = 0
chao = (255, 255, 255)


#criação de objetos que irão compor a formulação da estrutura do labirinto
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
parede_img = pygame.image.load("parede.png")
chao_img = pygame.image.load("chao.jpg")
livro_img = pygame.image.load("livro.png")
boneca_img = pygame.image.load("boneca.png")

#função que processa a estrutura do labirinto, ou seja, para cada numero correspondente a posição é gerado uma imagem ou um retangulo no caso do contorno
def processar_posicao(surface, posx, posy):
    
    if maze[posx][posy] == 1:
        gameDisplay.blit(parede_img, (posy*size_quad, posx*size_quad))        
        return
    elif maze[posx][posy] == 2 or maze[posx][posy] == 32 or maze[posx][posy] == 8 or maze[posx][posy] == 9:
        gameDisplay.blit(chao_img, (posy*size_quad, posx*size_quad))   
        gameDisplay.blit(boneca_img, (posy*size_quad, posx*size_quad))        
        return
    elif maze[posx][posy] == 3:
        color = contour
        rect = pygame.Rect(posy * size_quad, posx * size_quad, size_quad, size_quad)
        pygame.draw.rect(surface, color, rect)
    elif maze[posx][posy] == 4:
        gameDisplay.blit(chao_img, (posy*size_quad, posx*size_quad))  
        gameDisplay.blit(livro_img, (posy*size_quad, posx*size_quad))        
        return
    elif maze[posx][posy] == 4 or maze[posx][posy] == 5 or maze[posx][posy] == 7 or maze[posx][posy] == 10 or maze[posx][posy] == 11 or maze[posx][posy] == 12:
        gameDisplay.blit(chao_img, (posy*size_quad, posx*size_quad))        
        return
    elif maze[posx][posy] == 6 or maze[posx][posy] == 13 or maze[posx][posy] == 14 or maze[posx][posy] == 15 or maze[posx][posy] == 24 or maze[posx][posy] == 25 :
        gameDisplay.blit(chao_img, (posy*size_quad, posx*size_quad))  
        gameDisplay.blit(boneca_img, (posy*size_quad, posx*size_quad))        
        return       
    else: 
        gameDisplay.blit(chao_img, (posy*size_quad, posx*size_quad))        
        return

#As funções abaixo escrevem na tela as reações a depender da ação do jogador 
def boas_vindas():
    basicFont = pygame.font.SysFont(None, 32)
    text = basicFont.render('Bem-vindo(a) ao Labirinto Literário!', True, chao, contour)    
    gameDisplay.blit(text, (65, 20, 50, 50))

    
def apresentar_texto1():
    basicFont = pygame.font.SysFont(None, 32)
    text = basicFont.render('Machado de Assis escreveu Dom Casmurro? S/N', True, chao, contour)    
    gameDisplay.blit(text, (65, 20, 50, 50))


def apresentar_texto2():
    basicFont = pygame.font.SysFont(None, 32)
    text = basicFont.render('Adélia Prado é uma poetisa brasileira? S/N', True, chao, contour)    
    gameDisplay.blit(text, (65, 20, 50, 50))


def apresentar_texto3():
    basicFont = pygame.font.SysFont(None, 32)
    text = basicFont.render('Gonçalves Dias escreveu a poesia Canção de Exílio? S/N', True, chao, contour)    
    gameDisplay.blit(text, (65, 20, 50, 50))


def apresentar_texto4():
    basicFont = pygame.font.SysFont(None, 32)
    text = basicFont.render('Álvarez de Azevedo escreveu Noite na Taverna? S/N', True, chao, contour)    
    gameDisplay.blit(text, (65, 20, 50, 50))
       

def ganhou():
    basicFont = pygame.font.SysFont(None, 32)
    text = basicFont.render('Você ganhou, parabéns!!', True, chao, contour)
    gameDisplay.blit(text, (65, 20, 50, 50))


def perdeu():
    basicFont = pygame.font.SysFont(None, 32)
    text = basicFont.render('Você perdeu, tente outra vez!!', True, chao, contour)
    gameDisplay.blit(text, (65, 20, 50, 50))

   
def siga_em_frente():
    basicFont = pygame.font.SysFont(None, 32)
    text = basicFont.render('Você acertou, siga em frente!', True, chao, contour)
    gameDisplay.blit(text, (65, 20, 50, 50))


#essa função determina a saída ou a entrada do looping realizado pelo comando while 
def game_loop():
    gameExit = False    
    #o método fill preenche todo o cenário com a cor passada como parâmetro e isso só será feito quando o display.update for chamado
    gameDisplay.fill(chao)


#aqui há o início do laço de repetição
while not gameExit:    

    for event in pygame.event.get():
        #evento determina a saída do jogo quando o usúario aperta o x no canto no topo da tela
        if event.type == pygame.QUIT:
            gameExit = True
        #for para percorrer as linhas da matriz    
        for i in range(len(maze)):
            down = True
            #for para percorrer as colunas da matriz
            for j in range(len(maze[0])):
                #sucessão de eventos que relacionam o número da matriz com imagens ou cores
                if maze[i][j] == 32:
                    boas_vindas()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:  
                            maze[i][j] = 2
                                            
                if event.type == pygame.KEYDOWN and maze[i][j] == 2 or maze[i][j] == 9:
                    if event.key == pygame.K_DOWN:
                        #explicando: se o próximo elemento da matriz for zero, o zero passará a ser 2 e a posição atual, depois do movimento, passa a ser 5.                            
                        if maze[i + 1][j] == 0:
                            maze[i + 1][j] = 2
                            maze[i][j] = 5                                                           
                        if maze[i + 1][j] == 1:
                            maze[i][j] = 2
                        if maze[i + 1][j] == 5:
                            maze[i + 1][j] = 6                                
                            maze[i][j] = 5
                        if maze[i + 1][j] == 10:
                            maze[i + 1][j] = 14
                            maze[i][j] = 5                            
                        if maze[i + 1][j] == 7:
                            maze[i + 1][j] = 8                                                             
                            maze[i][j] = 0                         
                        if  maze[i + 1][j] == 12:                            
                            maze[i + 1][j] = 15
                            maze[i][j] = 5
                                                
                        down = False                            
                        #a cada final de evento eu chamo a função processar_posição para modificar os elementos no cenário e armazenar essas modificações na memória
                        processar_posicao(gameDisplay, i, j)
                            
                    if event.key == pygame.K_UP:
                        if maze[i - 1][j] == 0 or maze[i - 1][j] == 5:
                            maze[i - 1][j] = 2
                            maze[i][j] = 0
                        if maze[i - 1][j] == 1 or maze[i - 1][j] == 4:
                            maze[i][j] = 2
                        if maze[i - 1][j] == 5:
                            maze[i - 1][j] = 6
                            maze[i][j] = 5
                        if maze[i][j] == 9:                                
                            maze[i][j + 1] = 2
                            maze[i][j] = 0
                        if maze[i - 1][j] == 7:
                            maze[i - 1][j] = 8                                                             
                            maze[i][j] = 0
                            
                        processar_posicao(gameDisplay, i, j)
                        break
                    if event.key == pygame.K_RIGHT:
                        if maze[i][j + 1] == 0: 
                            maze[i][j + 1] = 2
                            maze[i][j] = 0                      
                        if maze[i][j + 1] == 5:
                            maze[i][j + 1] = 6
                            maze[i][j] = 0                            
                        if maze[i][j + 1] == 7:
                            maze[i][j + 1] = 8                                                             
                            maze[i][j] = 0   
                        if maze[i][j + 1] == 1:
                            maze[i][j] = 2
                        if maze[i][j + 1] == 11:
                            if maze[i][j + 1] == 1:
                                maze[i][j] = 2
                            else:
                                maze[i][j + 1] = 13
                                maze[i][j] = 0
                                
                        processar_posicao(gameDisplay, i, j)
                        break
                    if event.key == pygame.K_LEFT:
                        if maze[i][j - 1] == 0 or maze[i][j - 1] == 5:
                            maze[i][j - 1] = 2
                            maze[i][j] = 0
                        if maze[i][j - 1] == 1 or maze[i][j - 1] == 4:
                            maze[i][j] = 2                        
                        if maze[i + 1][j] == 7:
                            maze[i + 1][j] = 8                                                             
                            maze[i][j] = 0
                        if maze[i][j] == 9:
                            maze[i][j + 1] = 2
                            maze[i][j] = 0  
                        processar_posicao(gameDisplay, i, j)
                        break                       
                processar_posicao(gameDisplay, i, j)
                        
                if maze[i][j] == 6:                    
                    apresentar_texto2()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            maze[i][j] = 24
                        if event.key == pygame.K_n:
                            maze[i][j] = 2
                            contador_perdeu += 1                        
                                                
                if maze[i][j] == 13:                    
                    apresentar_texto3()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:                           
                            maze[i][j] = 24                                                     
                        if event.key == pygame.K_n:
                            maze[i][j] = 2
                            contador_perdeu += 1 

                if maze[i][j] == 14:                    
                    apresentar_texto4()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:                            
                            maze[i][j] = 25                                                      
                        if event.key == pygame.K_n:
                            maze[i][j] = 2
                            contador_perdeu += 1 

                if maze[i][j] == 25:
                    siga_em_frente()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            maze[i][j] = 9
                            maze[i + 1][j] = 2
                            maze[i][j] = 0
                        down = False

                if maze[i][j] == 15:                    
                    apresentar_texto1()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:                            
                            maze[i][j] = 24                                                      
                        if event.key == pygame.K_n:
                            maze[i][j] = 2
                            contador_perdeu += 1 
                   
                if maze[i][j] == 24:
                    siga_em_frente()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            maze[i][j] = 9
                            maze[i][j + 1] = 2
                            maze[i][j] = 0                     
                        break
                
                if maze[i][j] == 8:
                    ganhou()                                              
                    break   
            if down is not True:
                break

            if contador_perdeu == 4:
                perdeu()
                break     

    #ocorre a atualização de todo o cenário do jogo pois ele recebe o que foi armazenado na memória por meio do objeto Surface (que aqui eu chamei de gameDisplay)          
    pygame.display.update()
    #limita o número máximo de interações por segundo de modo a força-lo a rodar em uma dada velocidade
    clock.tick(40)
game_loop()
pygame.quit()
quit()