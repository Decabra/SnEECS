import pygame, sys
from pygame import *
from pygame.locals import *
import time
import random ##For creating apples randomly
pygame.init()
pygame.font.init()
body_size = 20
font = pygame.font.SysFont(None, 25)
Info = pygame.display.Info()
SCREEN_WIDTH = Info.current_w - body_size
SCREEN_HEIGHT = Info.current_h - body_size
#SCREEN_WIDTH  =  900
#SCREEN_HEIGHT  = 600
#Colors:
hot_red = (180, 0, 0)
light_red = (255, 96, 96)
hot_green = (0, 200, 0)
light_green = (96, 255, 96)
white = (255,255,255)
RED =   (255,   0,   0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
Food_colour = (150, 100, 25)
clock = pygame.time.Clock()
FPS= 60
snakePass = pygame.image.load('logo.jpg')
snakePass = pygame.transform.scale(snakePass, (SCREEN_WIDTH, SCREEN_HEIGHT))
######MUSIC#######
#pygame.mixer.music.load("Game_Music.mp3")
#pygame.mixer.music.play(-1,0.0)
##################
#Initial Constants
#Velocity decides difficulty of game. Is incremented
#when food is eaten
vel = 5
Xvel = 0
Yvel = 0
#background_image = pygame.image.load("SEECS.jpg")
X = SCREEN_WIDTH // 2
Y = SCREEN_HEIGHT // 2
#Setting up Pygame
#Creating the game window
#Setting the background colour to Red ##RBG##
display.set_caption("SnEECS!")
window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.FULLSCREEN)

# To display the message when car crashed
def text_object(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()
def exit():
    pygame.quit()
    quit()

def lose_message(message, color):
    text = font.render(message, True, color)
    window.blit(text, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2])

def button(msg,x,y,w,h,ac,ic,action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                pygame.draw.rect(window, ac, (x, y, w, h))
                if click[0] == 1 and action != None:
                    action()
            else:
                pygame.draw.rect(window, ic, (x, y, w, h))
            smallText = pygame.font.SysFont('simsunnsimsun', 20)
            TextSurf, TextRect = text_object(msg, smallText)
            TextRect.center = (x+(w/2),y+(h/2))
            window.blit(TextSurf, TextRect)
#Menu, produces a traceback when exiting
def menu():
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            window.fill(white)
            window.blit(snakePass, (0,0))
            button('GO!',(3*SCREEN_WIDTH)/20,SCREEN_HEIGHT/1.2,100,50,GREEN,hot_green,game_Loop)
            button('Quit!',(3*SCREEN_WIDTH)/4,SCREEN_HEIGHT/1.2,100,50,RED,hot_red,exit)
            pygame.display.update()
#Draws the snake
def snake(snake_body, body_size):
    for X_and_Y in snake_body:
        body=pygame.draw.rect(window, GREEN, (X_and_Y[0], X_and_Y[1], body_size, body_size))
#Makes all the pixels move about
def game_Loop():
    snake_body = []
    snake_length = 6
    foodX = round(random.randrange(0, SCREEN_WIDTH - body_size) / body_size) * body_size
    foodY = round(random.randrange(0, SCREEN_HEIGHT - body_size) / body_size) * body_size
    ##Round function is used on above variables so that
    ##the food appears in the same line of action S the snake
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                move_Left = event.key == pygame.K_LEFT
                move_Right = event.key == pygame.K_RIGHT
                move_Up = event.key == pygame.K_UP
                move_Down = event.key == pygame.K_DOWN

                ##Changing snake coordinates on key presses
                global X, Y, Xvel, Yvel, vel
                if move_Left:
                    Xvel = -vel
                    Yvel = 0
                if move_Right:
                    Xvel = vel
                    Yvel = 0
                if move_Up:
                    Yvel = -vel
                    Xvel = 0
                if move_Down:
                    Yvel = vel
                    Xvel = 0
        if (X < 0) or (Y < 0) or (X > SCREEN_WIDTH) or (Y > SCREEN_HEIGHT):
            lose_message("You crashed! Try again", BLACK)
            display.update()
            time.sleep(2)
            break
        #window.fill(RED)
        X += Xvel
        Y += Yvel
        #window.blit(background_image, [0, 0])
        pygame.draw.rect(window , Food_colour, [foodX, foodY, body_size, body_size])

        snake_head = []
        snake_head.append(X)
        snake_head.append(Y)
        snake_body.append(snake_head)
        #Eating the apple
        if (abs(X - foodX) < body_size) and (abs(Y - foodY) < body_size):
            foodX = round(random.randrange(0, SCREEN_WIDTH - body_size) / body_size) * body_size
            foodY = round(random.randrange(0, SCREEN_HEIGHT - body_size) / body_size) * body_size
            snake_length += 5
            #global vel
            vel += 1
        if len(snake_body) > snake_length:
            del snake_body[0]
        snake(snake_body, body_size)
        display.update()

        clock.tick(FPS)
        window.fill(BLACK)
menu()
#Executing Program
game_Loop()
