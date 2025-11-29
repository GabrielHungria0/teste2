import pygame
import time


class BirdDecorator(pygame.sprite.Sprite):
    def __init__(self, bird):
        super().__init__()
        self._decorated_bird = bird
        self._sync_attributes()
    
    def _sync_attributes(self):
        self.image = self._decorated_bird.image
        self.rect = self._decorated_bird.rect
        self.mask = self._decorated_bird.mask
    
    def update(self):
        self._decorated_bird.update()
        self._sync_attributes()
    
    def __getattr__(self, name):
        return getattr(self._decorated_bird, name)


class InvincibleBirdDecorator(BirdDecorator):
    def __init__(self, bird, duration=3.0):
        super().__init__(bird)
        self._duration = duration
        self._start_time = time.time()
        self._is_invincible = True
    
    def update(self):
        super().update()
        self._check_invincibility_expired()
        if self._is_invincible:
            self._apply_visual_effect()
    
    def _check_invincibility_expired(self):
        if time.time() - self._start_time > self._duration:
            self._is_invincible = False
    
    def _apply_visual_effect(self):
        self._decorated_bird.image.set_alpha(200)
    
    def can_collide(self):
        if self._is_invincible:
            return False
        return self._decorated_bird.can_collide()
    
    def check_collision(self, sprite_group):
        if not self.can_collide():
            return False
        
        return pygame.sprite.spritecollide(
            self._decorated_bird, sprite_group, False, pygame.sprite.collide_mask
        )