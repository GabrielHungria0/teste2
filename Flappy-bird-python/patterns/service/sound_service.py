from abc import ABC, abstractmethod
from typing import Dict

from patterns.loader.asset_loader import AssetLoader
from patterns.loader.sound import SoundAsset


class SoundService:

    def __init__(self):
        self.sounds: Dict[str, SoundAsset] = {}

    def play(self, path: str, tag: str):
        if self.sounds.get(tag) is None:
            self.sounds[tag] = AssetLoader.load_sound(path)

        self.sounds[tag].play()
