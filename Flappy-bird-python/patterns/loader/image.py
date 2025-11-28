import pygame


class ImageAsset:
    def __init__(self, path: str):
        self.path = path
        self.pgImage = pygame.image.load(path).convert_alpha()
        self.width = self.pgImage.get_width()
        self.height = self.pgImage.get_height()

    def get_rect(self):
        return self.pgImage.get_rect()
