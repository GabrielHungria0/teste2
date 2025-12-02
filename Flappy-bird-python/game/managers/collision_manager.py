"""Gerenciador centralizado de detecção e tratamento de colisões."""
import time
from game.collision import DecoratorAwareCollisionDetector
from patterns.event import CollisionEvent, GameOverEvent


class CollisionManager:
        game_context.event_system.notify(CollisionEvent())
        game_context.event_system.notify(GameOverEvent())
        time.sleep(1)
        game_context.game_over()
