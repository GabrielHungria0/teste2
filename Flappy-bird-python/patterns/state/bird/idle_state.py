from .bird_state_interface import BirdState


class IdleState(BirdState):
    """Estado inicial do pássaro antes de começar a voar."""
    
    def update(self, bird):
        bird._update_sprite()
    
    def bump(self, bird):
        from .flying_state import FlyingState
        
        bird.set_state(FlyingState())
        bird._speed = -bird._config.SPEED
    
    def can_collide(self):
        return False
