
import pygame
import sys

pygame.init()


# https://github.com/kodeklubben-tromso/python/

class Screen:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        self.sc = pygame.display.set_mode( (self.width, self.height) )
    
    # Everything above is from course 2
    # That should be everyones starting point
    def draw(self, objects):

        self.sc.fill(0)
        # Call all draw functions on the objects in the given list
        for obj in objects:
            obj.draw(self.sc)

class Ball:
    def __init__(self, x=200, y=300):
        # Position can be a list of two coordinates
        self.pos = [x, y]
        self.radius = 3
        self.color = (255, 255, 255)
        self.speed = 10

    def move(self, buttons):

        if buttons["Up"]:
            self.pos[1] -= self.speed
        if buttons["Down"]:
            self.pos[1] += self.speed
        if buttons["Left"]:
            self.pos[0] -= self.speed
        if buttons["Right"]:
            self.pos[0] += self.speed
    
     
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

class Game:
    def __init__(self):
        self.screen = Screen(800, 600)
        self.objects = []

        self.buttons = {"Up": False, "Down": False, "Left": False, "Right": False}

        # All objects to be drawn should be added to the objects list
        # The objects needs to have a draw(screen) function
        self.objects.append(Ball())


    def event_handler(self):
        # Go through all events

        pressed = pygame.key.get_pressed()
        self.buttons["Up"] = pressed[pygame.K_w]
        self.buttons["Left"] = pressed[pygame.K_a]
        self.buttons["Right"] = pressed[pygame.K_d]
        self.buttons["Down"] = pressed[pygame.K_s]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    def move(self):

        for obj in self.objects:
            obj.move(self.buttons)

        self.buttons["Up"] = False
        self.buttons["Left"] = False
        self.buttons["Right"] = False
        self.buttons["Down"] = False

    def run(self):

        while True:

            self.move()
            self.screen.draw(self.objects)
            self.event_handler()

            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    g = Game()
    g.run()