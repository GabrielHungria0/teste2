import pygame
from patterns.ecs.game_object import Component


class SpriteRenderer(Component):
    def __init__(self, image_path, layer: int, flipped: bool = False):
        super().__init__()
        self.layer = layer
        self.flipped = flipped

        self.original_image = pygame.image.load(image_path).convert_alpha()

        self.image = pygame.transform.scale(
            self.original_image,
            (self.original_image.get_width(), self.original_image.get_height()),
        )

        self.width = self.original_image.get_width()
        self.height = self.original_image.get_height()

        if self.flipped:
            self.image = pygame.transform.flip(self.image, False, True)

    def update(self, dt):
        if self.game_object.width == 0:
            self.game_object.width = self.width
            self.game_object.height = self.height

    def render(self, surface):
        surface.blit(self.image, (self.game_object.x, self.game_object.y))

    def start(self):
        pass

    def dispose(self):
        self.original_image = None
        self.image = None
