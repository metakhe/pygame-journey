import pygame
from pygame.locals import Rect


class Player:
    def __init__(self, window, x, y, width, height, speed, sprites):
        self.window = window
        self.rect = Rect(x, y , width, height)
        self.speed = speed

        self.sprites = sprites

        self.is_walking = False
        self.position = "idle"  # ["idle", "walk"]
        self.direction = "down"  # ["left", "up", "right", "down"]
        self.vertical_leg_position = "left"  # [None, "left", "right"]

    def center(self, x, y):
        self.rect.center = (x, y)

    def move(self, direction):

        match direction:
            case "left":
                self.rect.x -= self.speed

                if self.rect.x < 0 - self.rect.width:
                    self.rect.x = self.window.get_width()
            case "up":
                self.rect.y -= self.speed

                if self.rect.y < 0 - self.rect.height:
                    self.rect.y = self.window.get_height()
            case "right":
                self.rect.x += self.speed

                if self.rect.x > self.window.get_width():
                    self.rect.x = 0 - self.rect.width
            case "down":
                self.rect.y += self.speed

                if self.rect.y > self.window.get_height():
                    self.rect.y = 0 - self.rect.width

        self.is_walking = True
        self.direction = direction

    def render(self, image_path):
        image = pygame.transform.scale(
            pygame.image.load(image_path),
            (self.rect.width, self.rect.height)
        )

        self.window.blit(image, self.rect)
