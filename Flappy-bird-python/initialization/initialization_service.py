"""Serviço centralizado para inicialização de todos os subsistemas do jogo."""
import pygame
from config import GameConfig
from patterns.faceit.resource_facade import ResourceFacade
from patterns.observer import GameEventSubject, ScoreObserver, SoundObserver
from game.managers.sprite_manager import SpriteManager
from game.managers import GroundManager, PipeManager


class GameInitializationService:
    """Responsável por inicializar e resetar subsistemas do jogo."""
    
    def __init__(self, config, initializer):
        self._config = config
        self._initializer = initializer
    
    def initialize_all(self):
        """Inicializa todos os subsistemas e retorna um dicionário com referências."""
        systems = self._create_systems()
        resources = self._create_resources(systems)
        entities = self._create_entities(systems, resources)
        
        return {
            **systems,
            **resources,
            **entities
        }
    
    def _create_systems(self):
        """Cria event system, observers e sprite manager."""
        event_system = GameEventSubject()
        score_observer = ScoreObserver()
        sprite_manager = SpriteManager()
        sprite_manager.create_group("bird")
        sprite_manager.create_group("ground")
        sprite_manager.create_group("pipes")
        
        return {
            "event_system": event_system,
            "score_observer": score_observer,
            "sprite_manager": sprite_manager
        }
    
    def _create_resources(self, systems):
        """Cria ResourceFacade, observers de som e assets de UI."""
        resource_facade = ResourceFacade()
        sound_observer = SoundObserver(resource_facade)
        systems["event_system"].attach(systems["score_observer"])
        systems["event_system"].attach(sound_observer)
        
        bg_image = resource_facade.get_image("background")
        background = pygame.transform.scale(
            bg_image,
            (self._config.SCREEN_WIDTH, self._config.SCREEN_HEIGHT)
        )
        begin_image = resource_facade.get_image("message")
        
        return {
            "resource_facade": resource_facade,
            "sound_observer": sound_observer,
            "background": background,
            "begin_image": begin_image
        }
    
    def _create_entities(self, systems, resources):
        """Cria entidades do jogo: bird, ground, pipes e managers."""
        bird = self._initializer.initialize_bird(systems["sprite_manager"], resources["resource_facade"])
        ground_manager = GroundManager(systems["sprite_manager"])
        self._initializer.initialize_ground(systems["sprite_manager"], resources["resource_facade"])
        pipe_manager = self._initializer.initialize_pipes(systems["sprite_manager"], resources["resource_facade"])
        hud_renderer = self._initializer.create_hud_renderer()
        collision_manager = self._initializer.create_collision_manager()
        
        return {
            "bird": bird,
            "ground_manager": ground_manager,
            "pipe_manager": pipe_manager,
            "hud_renderer": hud_renderer,
            "collision_manager": collision_manager
        }
