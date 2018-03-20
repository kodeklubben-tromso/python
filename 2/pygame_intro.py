
import pygame
import time

pygame.init()


class Screen:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        self.sc = pygame.display.set_mode( (self.width, self.height) )


sc = Screen(800, 400)

while True:
    time.sleep(20)