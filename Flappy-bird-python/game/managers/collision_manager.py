"""Gerenciador centralizado de detecção e tratamento de colisões."""
import time
from game.collision import SmartCollisionDetector
from patterns.event import CollisionEvent, GameOverEvent
from patterns.state.bird.dead_state import DeadState


class CollisionManager:
 
    GAME_OVER_DELAY = 1.0
    
    def __init__(self):
        self._detector = SmartCollisionDetector()
    
    def check_and_handle(self, game_context):
        if self._has_collision(game_context):
            self._handle_collision(game_context)
    
    def _has_collision(self, game_context):
        """Verifica se há colisão com chão ou canos."""
        bird = game_context.bird
        ground_group = game_context.sprite_manager.get_group("ground")
        pipe_group = game_context.sprite_manager.get_group("pipes")
        
        return (
            self._detector.detect_collision(bird, ground_group) or
            self._detector.detect_collision(bird, pipe_group)
        )
    
    def _handle_collision(self, game_context):
        """Trata a colisão: mata o pássaro e notifica eventos."""
        self._kill_bird(game_context.bird)
        self._notify_collision_events(game_context)
        time.sleep(self.GAME_OVER_DELAY)
        game_context.state_manager.transition_to_game_over()
    
    def _kill_bird(self, bird):
        """Muda o estado do bird para morto."""
        bird.set_state(DeadState())
    
    def _notify_collision_events(self, game_context):
        """Notifica observadores sobre colisão e game over."""
        game_context.event_system.notify(CollisionEvent())
        game_context.event_system.notify(GameOverEvent())
