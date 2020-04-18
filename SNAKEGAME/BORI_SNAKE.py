import pygame
import time
import random

pygame.init()

#color define
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,190,0)
purple = (255,0,155)
yellow = (255,255,0)
y = (0,155,155)
snakegreen = (10,200,0)
orangebrown = (255,125.5,0)
yellowishgreen = (195,255,0)
pink = (255,0,100)
darkpurple = (185,0,140)
darkblue= (0,0,165)
darkred=(240,0,0)
grey = (180,195,180)
lightpink = (255,99,242)
orange = (255,99,11)
yellowb = (255,230,13)
whiteyellow=(253,255,212)

display_h = int(600)
display_w = int(600)
blocksize = int(10)
applesize = 12
fedinc = 2

# time control
clock = pygame.time.Clock()

gameExit = False

szfont = 'small'

gameDisplay = pygame.display.set_mode((display_h,display_w))
pygame.display.set_caption('Bori Snake')

snakeimg = pygame.image.load('snakehead.png')
starthead = pygame.image.load('snahead.png')
startapple = pygame.image.load('snakeappl2.jfif')
icon = pygame.image.load('snahead22.png')
appleimg = pygame.image.load('snakeappl2py.jpg')
appleimg2 = pygame.image.load('ssnakeapp1py.jpg')
pygame.display.set_icon(icon)

#time.
#font
tinyfont = pygame.font.SysFont("comicsansms",20)
smallfont = pygame.font.SysFont("comicsansms",25)
midfont = pygame.font.SysFont("comicsansms",50)
bigfont = pygame.font.SysFont("comicsansms",85)

randAppleX, randAppleY = randapplegen()

#score show
def scoreshow(score):
    text = smallfont.render("ScOrE: "+str(score), True, grey)
    gameDisplay.blit(text,(0,0))

#paused
def pause():

    paused = True
    screenmessage("PAUSED!!!", orange, y_displace=-150, szfont='big')
    screenmessage("Press 'Space_bar' to continue or 'Quit' to quit...",
                  orange, y_displace=100, szfont='small')
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    paused = False
        #gameDisplay.fill(orange)

        pygame.display.flip()
        clock.tick(5)



def gameintro():

    intro = True

    while intro == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                if event.key == pygame.K_q:
                    print('game quitted')
                    pygame.quit()
                    quit()

        gameDisplay.fill(darkpurple)
        screenmessage('WeLcOmE',green,y_displace=-250,szfont='big')
        screenmessage('TO',yellow,y_displace=-120,szfont='big')
        screenmessage("BOri's SNaKE GAME",y,y_displace=-20,szfont='mid')
        screenmessage('The rules still remain the Same, as on the nokia bla blah blah!!!!!',
                      white,y_displace=110,szfont='tiny' )
        screenmessage("Press 'Space_bar' to play or 'Q' to quit ",orangebrown,y_displace=190,szfont='small')
        screenmessage("Press 'Space_bar' to pause ", orangebrown, y_displace=240, szfont='small')
        gameDisplay.blit(starthead,(30,95))
        gameDisplay.blit(startapple,(450,120))

        pygame.display.flip()
        clock.tick(5)

#text screen1
def text_objects(text,color,szfont):
    if szfont == 'small':
        textsurface =  smallfont.render(text,True,color)
    if szfont == 'mid':
        textsurface =  midfont.render(text,True,color)
    if szfont == 'big':
        textsurface =  bigfont.render(text,True,color)
    if szfont == 'tiny':
        textsurface =  tinyfont.render(text,True,color)
    return textsurface, textsurface.get_rect()

#text screen2
def screenmessage( msg,color,x_displace=0,y_displace=0,szfont='small'):
    textscreen, textrect = text_objects(msg,color,szfont)
    #screentext = font.render(msg,True,color)
    #gameDisplay.blit(screentext, [display_w/2,display_h/2])
    textrect.center = (int(display_w/2+x_displace), int(display_h/2+y_displace))
    gameDisplay.blit(textscreen,textrect)


# game over display
def gameoverdisplay(countcol,tdisp,hit,score):
    if hit == 1:
        yourerror='You ate youself'
    elif hit == 2:
        yourerror = 'You hit the boundary'

    gameDisplay.fill(countcol)
    screenmessage('GAME OVER', tdisp,y_displace=-250,szfont='big')
    screenmessage('ScOrE :'+str(score), tdisp, y_displace=-150, szfont='mid')
    screenmessage(yourerror,tdisp,y_displace=-30,szfont='small')
    screenmessage('click "Space_bar",To Play Again, or "Q" to Quit', tdisp, y_displace=70, szfont='small')
    screenmessage('...SMH!!!...', tdisp, y_displace=150, szfont='big')
    pygame.display.update()


# apple make
def randapplegen():
    randAppleX = round(random.randrange(0, display_w - applesize) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_h - applesize) / 10.0) * 10.0
    return randAppleX,randAppleY



# snake graphics
def snake(snakelist, blocksize,snakeLen):

    #snake head direction
    if headdirect == 'right':
        head = pygame.transform.rotate(snakeimg,270)
    if headdirect == 'left':
        head = pygame.transform.rotate(snakeimg,90)
    if headdirect == 'up':
        head = pygame.transform.rotate(snakeimg,0)
    if headdirect == 'down':
        head = pygame.transform.rotate(snakeimg,180)

    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))

    for xny in snakelist[:-1]:
        if snakeLen < 2:
            for xny in snakelist[1:-1]:
                pygame.draw.rect(gameDisplay, snakegreen, [xny[0], xny[1], blocksize, blocksize])


        if snakeLen >= 2:

            pygame.draw.rect(gameDisplay, snakegreen, [snakelist[0][0],snakelist[0][1], blocksize, blocksize])

            for xny in snakelist[1:-1]:
                if snakelist.index(xny)%3==0:
                    colora = yellowishgreen
                elif  snakelist.index(xny)%3==1:
                    colora =  snakegreen
                elif  snakelist.index(xny)%3==2:
                    colora =yellowishgreen
                #elif  snakelist.index(xny)%3==3:
                    colora = yellow
                #elif  snakelist.index(xny)%5==4:
                    #colora =  yellow
                pygame.draw.rect(gameDisplay, colora, [xny[0], xny[1], int(blocksize), int(blocksize)])

#game loop
def gameloop():

    # coordinates
    lead_x = display_w / 2
    lead_y = display_h / 2
    lead_x_change = 10
    lead_y_change = 0
    randAppleX, randAppleY = randapplegen()

    #variables declaration
    global headdirect
    headdirect = 'right'
    gameExit = False
    gameOver = False
    snakelist = []
    snakeLength = 1
    eat = 0
    fps = 10
    score = 0

    #while loop
    while gameExit == False:

        if eat == 1:
            eat =  0
            snakeLength += 1
            fps += 1
        # KEYS
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit = True
            #print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    headdirect = 'left'
                    lead_x_change = -blocksize
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    headdirect = 'right'
                    lead_x_change = blocksize
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    headdirect = 'up'
                    lead_y_change = -blocksize
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    headdirect = 'down'
                    lead_y_change = blocksize
                    lead_x_change = 0
                elif event.key == pygame.K_SPACE:
                    pause()

#            if event.type == pygame.KEYUP:
#                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                    lead_x_change = 0
#                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                    lead_y_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change


        #pygame.draw.rect(gameDisplay, yellow,[randAppleX,randAppleY,blocksize,blocksize])
        gameDisplay.fill(whiteyellow)
        #pygame.draw.rect(gameDisplay, black, [400,300,10,-50])
        # pygame.draw.rect(gameDisplay, red, [400, 300, -100, -10])
        # gameDisplay.fill(orange,rect=[200,200,50,20])
        #pygame.draw.rect(gameDisplay,pink,[randAppleX, randAppleY,applesize ,applesize])

        #apple draw
        gameDisplay.blit(appleimg2,(int(randAppleX),int(randAppleY)))
        #snake define
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakeLength:
            del snakelist[0]

        #hit
        for xny in snakelist[:-1]:
            if xny == snakehead[:-2]:
                gameOver = True
                hit = 1
      #if snakehead[-1] == snakehead[-2]:
      #    lead_x -= lead_x_change
      #    lead_y -= lead_y_change
      #    lead_x_change = 0
      #    lead_y_change = 0
        #snake draw
        snake(snakelist, blocksize,snakeLength)
        #hit2
        if lead_x >= display_w or lead_x < 0 or lead_y >= display_h or lead_y < 0:
            gameOver = True
            hit = 2
            clock.tick(0)
        #eat1
        if lead_x >= randAppleX  and lead_y >= randAppleY and lead_x < randAppleX+blocksize  and lead_y < randAppleY+blocksize:
            eat += 1
            print("om nom nom")
            randAppleX ,randAppleY = randapplegen()
        #eat2
        if lead_x > randAppleX and lead_x < randAppleX + applesize or lead_x + blocksize > randAppleX and lead_x+blocksize< randAppleX+applesize:

            if  lead_y > randAppleY and lead_y <randAppleY+applesize:
                eat += 1
                score += 2
                print("om nom nom")
                randAppleX, randAppleY = randapplegen()

            elif lead_y + blocksize > randAppleY and lead_y + blocksize < randAppleY + applesize:
                 eat += 1
                 score += 2
                 print("om nom nom")
                 randAppleX, randAppleY = randapplegen()

        scoreshow(score)
        count = 0
        while gameOver == True:
            loopnum = 10
            tal = count%loopnum
            if tal < loopnum/2 :
                countcol = red
                tdisp = whiteyellow
            elif tal >= loopnum/2:
                countcol = whiteyellow
                tdisp = darkred
            gameoverdisplay(countcol,tdisp,hit,score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        print("restarted")
                        gameOver=False
                        gameloop()
                        pygame.display.flip()

            time.sleep(0.1)
            count+=1
            pygame.display.flip()

            #gameDisplay.fill(white)
            ##pygame.display.flip()
            #time.sleep(3)


        clock.tick(fps)
        #time.sleep(.1)
        pygame.display.flip()

    print('\nGAME OVER')
    #pygame.display.flip()
    #time.sleep(2)
    pygame.quit()
    #quit()


#gameDisplay.fill(white)
#pygame.display.flip()
#gameintro()
#gameloop()


