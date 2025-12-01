# patterns/state/bird/flying_state.py

from .bird_state_interface import BirdState

class FlyingState(BirdState):
    def update(self, bird):
        bird._update_sprite()
        bird._apply_gravity()
        bird._update_position()
    
    def bump(self, bird):
        bird._speed = -bird._config.SPEED
    
    def can_collide(self):
        return True