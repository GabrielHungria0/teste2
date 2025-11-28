"""
Entidade MovingPipe (Cano que se move verticalmente)
"""
import pygame
from config import PIPE_WIDHT, PIPE_HEIGHT, SCREEN_HEIGHT, GAME_SPEED


class MovingPipe(pygame.sprite.Sprite):
    
    def __init__(self, inverted, xpos, ysize, resource_facade, movement_range=50, movement_speed=2):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = resource_facade.get_image('pipe')
        self.image = pygame.transform.scale(self.image, (PIPE_WIDHT, PIPE_HEIGHT))
        
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.initial_y = -(self.rect[3] - ysize)
        else:
            self.initial_y = SCREEN_HEIGHT - ysize
        
        self.rect[1] = self.initial_y
        
        # Configurações de movimento
        self.movement_range = movement_range
        self.movement_speed = movement_speed
        self.movement_offset = 0
        self.movement_direction = 1
        
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        # Movimento horizontal
        self.rect[0] -= GAME_SPEED
        
        # Movimento vertical
        self.movement_offset += self.movement_speed * self.movement_direction
        
        if abs(self.movement_offset) >= self.movement_range:
            self.movement_direction *= -1
        
        self.rect[1] = self.initial_y + self.movement_offset