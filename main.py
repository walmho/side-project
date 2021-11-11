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

#Clock setup
clock = pygame.time.Clock()

def windowSetup():
    global dimensions
    dimensions = (500, 250)
    pygame.display.set_caption("Clickey Clack")
    global window
    window = pygame.display.set_mode(dimensions)
    window.fill(WHITE)

#Since this is my first class I'm going to use more comments than neccesary here:
class gridSquare():
    #Initialize function, run once to define all vars in the object, etc.
    def __init__(self, size=50):
        self.coord = [0, 0]
        self.size = size
        self.movespeed = 1
        #Basically, this makes the var windowsize reference whichever axis is smaller, so the sprite knows when its out of bounds
        if dimensions[0] < dimensions[1]:
            self.windowsize = dimensions[0]
        else:
            self.windowsize = dimensions[1]

    def update(self):
        #Draws a cube using top left coordinate as reference and wanted size
        pygame.draw.polygon(window, BLACK, (
            (self.coord[0], self.coord[1]),
            (self.coord[0]+self.size, self.coord[1]), 
            (self.coord[0]+self.size, self.coord[1]+self.size), 
            (self.coord[0], self.coord[1]+self.size))
        )
        #Updating box position vars
        self.coord = [self.coord[0]+self.movespeed, self.coord[1]+self.movespeed]

        #If bottom right corner of sprite hits the edge of the window, reset coords
        if self.coord[1] > self.windowsize-self.size:
            self.coord = [0, 0]

    def isOver(self):
        # Checks if the mouse is over the box relative to its current position
        pos = pygame.mouse.get_pos()
        if pos >= (self.coord[0], self.coord[1]) and pos <= (self.coord[0]+self.size, self.coord[1]+self.size):
            print("Clicked!")
        elif pos < (self.coord[0], self.coord[1]) and pos > (self.coord[0]+self.size, self.coord[1]+self.size):
            print("Not clicked!")

def gameLoop():
    global window, clock
    #Initializes an instance of gridSquare() class
    square = gridSquare()
    while True:
        #"Resets" Window so square is drawn fresh each time
        window.fill(WHITE)
        #Event check loop
        for event in pygame.event.get():
            #If exit button is clicked
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #If mouse button is clicked:
            if event.type == MOUSEBUTTONUP:
                square.isOver()

        square.update()
        pygame.display.update()
        clock.tick(60)

def main():
    pygame.init()
    windowSetup()
    gameLoop()

if __name__ == "__main__":
    main()
