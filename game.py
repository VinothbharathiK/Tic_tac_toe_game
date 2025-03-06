import numpy as np
import pygame
size=(600,600)
white =(255,255,255)
black =(0,0,0)
circle =pygame.image.load("circ.png")
CIRCLE = pygame.transform.scale(circle, (100, 100))
cross =pygame.image.load("cross.png")
CROSS = pygame.transform.scale(cross, (100, 100))


def mark(row,column,player):
    board[row][column] =player
    

def is_empty(row,column):
    return board[row][column] == 0

def full():
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return False
    return True

def draw_image():
    for r in range(3):
        for c in range(3):
            if board[r][c] ==1:
                window.blit(CIRCLE,(c*200+50,r*200+50))
            elif board[r][c] ==2:
                window.blit(CROSS,(c*200+50,r*200+50)) 
    pygame.display.update()

def draw_lines():
    pygame.draw.line(window,black,(200,0),(200,600),5)
    pygame.draw.line(window,black,(400,0),(400,600),5)
    pygame.draw.line(window,black,(0,200),(600,200),5)
    pygame.draw.line(window,black,(0,400),(600,400),5)



def won(player):
    if player ==1 :
        announce = (0, 0, 255)
        
    if player ==2 :
        announce = (255, 0, 0)  

    for r in range(3):
        if board[r][0] ==player and board[r][1]==player and board[r][2]==player :
            
            pygame.draw.line(window,announce,(5,(r*200)+100),(600-10,(r*200)+100),5)
            return True
    for c in range(3):
        if board[0][c] ==player and board[1][c]==player and board[2][c]==player :
            
            pygame.draw.line(window,announce,((c*200+100),5),((c*200)+100,600-10),5)
            return True

    if board[0][0] ==player and board[1][1]==player and board[2][2]==player :
          
            pygame.draw.line(window,announce,(10,10),(590,590),5)
            return True

    if board[0][2] ==player and board[1][1]==player and board[2][0]==player :
            
            pygame.draw.line(window,announce,(590,10),(10,590),5)
            return True        
    




board = np.zeros((3,3))
game_over = False
turn = 0



pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption("Tic tac toe")
window.fill(white)
draw_lines()
pygame.display.update()


 

while not game_over :
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            row=int(event.pos[1]/200)
            col=int(event.pos[0]/200)
            if turn%2 == 0:
               
                if is_empty(row,col):
                    mark(row,col,1)
                    
                    if won(1):
                        game_over=True

                    elif full():
                        game_over=True
                    
                else :
                    turn -=1
            else:
                
                if is_empty(row,col):
                    mark(row,col,2)
                    
                    if won(2):
                        game_over=True
                        
                    elif full():
                        game_over=True

                else :
                    turn -=1

            turn += 1        
           
            
            draw_image()



    if game_over == True:
        print("game over")
        pygame.time.delay(2000)  
        board.fill(0)
        window.fill(white)
        draw_lines()
        draw_image()
        game_over = False
        pygame.display.update()


