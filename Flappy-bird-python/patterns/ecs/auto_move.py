from config import GAME_SPEED
from patterns.ecs.game_object import Component


class AutoMove(Component):
    def __init__(self, speed=GAME_SPEED):
        super().__init__()
        self.speed = speed

    def update(self, dt):
        self.game_object.x += self.speed * dt
        print(f"updating pos x to {self.game_object.x}")

    def start(self):
        pass

    def dispose(self):
        pass
