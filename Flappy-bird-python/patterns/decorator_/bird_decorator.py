class BirdDecorator:
 
    def __init__(self, bird):
        from entities.bird import Bird as BirdClass
        
        if not isinstance(bird, (BirdClass, BirdDecorator)):
            raise TypeError(f"bird deve ser uma instância de Bird ou BirdDecorator, recebeu {type(bird)}")
        
        self._decorated_bird = bird
        self.image = bird.image
        self.rect = bird.rect
        self.mask = bird.mask
        self.groups = bird.groups
    
    def update(self):
        """Atualiza o bird decorado e sincroniza atributos visuais."""
        self._decorated_bird.update()
        self.image = self._decorated_bird.image
        self.rect = self._decorated_bird.rect
        self.mask = self._decorated_bird.mask
    
    def set_state(self, state):
        self._decorated_bird.set_state(state)
    
    def get_state(self):
        return self._decorated_bird.get_state()
    
    def bump(self):
        self._decorated_bird.bump()
    
    def can_collide(self):
 
        return self._decorated_bird.can_collide()
    
    def begin(self):
        self._decorated_bird.begin()
    
    def __getattr__(self, name):
        return getattr(self._decorated_bird, name)
    
    def __class_getitem__(cls, item):
        return cls
