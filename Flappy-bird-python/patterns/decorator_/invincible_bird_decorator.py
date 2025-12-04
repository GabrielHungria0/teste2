"""Decorator que adiciona invencibilidade temporária ao Bird."""
import time
from patterns.decorator_.bird_decorator import BirdDecorator


class InvincibleBirdDecorator(BirdDecorator):
    """
    Decorador que torna o Bird invencível por um período limitado.
    
    Durante a invencibilidade:
    - can_collide() retorna False, bloqueando colisões
    - Aplica efeito visual de transparência
    - Após expirar, restaura comportamento normal
    """
    
    DEFAULT_DURATION = 3.0
    INVINCIBLE_ALPHA = 200
    NORMAL_ALPHA = 255
    
    def __init__(self, bird, duration=None):
        super().__init__(bird)
        self._duration = duration or self.DEFAULT_DURATION
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
    
    @property
    def remaining_time(self):
        """Retorna o tempo restante de invencibilidade."""
        if not self._is_invincible:
            return 0.0
        elapsed = time.time() - self._start_time
        return max(0.0, self._duration - elapsed)
    
    def update(self):
        """Atualiza o bird decorado, verifica expiração e aplica efeito visual."""
        super().update()
        self._update_invincibility_status()
        self._apply_visual_feedback()
    
    def _update_invincibility_status(self):
        """Verifica e atualiza o status de invencibilidade."""
        if self._is_invincible and self._has_expired():
            self._is_invincible = False
    
    def _has_expired(self):
        """Verifica se o tempo de invencibilidade expirou."""
        return time.time() - self._start_time > self._duration
    
    def _apply_visual_feedback(self):
        """Aplica feedback visual baseado no status de invencibilidade."""
        alpha = self.INVINCIBLE_ALPHA if self._is_invincible else self.NORMAL_ALPHA
        self._set_alpha(alpha)
    
    def _set_alpha(self, alpha):
        """Define a transparência da imagem com tratamento de erro."""
        try:
            self._decorated_bird.image.set_alpha(alpha)
        except (AttributeError, pygame.error):
            pass
    
    def can_collide(self):
        """
        Retorna False durante invencibilidade, bloqueando colisões.
        Após expirar, delega para o bird decorado.
        """
        if self._is_invincible:
            return False
        return self._decorated_bird.can_collide()
