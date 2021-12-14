import pygame
from sys import exit
from ball import Ball
import random
from utility import get_angle

pygame.init()


X, Y = 1300, 800
screen = pygame.display.set_mode((X,Y))
clock = pygame.time.Clock()

c_r = 15

#colors
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

ball = 5
balls = []

dog = pygame.image.load("bin/dog.png").convert_alpha()
dog = pygame.transform.scale(dog, (150, 150))

bone = pygame.image.load("bin/bone.png").convert_alpha()
bone = pygame.transform.scale(bone, (70, 60))

fence = pygame.image.load("bin/fence.png").convert_alpha()
fence = pygame.transform.scale(fence, (300, 50))

grass = pygame.image.load("bin/grass.png").convert_alpha()
grass = pygame.transform.scale(grass, (50, 50))

left_fence = pygame.transform.rotate(fence, 90)

grasses = []
num_grass = 20
for i in range(num_grass):
    grasses.append((random.randint(100, X-100), random.randint(100, Y-100)))
    
for i in range(ball):
    balls.append(Ball(X, Y))

while True:
    screen.fill(black)
    for i in range(num_grass):
        screen.blit(grass, grasses[i])
    for i in range(4):
        if i < 3:
            screen.blit(left_fence, (0, 300*i))
            screen.blit(left_fence, (X-50, 300*i))
        screen.blit(fence, (300*i+50, 0))
        screen.blit(fence, (300*i+50, Y-50))

    x, y = pygame.mouse.get_pos()
    screen.blit(bone, (x-20, y-30))
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for i in range(ball):
                balls[i].update_revert()

        if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print("click")
            for i in range(ball):
                balls[i].set_position()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for i in range(ball):
        balls[i].update_vector(x, y)
        balls[i].update_position()
        c_x, c_y = balls[i].get_c()
        color = balls[i].get_color()
        #draw dog
        alpha = get_angle(c_x, c_y, x, y)
        rotated_dog = pygame.transform.rotate(dog, alpha)
        rotated_dog = pygame.transform.flip(rotated_dog, (x < c_x), (c_y < y))
        screen.blit(rotated_dog, (c_x-70, c_y-60))
        #pygame.draw.circle(screen, color, (c_x, c_y), c_r)
    
    clock.tick(30) #FPS

    pygame.display.update()
