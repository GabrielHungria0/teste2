from patterns.loader.image import ImageAsset
from patterns.loader.sound import SoundAsset


class AssetLoader:
    @staticmethod
    def load_sound(path: str) -> SoundAsset:
        return SoundAsset(path)

    @staticmethod
    def load_image(path: str) -> ImageAsset:
        return ImageAsset(path)
