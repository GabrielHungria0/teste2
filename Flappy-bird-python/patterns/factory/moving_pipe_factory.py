from typing import List
from entities.moving_pipe import MovingPipe
from entities.pipe import Pipe
from patterns.factory.factory import ObstacleFactory


class MovingPipeFactory(ObstacleFactory):
    def __init__(self, movement_range=40, movement_speed=2):
        super().__init__()
        self._movement_range = movement_range
        self._movement_speed = movement_speed
    
    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        size = self._generate_random_size()
        gap = self._config.PIPE_GAP
        
        # Cria uma classe wrapper que injeta parâmetros de movimento
        def create_moving_pipe(*args, **kwargs):
            return MovingPipe(*args, self._movement_range, self._movement_speed, **kwargs)
        
        return self._create_pipe_pair(xpos, size, gap, resource_facade, create_moving_pipe)