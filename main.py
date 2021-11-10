import pygame, sys
from pygame.locals import *
from pygame import *

import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def windowSetup():
    dimensions = windowX, windowY = 500, 250
    pygame.display.set_caption("IDK")
    global window
    window = pygame.display.set_mode(dimensions)
    window.fill(WHITE)

class gridSquare():
    def __init__(self, size=50):
        self.coord = (0, 0)
        self.size = size

    def update(self):
        pygame.draw.polygon(window, BLACK, (
            self.coord, 
            (self.coord[0]+self.size, self.coord[1]), 
            (self.coord[0]+self.size, self.coord[1]+self.size), 
            (self.coord[0], self.coord[1]+self.size))
        )

        # self.coord += 5 

    def checkHover(self):
        # for events in pygame.event.get():
        pos = pygame.mouse.get_pos()
        ev = pygame.event.get()
        if pos <= (50, 50):
            print("Hovering!")
        elif pos > (50, 50):
            print("Not hovering!")

def gameLoop():
    global window
    while True:
        window.fill(WHITE)
        square = gridSquare()
        square.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                square.checkHover()

        pygame.display.update()

def main():
    pygame.init()
    windowSetup()
    gameLoop()

if __name__ == "__main__":
    main()
