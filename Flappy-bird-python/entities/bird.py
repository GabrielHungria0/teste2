"""
Entidade Bird (Pássaro)
"""

import pygame
from config import SPEED, GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT


class Bird(pygame.sprite.Sprite):

    def __init__(self, resource_facade):
        pygame.sprite.Sprite.__init__(self)

        self.images = resource_facade.get_bird_images()
        self.speed = SPEED
        self.current_image = 0
        self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 6
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.speed += GRAVITY
        self.rect[1] += self.speed

    def bump(self):
        self.speed = -SPEED

    def begin(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
