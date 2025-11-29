import pygame
from config import GameConfig
from patterns.state.bird_state import IdleState, FlyingState, DeadState


class Bird(pygame.sprite.Sprite):
    def __init__(self, resource_facade):
        pygame.sprite.Sprite.__init__(self)
        
        self._config = GameConfig()
        self._images = resource_facade.get_bird_images()
        self._speed = self._config.SPEED
        self._current_image = 0
        
        self.image = self._images[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self._create_initial_rect()
        
        self._state = IdleState()
    
    def _create_initial_rect(self):
        rect = self.image.get_rect()
        rect[0] = self._config.SCREEN_WIDTH / 6
        rect[1] = self._config.SCREEN_HEIGHT / 2
        return rect
    
    def set_state(self, state):
        self._state = state
    
    def get_state(self):
        return self._state
    
    def update(self):
        self._state.update(self)
    
    def _update_sprite(self):
        self._current_image = (self._current_image + 1) % 3
        self.image = self._images[self._current_image]
    
    def _apply_gravity(self):
        self._speed += self._config.GRAVITY
    
    def _update_position(self):
        self.rect[1] += self._speed
    
    def bump(self):
        self._state.bump(self)
    
    def die(self):
        self.set_state(DeadState())
    
    def can_collide(self):
        return self._state.can_collide()
    
    def begin(self):
        self._update_sprite()