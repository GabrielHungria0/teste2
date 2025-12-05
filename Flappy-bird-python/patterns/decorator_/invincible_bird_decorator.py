"""Decorator que adiciona invencibilidade temporária ao Bird."""
import time
from patterns.decorator_.bird_decorator import BirdDecorator


class InvincibleBirdDecorator(BirdDecorator):
  
    DEFAULT_DURATION = 3.0
    INVINCIBLE_ALPHA = 100
    NORMAL_ALPHA = 255
    
    def __init__(self, bird, duration=None):
        super().__init__(bird)
        self._duration = duration or self.DEFAULT_DURATION
        self._start_time = time.time()
        self._is_invincible = True
    
    def reset(self, duration=None):
        if duration is not None:
            self._duration = duration
        self._start_time = time.time()
        self._is_invincible = True
    
    @property
    def is_expired(self):
        return not self._is_invincible
    
    @property
    def remaining_time(self):
        if not self._is_invincible:
            return 0.0
        elapsed = time.time() - self._start_time
        return max(0.0, self._duration - elapsed)
    
    def update(self):
        super().update()
        self._update_invincibility_status()
        self._apply_visual_feedback()
    
    def _update_invincibility_status(self):
        if self._is_invincible and self._has_expired():
            self._is_invincible = False
    
    def _has_expired(self):
        return time.time() - self._start_time > self._duration
    
    def _apply_visual_feedback(self):
        alpha = self.INVINCIBLE_ALPHA if self._is_invincible else self.NORMAL_ALPHA
        self._set_alpha(alpha)
    
    def _set_alpha(self, alpha):
        try:
            self._decorated_bird.image.set_alpha(alpha)
        except (AttributeError, pygame.error):
            pass
    
    def can_collide(self):
        if self._is_invincible:
            return False
        return self._decorated_bird.can_collide()
