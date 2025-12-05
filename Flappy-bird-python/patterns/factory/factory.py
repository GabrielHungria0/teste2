from abc import ABC, abstractmethod
import random
from typing import List
import uuid
from config import GameConfig
from entities.pipe import Pipe


class ObstacleFactory(ABC):
    def __init__(self):
        self._config = GameConfig()
    
    @abstractmethod
    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        pass
    
    def _generate_random_size(self):
        return random.randint(100, 300)
    
    def _create_pipe_pair_id(self):
        return uuid.uuid4().hex
    
    def _assign_pair_id(self, pipes, pair_id):
        for pipe in pipes:
            pipe.pair_id = pair_id
    
    def _create_pipe_pair(self, xpos, size, gap, resource_facade, pipe_class=Pipe):
        
        pipe_bottom = pipe_class(False, xpos, size, resource_facade)
        pipe_top = pipe_class(True, xpos, self._config.SCREEN_HEIGHT - size - gap, resource_facade)
        
        pair_id = self._create_pipe_pair_id()
        self._assign_pair_id([pipe_bottom, pipe_top], pair_id)
        
        return [pipe_bottom, pipe_top]


class PipeFactory(ObstacleFactory):
    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        size = self._generate_random_size()
        gap = self._config.PIPE_GAP
        return self._create_pipe_pair(xpos, size, gap, resource_facade)