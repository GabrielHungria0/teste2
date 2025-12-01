"""Gerenciador centralizado de detecção e tratamento de colisões."""
import time
from game.collision import DecoratorAwareCollisionDetector
from patterns.event import CollisionEvent, GameOverEvent


class CollisionManager:
    """Encapsula detecção de colisão e tratamento de eventos."""
    
    def __init__(self):
        self._detector = DecoratorAwareCollisionDetector()
    
    def check_and_handle(self, game_context):
        """Verifica colisões usando o detector e trata o resultado."""
        bird = game_context.bird
        ground_group = game_context.sprite_manager.get_group("ground")
        pipe_group = game_context.sprite_manager.get_group("pipes")
        
        if self._detector.detect_collision(bird, ground_group):
            self._handle_collision(game_context)
        elif self._detector.detect_collision(bird, pipe_group):
            self._handle_collision(game_context)
    
    def _handle_collision(self, game_context):
        """Trata a colisão: mata o pássaro e notifica eventos."""
        game_context.bird.die()
        game_context.event_system.notify(CollisionEvent())
        game_context.event_system.notify(GameOverEvent())
        time.sleep(1)
        game_context.game_over()
