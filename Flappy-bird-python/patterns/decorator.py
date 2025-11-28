# decorators.py
import pygame
import time

class BirdDecorator(pygame.sprite.Sprite):
    
    def __init__(self, bird):
        super().__init__()
        self._decorated_bird = bird
        
        self.image = bird.image
        self.rect = bird.rect
        self.mask = bird.mask
        
    def update(self):
        self._decorated_bird.update()
        self.image = self._decorated_bird.image
        self.rect = self._decorated_bird.rect
        self.mask = self._decorated_bird.mask

    def __getattr__(self, name):
        """Passa chamadas de métodos não definidos para o objeto decorado (ex: bump())"""
        return getattr(self._decorated_bird, name)


class InvincibleBirdDecorator(BirdDecorator):
    """Adiciona invencibilidade temporária ao pássaro."""
    
    def __init__(self, bird, duration=3.0):
        super().__init__(bird)
        self.is_invincible = True
        self.start_time = time.time()
        self.duration = duration
        
    def update(self):
        super().update()
        
        # Verifica se a invencibilidade acabou
        if time.time() - self.start_time > self.duration:
            self.is_invincible = False
            return self._decorated_bird # Retorna o objeto original sem o decorator

        self._decorated_bird.image.set_alpha(255)



    def check_collision(self, pipe_group):
        if self.is_invincible:
            return False
        
        return pygame.sprite.spritecollide(self._decorated_bird, pipe_group, False, pygame.sprite.collide_mask)