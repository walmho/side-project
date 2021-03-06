import pygame, sys
from pygame.locals import *
from pygame import *
import time

#Color definition
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
PURPLE = (155, 0, 255)

#Colorlist exludes white for now because it's kind of difficult to spot a white object against white BG
colorList = [BLACK, RED, GREEN, BLUE, YELLOW, PINK, PURPLE]

#Clock setup
clock = pygame.time.Clock()

def windowSetup():
    global dimensions, windowX, windowY
    dimensions = windowX, windowY = (1000, 500)
    pygame.display.set_caption("Clickey Clack")
    global window
    window = pygame.display.set_mode(dimensions)
    window.fill(WHITE)

class spaceShip():
    def __init__(self):
        self.coords = [500, 400]
        self.size = 50
        self.bottomLeft = [self.coords[0]-self.size, self.coords[1]-self.size]
        self.bottomRight = [self.coords[0]+self.size, self.coords[1]-self.size]

    def update(self):
        ship = pygame.draw.polygon(window, PURPLE, (self.coords, self.bottomLeft, self.bottomRight))

def gameLoop():
    global window, clock
    heroShip = spaceShip()

    while True:
        #"Resets" Window so square is drawn fresh each time
        window.fill(WHITE)
        heroShip.update()
        #Event check loop
        for event in pygame.event.get():
            #If exit button is clicked
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

def main():
    pygame.init()
    windowSetup()
    gameLoop()

if __name__ == "__main__":
    main()
