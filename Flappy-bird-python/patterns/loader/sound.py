import pygame
from patterns.loader.asset import Asset


class SoundAsset(Asset):
    def __init__(self, path):
        self._pgSound = pygame.mixer.Sound(path)

    def play(self):
        self._pgSound.play()
