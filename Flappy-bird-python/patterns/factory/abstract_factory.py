from abc import ABC, abstractmethod
import random
from typing import List
import uuid

from config import PIPE_GAP, SCREEN_HEIGHT
from entities.pipe import Pipe


class ObstacleFactory(ABC):

    @abstractmethod
    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        pass


class PipeFactory(ObstacleFactory):

    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        size = random.randint(100, 300)
        pipe_bottom = Pipe(False, xpos, size, resource_facade)
        pipe_top = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP, resource_facade)
        # Marca o par com um id único para facilitar contagem
        pair_id = uuid.uuid4().hex
        pipe_bottom.pair_id = pair_id
        pipe_top.pair_id = pair_id
        return [pipe_bottom, pipe_top]
