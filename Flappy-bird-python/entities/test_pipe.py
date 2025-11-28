from config import GAME_SPEED, PIPE_LAYER
from patterns.ecs.auto_move import AutoMove
from patterns.ecs.game_object import Component, GameObject
from patterns.ecs.sine_movement import SineMovement
from patterns.ecs.sprite_renderer import SpriteRenderer


class TestPipe(Component):

    def __init__(self, flipped=False):
        super().__init__()
        self.flipped = flipped

    def update(self, dt):
        renderer = self.game_object.get_component(SpriteRenderer)

        if renderer is not None:
            if self.game_object.x < -renderer.width:
                super().destroy()

    def start(self):
        self.game_object.add_component(
            SpriteRenderer("assets/sprites/pipe-green.png", PIPE_LAYER, self.flipped)
        )

        self.game_object.add_component(AutoMove(-GAME_SPEED))

    def dispose(self):
        print("Destroying test pipe")
