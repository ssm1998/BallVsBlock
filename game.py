import pygame, sys, random
from pygame.locals import *

pygame.init()

height = 800
width = 600
resolution = (width,height)

white = (255,255,255)
black = (  0,  0,  0)

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

ball = pygame.image.load('ball.png')
block = pygame.image.load('block.png')

ball = pygame.transform.scale(ball,(width/10,width/10))
block = pygame.transform.scale(block, (width/10,width/10))

ball.set_colorkey(ball.get_at((0,0)), RLEACCEL)
block.set_colorkey(block.get_at((0,0)), RLEACCEL)

game_display = pygame.display.set_mode(resolution)
pygame.display.set_caption('Ball Vs Block')
game_display.fill(white)
game_display.blit(ball, (width/2,height/2))
pygame.display.flip()

class blocks:
    
    blockPos = ()
    numBlocks = 0
    posList = []
    tempList = []
    gen = 0

    def __init__(self,numBlocks):
        self.numBlocks = numBlocks

    def generate(self):
        self.blockPos = [(0,0),(width/10,0),(width/5,0),((3*width)/10,0),((2*width)/5,0),
           (width/2,0),((3*width)/5,0),((7*width)/10,0),((4*width)/5,0),((9*width)/10,0)]
        while len(self.tempList) <= self.numBlocks:
            self.gen = random.randint(0,9)
            if self.gen not in self.tempList:
                self.tempList.append(self.gen)

        for var in self.tempList:
            self.posList.append(self.blockPos[var])

    def drawBlocks(self):
        pygame.display.flip()
        for pos in self.posList:
            game_display.blit(block,pos)
    
    def increaseY(self):
        if self.posList[0][1] < height:
            for var in range(len(self.posList)):
                self.posList[var] = (self.posList[var][0],self.posList[var][1]+(height/10))
    
        

while True:
    game_display.fill(white)
    game_display.blit(ball, pygame.mouse.get_pos())
    x = random.randint(1,8)
    print x
    b1 = blocks(x)
    b1.generate()
    b1.drawBlocks()
    b1.increaseY()
    if b1.posList[0][1] < height:
        print "Deleted"
        del b1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    fpsClock.tick(FPS)
