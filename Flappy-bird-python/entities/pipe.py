"""
Entidade Pipe (Cano)
"""
import pygame
from config import PIPE_WIDHT, PIPE_HEIGHT, SCREEN_HEIGHT, GAME_SPEED


class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, inverted, xpos, ysize, resource_facade):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = resource_facade.get_image('pipe')
        self.image = pygame.transform.scale(self.image, (PIPE_WIDHT, PIPE_HEIGHT))
        
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = -(self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_HEIGHT - ysize
        
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        self.rect[0] -= GAME_SPEED