from abc import ABC, abstractmethod
from patterns.factory import (
    PipeFactory,
    MovingPipeFactory,
    NarrowPipeFactory,
    AlternatingMovingPipeFactory
)

class DifficultyLevel(ABC):
    def __init__(self):
        self._next_level = None
    
    def set_next(self, level):
        self._next_level = level
        return level
    
    @abstractmethod
    def get_threshold(self):
        pass
    
    @abstractmethod
    def create_factory(self):
        pass
    
    def handle(self, score, current_factory):
        if score >= self.get_threshold():
            if self._next_level:
                return self._next_level.handle(score, current_factory)
            return self._get_factory_if_different(current_factory)
        
        return self._get_factory_if_different(current_factory)
    
    def _get_factory_if_different(self, current_factory):
        new_factory = self.create_factory()
        if not isinstance(current_factory, type(new_factory)):
            return new_factory
        return current_factory
