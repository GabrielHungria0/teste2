from patterns.ecs.game_object import Component
from patterns.ecs.sprite_renderer import SpriteRenderer


class BoundingBox(Component):
    def start(self):
        renderer = self.game_object.get_component(SpriteRenderer)

        if renderer is not None:
            self.width = renderer.width
            self.height = renderer.height
        else:
            raise RuntimeError("Bounding Box require Sprite Renderer component")

    def update(self, dt):
        pass

    def dispose(self):
        pass
