import pygame
from config import GameConfig


class SpriteManager:
    def __init__(self):
        self._config = GameConfig()
        self._groups = {}
    
    def create_group(self, name):
        self._groups[name] = pygame.sprite.Group()
        return self._groups[name]
    
    def get_group(self, name):
        return self._groups.get(name, pygame.sprite.Group())
    
    def add_to_group(self, group_name, sprite):
        if group_name in self._groups:
            self._groups[group_name].add(sprite)
    
    def remove_from_group(self, group_name, sprite):
        if group_name in self._groups:
            self._groups[group_name].remove(sprite)
    
    def clear_group(self, group_name):
        if group_name in self._groups:
            self._groups[group_name].empty()
    
    def update_group(self, group_name):
        if group_name in self._groups:
            self._groups[group_name].update()
    
    def draw_group(self, group_name, screen):
        if group_name in self._groups:
            self._groups[group_name].draw(screen)
    
    def get_sprites(self, group_name):
        if group_name in self._groups:
            return self._groups[group_name].sprites()
        return []