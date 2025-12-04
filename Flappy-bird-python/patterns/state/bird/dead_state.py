from .bird_state_interface import BirdState


class DeadState(BirdState):
    """Estado do pássaro após morrer."""
    
    def update(self, bird):
        bird._apply_gravity()
        bird._update_position()
    
    def bump(self, bird):
        pass
    
    def can_collide(self):
        return False
