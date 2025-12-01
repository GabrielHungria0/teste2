# patterns/state/bird/dead_state.py

from .bird_state_interface import BirdState

class DeadState(BirdState):
    def update(self, bird):
        bird._apply_gravity()
        bird._update_position()
    
    def bump(self, bird):
        pass
    
    def can_collide(self):
        return False