import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (1000,1000)

white = (255,255,255)
black = (  0,  0,  0)

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

ball = pygame.image.load('ball.png')
ball = pygame.transform.scale(ball,(100,100))
ball.set_colorkey(ball.get_at((0,0)), RLEACCEL)

game_display = pygame.display.set_mode(resolution)
pygame.display.set_caption('Ball Vs Block')
game_display.fill(white)
game_display.blit(ball, (500,500))
pygame.display.flip()

while True:
    game_display.fill(white)
    game_display.blit(ball, pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    fpsClock.tick(FPS)
