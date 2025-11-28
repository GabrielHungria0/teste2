from config import GRAVITY, GAME_SPEED
from patterns.ecs.game_object import Component


class RigidBody(Component):
    def __init__(self, velocity=0):
        super().__init__()
        self.velocity = velocity
        self.gravity = GRAVITY

    def update(self, dt):
        self.velocity += self.gravity * dt

        self.game_object.y += self.velocity

    def jump(self, force):
        self.velocity = force
