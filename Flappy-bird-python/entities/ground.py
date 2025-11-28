"""
Entidade Ground (Chão)
"""

import pygame
from config import GROUND_WIDTH, GROUND_HEIGHT, SCREEN_HEIGHT, GAME_SPEED


class Ground(pygame.sprite.Sprite):

    def __init__(self, xpos, resource_facade):
        pygame.sprite.Sprite.__init__(self)

        self.image = resource_facade.get_image("ground")
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED
