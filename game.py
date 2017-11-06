import pygame, sys, random, time
from pygame.locals import *

pygame.init()

#Constants
height = 600
width = 600
resolution = (width,height)
blockPos = [(x*(width/10),0) for x in range(10)]

#Colors
white = (255,255,255)
black = (  0,  0,  0)

#Time Frame
FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()

#Loading images
ball = pygame.image.load('ball.png')
block = pygame.image.load('block.png')

ball = pygame.transform.scale(ball,(width/10,width/10))
block = pygame.transform.scale(block, (width/10,width/10))

ball.set_colorkey(ball.get_at((0,0)), RLEACCEL)
block.set_colorkey(block.get_at((0,0)), RLEACCEL)

game_display = pygame.display.set_mode(resolution)
pygame.display.set_caption('Ball Vs Block')
game_display.fill(white)
pygame.display.flip()

class Balls:
    
    numBalls = 0

    def add(self,numBalls):
        obj = game_display.blit(ball, pygame.mouse.get_pos())
        for var in range(numBalls):
            game_display.blit(ball, obj.midleft)
            obj = game_display.blit(ball, obj.midleft)

class Blocks:
    
    blockPos = ()
    numBlocks = 0
    posList = []
    tempList = []
    gen = 0

    def generate(self,numBlocks):
        self.numBlocks = numBlocks
        self.posList = []
        self.tempList = []
        while len(self.tempList) <= self.numBlocks:
            self.gen = random.randint(0,9)
            if self.gen not in self.tempList:
                self.tempList.append(self.gen)

        for var in self.tempList:
            self.posList.append(blockPos[var])
        
        for pos in self.posList:
            game_display.blit(block,pos)
        
    def increaseY(self):
        if self.posList[0][1] < height:
            print "working"
            for var in range(len(self.posList)):
                self.posList[var] = (self.posList[var][0],self.posList[var][1]+(2*height/10))
            for pos in self.posList:
                game_display.blit(block,pos)
        else:
            self.generate(random.randint(1,8))
    
    def checkStuff(self):
        print self.tempList
        print self.posList

b1 = Blocks()
b1.generate(random.randint(1,8))
ba1 = Balls()

while True: #Main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_display.fill(white)
    ba1.add(4)
    b1.increaseY()
    b1.checkStuff()
    pygame.display.flip()
    fpsClock.tick(FPS)
