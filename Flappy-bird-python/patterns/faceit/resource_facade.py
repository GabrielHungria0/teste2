import pygame
from game.managers.resource_manager import ResourceManager


class ResourceFacade:
    """Facade que encapsula acesso a recursos do jogo."""
    def __init__(self):
        self._resource_manager = ResourceManager()

    def get_bird_images(self):
        return self._resource_manager.load_bird_sprites()
    
    def get_image(self, name):
        """Retorna uma imagem pelo nome."""
        image_methods = {
            "pipe": self._resource_manager.load_pipe_sprite,
            "ground": self._resource_manager.load_ground_sprite,
            "background": self._resource_manager.load_background_sprite,
            "message": self._resource_manager.load_message_sprite
        }
        method = image_methods.get(name)
        return method() if method else None
    
    def get_sound(self, name):
        """Carrega e retorna um som pygame.mixer.Sound."""
        sound_path = self._resource_manager.get_sound_path(name)
        if sound_path:
            return pygame.mixer.Sound(sound_path)
        return None