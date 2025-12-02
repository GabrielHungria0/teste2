import time

import pygame
from patterns.decorator_.bird_decorator import BirdDecorator


class InvincibleBirdDecorator(BirdDecorator):
    """Decorador que torna o Bird invencível por um período limitado."""
    
    def __init__(self, bird, duration=3.0):
        super().__init__(bird)
        self._duration = duration
        self._start_time = time.time()
        self._is_invincible = True
    
    def reset(self, duration=None):
        """Reinicia o timer de invencibilidade."""
        if duration is not None:
            self._duration = duration
        self._start_time = time.time()
        self._is_invincible = True
    
    @property
    def is_expired(self):
        """Retorna True se a invencibilidade expirou."""
        return not self._is_invincible
    
    def update(self):
        """Atualiza o bird decorado, verifica expiração e aplica efeito visual."""
        super().update()
        self._check_invincibility_expired()
        if self._is_invincible:
            self._apply_visual_effect()
    
    def _check_invincibility_expired(self):
        """Verifica se o tempo de invencibilidade expirou."""
        if time.time() - self._start_time > self._duration:
            self._is_invincible = False
            try:
                # Restaura opacidade original
                self._decorated_bird.image.set_alpha(255)
            except Exception:
                pass
    
    def _apply_visual_effect(self):
        """Aplica efeito visual (transparência) ao pássaro invencível."""
        self._decorated_bird.image.set_alpha(200)
    
    def can_collide(self):
        """Retorna False se invencível, bloqueando colisões."""
        return not self._is_invincible
    
    def check_collision(self, sprite_group):
        """Verifica colisão apenas se não estiver invencível."""
        if not self.can_collide():
            return False
        
        return pygame.sprite.spritecollide(
            self._decorated_bird, sprite_group, False, pygame.sprite.collide_mask
        )