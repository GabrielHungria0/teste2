from typing import List
from entities.pipe import Pipe
from patterns.factory.factory import PipeFactory

class NarrowPipeFactory(PipeFactory):
    def __init__(self, gap_reduction=30):
        super().__init__()
        self._gap_reduction = gap_reduction
    
    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        size = self._generate_random_size()
        narrow_gap = self._config.PIPE_GAP - self._gap_reduction
        return self._create_pipe_pair(xpos, size, narrow_gap, resource_facade)