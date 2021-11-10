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

class gridSquare(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def update(self):
        pygame.draw.polygon(window, BLACK, ((0, 0), (50, 0), (50, 50), (0, 50), (0, 0)))

    def checkHover(self):
        # for events in pygame.event.get():
        pos = pygame.mouse.get_pos()
        ev = pygame.event.get()
        if pos <= (50, 50):
            print("Hovering!")
        elif pos > (50, 50):
            print("Not hovering!")

def gameLoop():
    while True:
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