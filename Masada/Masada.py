import pygame
import time
import random

pygame.init()

pygame.mixer.music.load("TheFatRat - Time Lapse.mp3")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)

jew_width = 75

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Shamy's Game")
clock = pygame.time.Clock()

jewImg = pygame.image.load('jew.png')
jewImg = pygame.transform.scale(jewImg,(100,100))
jewImg2 = pygame.image.load('jew2.png')
jewImg2 = pygame.transform.scale(jewImg2,(100,100))
soldierImg = pygame.image.load('soldier.png')
soldierImg = pygame.transform.scale(soldierImg,(100,100))

desert = pygame.image.load('desert.jpeg')
desert = pygame.transform.scale(desert, (800, 600))
desert2 = pygame.image.load('desert3.jpeg')
desert2 = pygame.transform.scale(desert2, (800, 600))
desert3 = pygame.image.load('desert2.jpeg')
desert3 = pygame.transform.scale(desert3, (800, 600))
arrowImg = pygame.image.load('arrow.png')
arrowImg = pygame.transform.scale(arrowImg, (50, 50))
pygame.display.set_icon(jewImg)
pause = False

def arrow(ax, ay):
    gameDisplay.blit(arrowImg, (ax, ay))

def money(mx, my):
    gameDisplay.blit(moneyImg, (mx, my))

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Avoided: " + str(count), True, (0,0,255))
    gameDisplay.blit(text,(0,0))

def life(rip):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Lives: " + str(rip), True, (0,0,255))
    gameDisplay.blit(text,(0,20))

def soldier(thing_startx2, thing_startx3, thing_width, jew_width, x, y, thingx1, thingx2, thingx3, thingy1, thingy2, thingy3, count):
    gameDisplay.blit(soldierImg, (thingx1, thingy1))




def congrats():
    awards = random.randint(1, 3)
    largeText = pygame.font.Font('freesansbold.ttf', 25)
    if awards == 1:
        TextSurf, TextRect = text_objs("Nice!", largeText, black )
    if awards == 2:
        TextSurf, TextRect = text_objs("Good Job!", largeText, black)
    if awards == 3:
        TextSurf, TextRect = text_objs("Zoop!", largeText, black)
    TextRect.center = ( display_width * 0.92, 10)
    gameDisplay.blit(TextSurf, TextRect)


def jew(x,y):
    gameDisplay.blit(jewImg, (x,y))

def jew2(x2, y2):
    gameDisplay.blit(jewImg2, (x2, y2))


def text_objs(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objs(text, largeText)
    TextRect.center = (display_width * 0.5 , display_height * 0.5)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game()


def crash(dodged):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 105)
        smallText = pygame.font.Font('freesansbold.ttf', 35)
        TextSurf, TextRect = text_objs("You Died!", largeText, red)
        TextSurf2, TextRect2 = text_objs("Final Score: " + str(dodged) + "", smallText, blue)
        TextRect2.center = (130 , 20)
        TextRect.center = (display_width * 0.5 , display_height * 0.5)
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        button("Play Again?", 150, 450, 100, 50, green, bright_green, game)
        button("Quit!", 550, 450, 100, 50, red, bright_red, "quit")
        gameDisplay.blit(TextSurf, TextRect)



        pygame.display.update()
        clock.tick(15)

def end():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 105)
        TextSurf, TextRect = text_objs("You Escaped!", largeText, blue)
        TextRect.center = (display_width * 0.5 , display_height * 0.5)
        gameDisplay.blit(TextSurf, TextRect)

        button("Play Again?", 150, 450, 100, 50, green, bright_green, game)
        button("Quit!", 550, 450, 100, 50, red, bright_red, "quit")
        gameDisplay.blit(TextSurf, TextRect)



        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objs(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

def paused():
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        largeText = pygame.font.Font('freesansbold.ttf', 105)
        TextSurf, TextRect = text_objs("Paused", largeText, black)
        TextRect.center = (display_width * 0.5 , display_height * 0.5)
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue!", 150, 450, 100, 50, green, bright_green, game)
        button("Quit!", 550, 450, 100, 50, red, bright_red, quitgame)




        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(desert, (0, 0))
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = text_objs("The Escape From Masada", largeText, red)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Fight!",150,450,100,50,green,bright_green,game)
        button("Give Up?",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def game():
    global pause
    pygame.mixer.music.play(-1)
    mouse = pygame.mouse.get_pos()
    x = (display_width * 0.65)
    y = (display_height * 0.85)
    x2 = (display_width * 0.35)
    y2 = (display_height * 0.85)
    ax = thing_startx1 = random.randrange(0, display_width)
    ay = -600
    a_speed = 5
    a_width = 50
    a_height = 50

    x_change = 0
    y_change = 0
    nice = random.randint(1, 3)
    x2_change = 0
    y2_change = 0

    mx = random.randrange(0, 800)
    my = random.randrange(0, 600)

    thing_startx1 = random.randrange(0, display_width)
    thing_startx2 = random.randrange(0, display_width)
    thing_startx3 = random.randrange(0, display_width)
    thing_starty1 = -600
    thing_starty2 = -600
    thing_starty3 = -600
    thing_speed = 12
    thing_width = 100
    thing_height = 100
    dodged = 20
    rip = 0
    ded = 1

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_UP:
                    y_change = -10
                if event.key == pygame.K_DOWN:
                    y_change = 10
                if event.key == pygame.K_a:
                    x2_change = -10
                if event.key == pygame.K_d:
                    x2_change = 10
                if event.key == pygame.K_w:
                    y2_change = -10
                if event.key == pygame.K_s:
                    y2_change = 10
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    unpause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x2_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y2_change = 0


        x += x_change
        y += y_change
        x2 += x2_change
        y2 += y2_change

        #if y < my+100:
            #if x > mx and x < mx+100 or x+jew_width > mx and x+jew_width < mx+100:
                    #dodged += 0.01
                    #mx == random.randrange(0, 800)
                    #mx == random.randrange(0, 600)
        if dodged > 19:
            gameDisplay.blit(desert3, (0, 0))
        elif dodged > 9:
            gameDisplay.blit(desert2, (0, 0))
        else:
            gameDisplay.blit(desert, (0, 0))


        #(thing_startx2, thing_startx3, thing_width, jew_width, x, y, thingx1, thingx2, thingx3, thingy1, thingy2, thingy3, count)
        #soldier(thing_startx2, thing_starty3, thing_width, jew_width, x, y, thing_startx1, thing_startx2, thing_startx3, thing_starty1, thing_starty2, thing_starty3, dodged)
        thing_starty1 += thing_speed
        thing_starty2 += thing_speed
        thing_starty3 += thing_speed
        ay += a_speed
        jew(x,y)
        jew2(x2, y2)
        #money(mx, my)
        score(dodged)
        #life(rip)

        if x > display_width - 100:
            x = display_width - 100
        if x < 0:
            x = 0

        if y > display_height - 100:
            y = display_height - 100
        #if y < 0:
        #    y = 0

        if x2 > display_width - 100:
            x2 = display_width - 100
        if x2 < 0:
            x2 = 0

        if y2 > display_height - 100:
            y2 = display_height - 100
        #if y2 < 0:
            #y2 = 0
        if thing_starty1 > display_height or thing_starty2 > display_height or thing_starty3 > display_height:
            thing_starty1 = -1000
            thing_starty2 = -1000
            thing_starty3 = -1000

            thing_startx1 = random.randrange(0, display_width)
            thing_startx2 = random.randrange(0, display_width)
            thing_startx3 = random.randrange(0, display_width)

            dodged += 1
            thing_speed += 0.5

            congrats()





            if ay > display_height:
                ay = -200
                ax = random.randrange(0, display_width)
                a_speed += 1








        if y < thing_starty1+thing_height and y > thing_starty1:
            if x > thing_startx1 and x < thing_startx1+thing_width or x+jew_width > thing_startx1 and x+jew_width < thing_startx1+thing_width:
                rip += 1
                x = 0
                y = -1100


        if y2 < thing_starty1+thing_height and y2 > thing_starty1:
            if x2 > thing_startx1 and x2 < thing_startx1+thing_width or x2+jew_width > thing_startx1 and x2+jew_width < thing_startx1+thing_width:
                rip += 1
                x2 = 0
                y2 = -1100


        #if y2 < ay+a_height and y2 > ay:
        #    if x2 > ax + 50 and x2 < ax+a_width or x2+jew_width > ax and x2+jew_width < ax+a_width:
            #    rip += 1
            #    x = 0
                #y = -1100

        #if y < ay+a_height and y > ay:
        #    if x > ax + 50 and x < ax+a_width or x+jew_width > ax and x+jew_width < ax+a_width:
            #    rip += 1
            #    x = 0
            #    y = -1100


        if rip == 2:
            crash(dodged)


            #if x > thing_startx2 and x < thing_startx2+thing_width or x+jew_width > thing_startx2 and x+jew_width < thing_startx2+thing_width:
            #    crash()
            #if x > thing_startx3 and x < thing_startx3+thing_width or x+jew_width > thing_startx2 and x+jew_width < thing_startx3+thing_width:
            #    crash()
        #arrow(ax, ay)
        soldier(thing_startx2, thing_starty3, thing_width, jew_width, x, y, thing_startx1, thing_startx2, thing_startx3, thing_starty1, thing_starty2, thing_starty3, dodged)
        if dodged > 25:
            end()
        pygame.display.update()
        clock.tick(60)

game_intro()
game()
pygame.quit()
quit()
