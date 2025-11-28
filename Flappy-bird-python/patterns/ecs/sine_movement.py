import time
import math
from config import GAME_SPEED
from patterns.ecs.game_object import Component


class SineMovement(Component):
    def __init__(self, amplitude=50, frequency=1, horizontal_speed=GAME_SPEED):
        super().__init__()
        self.amplitude = amplitude
        self.frequency = frequency
        self.horizontal_speed = horizontal_speed
        self.start_time = time.time()
        self.initial_y = 0

    def update(self, dt):
        if self.game_object is None:
            return

        if self.initial_y == 0:
            self.initial_y = self.game_object.y

        self.game_object.x -= self.horizontal_speed * dt

        elapsed = time.time() - self.start_time

        self.game_object.y = int(
            self.initial_y
            + self.amplitude * math.sin(2 * math.pi * self.frequency * elapsed)
        )
