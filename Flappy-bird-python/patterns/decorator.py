import pygame
import time


class BirdDecorator:
    """
    Decorador base para Bird que segue o padrão Decorator.
    Herda de Bird dinamicamente (lazy import) para evitar circular imports.
    """
    def __init__(self, bird):
        # Obtém a classe Bird dinamicamente para evitar circular import
        from entities.bird import Bird as BirdClass
        
        # Valida que o bird decorado é uma Bird
        if not isinstance(bird, BirdClass):
            raise TypeError(f"bird deve ser uma instância de Bird, recebeu {type(bird)}")
        
        self._decorated_bird = bird
        # Sincroniza atributos pygame.sprite.Sprite
        self.image = bird.image
        self.rect = bird.rect
        self.mask = bird.mask
        self.groups = bird.groups
        self._Bird = BirdClass
    
    def update(self):
        """Atualiza o bird decorado e sincroniza atributos visuais."""
        self._decorated_bird.update()
        self.image = self._decorated_bird.image
        self.rect = self._decorated_bird.rect
        self.mask = self._decorated_bird.mask
    
    def set_state(self, state):
        """Delega mudança de estado ao bird decorado."""
        self._decorated_bird.set_state(state)
    
    def get_state(self):
        """Retorna o estado do bird decorado."""
        return self._decorated_bird.get_state()
    
    def bump(self):
        """Delega bump ao bird decorado."""
        self._decorated_bird.bump()
    
    def die(self):
        """Delega die ao bird decorado."""
        self._decorated_bird.die()
    
    def can_collide(self):
        """Retorna se o bird pode colidir."""
        return self._decorated_bird.can_collide()
    
    def begin(self):
        """Delega begin ao bird decorado."""
        self._decorated_bird.begin()
    
    def __getattr__(self, name):
        """Passa chamadas de atributos não definidos para o bird decorado."""
        return getattr(self._decorated_bird, name)
    
    # Compatibilidade com pygame.sprite
    def __class_getitem__(cls, item):
        return cls


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