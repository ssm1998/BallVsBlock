import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (1000,1000)

white = (255,255,255)
black = (  0,  0,  0)

ball = pygame.image.load('ball.png')
ball = pygame.transform.scale(ball,(100,100))
ball.set_colorkey(ball.get_at((0,0)), RLEACCEL)

game_display = pygame.display.set_mode(resolution)
game_display.fill(white)
game_display.blit(ball, (200,200))

pygame.display.set_caption('Ball Vs Block')


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
