import pygame 
from random import randint

#Dimenisons
WW = 400+20
WH = 400+30+50

#Colours
WHITE  = (255,255,255)
GREY   = (128,128,128)
GREEN1 = (0,128,0)
GREEN2 = (0,255,0)
RED1   = (128,0,0)
RED2   = (255,0,0)

pygame.init()
win = pygame.display.set_mode((WW,WH))
win.fill(WHITE)
font = pygame.font.SysFont('Calibri bold', 60)

positions = [(3,10),(4,10),(5,10)]
food = [8,15]
dire = 'r'
Score = 0

GameOver = False

def print_grid():
    global food
    global GameOver
    global positions
    
    win.fill(WHITE)
    if GameOver == False:
        pygame.draw.rect(win,GREY,pygame.Rect(10,70,400,400))
        pygame.draw.rect(win,GREY,pygame.Rect(10,10,400,50))
        
        ts = ('SCORE : '+str(Score))
        ts_text = font.render(ts,True,WHITE)
        ts_text_rect = ts_text.get_rect()
        ts_text_rect[0] += 100
        ts_text_rect[1] += 20
        win.blit(ts_text,ts_text_rect)
        
        pygame.draw.rect(win,RED1,pygame.Rect(10+food[0]*20,70+food[1]*20,20,20))
        pygame.draw.rect(win,RED2,pygame.Rect(10+food[0]*20,70+food[1]*20,20,20),2)
        for n in positions:
            pygame.draw.rect(win,GREEN1,pygame.Rect(10+n[0]*20,70+n[1]*20,20,20))
            pygame.draw.rect(win,GREEN2,pygame.Rect(10+n[0]*20,70+n[1]*20,20,20),2)
            
    elif GameOver == True:
        pygame.draw.rect(win,GREY,pygame.Rect(10,10,400,460))
        ta = ("GAME")
        tb = ("OVER")
        ts = ('SCORE : '+str(Score))
        ts_text = font.render(ts,True,WHITE)
        ta_text = font.render(ta,True,WHITE)
        tb_text = font.render(tb,True,WHITE)
        ts_text_rect = ts_text.get_rect()
        ts_text_rect[0] += 100
        ts_text_rect[1] += 300
        ta_text_rect = ts_text.get_rect()
        ta_text_rect[0] += 100
        ta_text_rect[1] += 150
        tb_text_rect = ts_text.get_rect()
        tb_text_rect[0] += 100
        tb_text_rect[1] += 200
        win.blit(ts_text,ts_text_rect)
        win.blit(ta_text,ta_text_rect)
        win.blit(tb_text,tb_text_rect)
        
def gen_food():
    global positions
    
    x = randint(0,19)
    y = randint(0,19)
    if [x,y] in positions:
        gen_food()
    return [x,y]

def next_move():
    global positions
    global food
    global dire
    global GameOver
    global Score
    
    h = positions[-1] #head
    next_pos = []
    
    if dire == 'l':next_pos = [(h[0]-1),(h[1])]
    elif dire == 'r':next_pos = [(h[0]+1),(h[1])]
    elif dire == 'u':next_pos = [(h[0]),(h[1]-1)]
    elif dire == 'd':next_pos = [(h[0]),(h[1]+1)]
    elif dire == None:pass
    
    if (next_pos[0] == -1) or (next_pos[1] == -1) or (next_pos[0] == 20) or (next_pos[1] == 20):
        GameOver = True
    
    if next_pos in positions:
        GameOver = True
    else:positions.append(next_pos)

    if next_pos == food:
        food = gen_food()
        Score += 1
    elif next_pos != food:
        positions=positions[1:]
    
clock = pygame.time.Clock()
run = True
while run == True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        run = False
    if event.type == pygame.KEYDOWN:
        if ((event.key == pygame.K_w) or (event.key == pygame.K_UP)) and (dire != 'd'):dire = 'u'
        elif ((event.key == pygame.K_a) or (event.key == pygame.K_LEFT)) and (dire != 'r'):dire = 'l'
        elif ((event.key == pygame.K_s) or (event.key == pygame.K_DOWN)) and (dire != 'u'):dire = 'd'
        elif ((event.key == pygame.K_d) or (event.key == pygame.K_RIGHT)) and (dire != 'l'):dire = 'r'
            
    next_move()
    print_grid()
    clock.tick(8)
    pygame.display.update()
pygame.quit()