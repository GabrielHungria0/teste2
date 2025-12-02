import pygame
from typing import Dict


class SoundService:
    """Gerencia reprodução de sons do jogo com suporte a cache."""
    def __init__(self):
        self._sounds: Dict[str, pygame.mixer.Sound] = {}
        
    def play(self, sound: pygame.mixer.Sound, tag: str = None):
        """Reproduz um som já carregado.
        
        Args:
            sound: Som pygame.mixer.Sound já carregado
            tag: Identificador opcional para armazenar em cache
        """
        if tag:
            self._sounds[tag] = sound
        sound.play()