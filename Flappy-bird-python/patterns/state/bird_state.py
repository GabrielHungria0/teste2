from abc import ABC, abstractmethod


class BirdState(ABC):
    @abstractmethod
    def update(self, bird):
        pass
    
    @abstractmethod
    def bump(self, bird):
        pass
    
    @abstractmethod
    def can_collide(self):
        pass


class FlyingState(BirdState):
    def update(self, bird):
        bird._update_sprite()
        bird._apply_gravity()
        bird._update_position()
        
        if bird._speed > bird._config.GRAVITY * 3:
            bird.set_state(FallingState())
    
    def bump(self, bird):
        bird._speed = -bird._config.SPEED
    
    def can_collide(self):
        return True


class FallingState(BirdState):
    def update(self, bird):
        bird._update_sprite()
        bird._apply_gravity()
        bird._update_position()
    
    def bump(self, bird):
        bird._speed = -bird._config.SPEED
        bird.set_state(FlyingState())
    
    def can_collide(self):
        return True


class DeadState(BirdState):
    def update(self, bird):
        bird._apply_gravity()
        bird._update_position()
    
    def bump(self, bird):
        pass
    
    def can_collide(self):
        return False


class IdleState(BirdState):
    def update(self, bird):
        bird._update_sprite()
    
    def bump(self, bird):
        bird.set_state(FlyingState())
    
    def can_collide(self):
        return False