"""Módulo de detecção de colisões."""
from .collision_detector import CollisionDetector

# Backward compatibility aliases
SmartCollisionDetector = CollisionDetector
DecoratorAwareCollisionDetector = CollisionDetector
MaskCollisionDetector = CollisionDetector

__all__ = ['CollisionDetector']