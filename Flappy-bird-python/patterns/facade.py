
import pygame
from config import *


class ResourceFacade:
    
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self._load_resources()
    
    def _load_resources(self):
        """Carrega todos os recursos do jogo"""
        self.images['bird_up'] = pygame.image.load(BIRD_UP_SPRITE).convert_alpha()
        self.images['bird_mid'] = pygame.image.load(BIRD_MID_SPRITE).convert_alpha()
        self.images['bird_down'] = pygame.image.load(BIRD_DOWN_SPRITE).convert_alpha()
        
        self.images['pipe'] = pygame.image.load(PIPE_SPRITE).convert_alpha()
        self.images['ground'] = pygame.image.load(GROUND_SPRITE).convert_alpha()
        self.images['background'] = pygame.image.load(BACKGROUND_SPRITE)
        self.images['message'] = pygame.image.load(MESSAGE_SPRITE).convert_alpha()
        
        self.sounds['wing'] = WING_SOUND
        self.sounds['hit'] = HIT_SOUND
    
    def get_bird_images(self):
        return [self.images['bird_up'], self.images['bird_mid'], self.images['bird_down']]
    
    def get_image(self, name):
        return self.images.get(name)
    
    def get_sound(self, name):
        return self.sounds.get(name)
    
    def get_scaled_background(self, width, height):
        return pygame.transform.scale(self.images['background'], (width, height))
    
    def get_scaled_ground(self, width, height):
        return pygame.transform.scale(self.images['ground'], (width, height))