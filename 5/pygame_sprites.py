
import pygame
import sys
import os
import time

pygame.init()


# https://github.com/kodeklubben-tromso/python/

IDLE_SPRITE_PATH = "animations/idle/"
RUN_SPRITE_PATH = "animations/run/"
TRANSPARENT_COLOR = (16, 129, 128)

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

        self.animation_type = "Idle"
        self.direction = "Left"
        self.animation_frame = 0

        self.animation_speed = 100
        self.last_frame = int(round(time.time() * 1000))

        idle_images_right = []
        idle_images_left = []
        run_images_right = []
        run_images_left = []

        for img in os.listdir(IDLE_SPRITE_PATH):
            image = pygame.image.load(os.path.join(IDLE_SPRITE_PATH, img)).convert()
            image.set_colorkey(image.get_at((0,0)))

            idle_images_right.append(image)
            idle_images_left.append(pygame.transform.flip(image, True, False))

        for img in os.listdir(RUN_SPRITE_PATH):
            image = pygame.image.load(os.path.join(RUN_SPRITE_PATH, img)).convert()
            image.set_colorkey(image.get_at((0,0)))

            run_images_right.append(image)
            run_images_left.append(pygame.transform.flip(image, True, False))

        self.images = {"Idle": {"Left": idle_images_left, "Right": idle_images_right }, "Run": {"Left": run_images_left , "Right": run_images_right}}

    def move(self, buttons):

        if not buttons["Left"] and not buttons["Right"]:
            if self.animation_type is not "Idle":
                self.animation_frame = 0
            self.animation_type = "Idle"
            return

        if buttons["Left"]:

            self.pos[0] -= self.speed
            self.animation_type = "Run"
            self.direction = "Left"

        if buttons["Right"]:
            self.pos[0] += self.speed
            self.animation_type = "Run"
            self.direction = "Right"


    def draw(self, screen):
        animation = self.images[self.animation_type][self.direction]
        if self.animation_frame >= len(animation):
            self.animation_frame = 0

        img = animation[self.animation_frame]
        imgrect = img.get_rect()
        imgrect.center = (self.pos[0], self.pos[1])
        screen.blit(img, imgrect)

        if int(round(time.time() * 1000)) - self.last_frame > self.animation_speed:
            self.last_frame = int(round(time.time() * 1000))
            self.animation_frame += 1

class Game:
    def __init__(self):
        self.screen = Screen(800, 600)
        self.objects = []

        self.buttons = {"Left": False, "Right": False}

        # All objects to be drawn should be added to the objects list
        # The objects needs to have a draw(screen) function
        self.objects.append(Ball())


    def event_handler(self):
        # Go through all events

        pressed = pygame.key.get_pressed()
        self.buttons["Left"] = pressed[pygame.K_a]
        self.buttons["Right"] = pressed[pygame.K_d]

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