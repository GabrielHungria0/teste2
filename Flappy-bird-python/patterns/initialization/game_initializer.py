"""Serviço responsável pela inicialização de entidades do jogo."""
from config import GameConfig
from entities.bird import Bird
from entities.ground import Ground
from patterns.factory import PipeFactory
from game.managers import PipeManager
from game.managers.hud_renderer import HUDRenderer
from game.managers.collision_manager import CollisionManager


class GameInitializer:
    """Inicializa todas as entidades do jogo (pássaro, chão, pipes)."""
    
    def __init__(self):
        self._config = GameConfig()
    
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
