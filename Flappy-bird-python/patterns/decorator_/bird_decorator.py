
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

