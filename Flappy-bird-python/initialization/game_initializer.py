import pygame
from config import GameConfig
from entities.bird import Bird
from entities.ground import Ground
from patterns.factory import PipeFactory
from game.managers import PipeManager, GroundManager
from game.managers.hud_renderer import HUDRenderer
from game.managers.collision_manager import CollisionManager
from game.managers.sprite_manager import SpriteManager
from patterns.faceit.resource_facade import ResourceFacade
from patterns.observer import GameEventSubject, ScoreObserver, SoundObserver


class GameInitializer:
    """
    Serviço centralizado responsável pela inicialização de todos os subsistemas e entidades do jogo.
    Combina a lógica de criação de entidades e orquestração da inicialização.
    """
    
    def __init__(self, config=None):
        self._config = config or GameConfig()
    
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
        bird = self.initialize_bird(systems["sprite_manager"], resources["resource_facade"])
        ground_manager = GroundManager(systems["sprite_manager"])
        self.initialize_ground(systems["sprite_manager"], resources["resource_facade"])
        pipe_manager = self.initialize_pipes(systems["sprite_manager"], resources["resource_facade"])
        hud_renderer = self.create_hud_renderer()
        collision_manager = self.create_collision_manager()
        
        return {
            "bird": bird,
            "ground_manager": ground_manager,
            "pipe_manager": pipe_manager,
            "hud_renderer": hud_renderer,
            "collision_manager": collision_manager
        }
    
    def initialize_bird(self, sprite_manager, resource_facade):
        """Cria e configura o pássaro."""
        bird = Bird(resource_facade)
        sprite_manager.add_to_group("bird", bird)
        return bird
    
    def initialize_ground(self, sprite_manager, resource_facade):
        """Cria e configura os blocos de chão iniciais."""
        for i in range(2):
            ground = Ground(self._config.GROUND_WIDTH * i, resource_facade)
            sprite_manager.add_to_group("ground", ground)
    
    def initialize_pipes(self, sprite_manager, resource_facade):
        """Cria e configura os pipes iniciais com seu gerenciador."""
        obstacle_factory = PipeFactory()
        pipe_manager = PipeManager(sprite_manager, obstacle_factory)
        
        for i in range(2):
            pipe_manager.add_pair(
                self._config.SCREEN_WIDTH * i + 800,
                resource_facade
            )
        
        return pipe_manager
    
    def create_hud_renderer(self):
        """Cria a renderizadora de HUD."""
        return HUDRenderer()
    
    def create_collision_manager(self):
        """Cria o gerenciador de colisões."""
        return CollisionManager()
