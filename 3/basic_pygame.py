
import pygame
import sys

pygame.init()

class Screen:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        self.sc = pygame.display.set_mode( (self.width, self.height) )
    
    # Everything above is from course 2
    # That should be everyones starting point
    def draw(self, objects):
        # Call all draw functions on the objects in the given list
        for obj in objects:
            obj.draw(self.sc)

class Ball:
    def __init__(self, x=200, y=300):
        # Position can be a list of two coordinates
        self.pos = [x, y]
        self.radius = 3
        self.color = (255, 255, 255)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

class Game:
    def __init__(self):
        self.screen = Screen(800, 600)
        self.objects = []

        # All objects to be drawn should be added to the objects list
        # The objects needs to have a draw(screen) function
        self.objects.append(Ball())


    def event_handler(self):
        # Go through all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def run(self):

        while True:
            self.screen.draw(self.objects)
            self.event_handler()

            pygame.display.flip()


if __name__ == "__main__":
    g = Game()
    g.run()
