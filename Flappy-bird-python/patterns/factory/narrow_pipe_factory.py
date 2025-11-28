from patterns.factory.abstract_factory import ObstacleFactory
import random
from typing import List
import uuid
from config import PIPE_GAP, SCREEN_HEIGHT
from entities.pipe import Pipe
from patterns.factory.abstract_factory import ObstacleFactory


class NarrowPipeFactory(ObstacleFactory):

    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        size = random.randint(100, 300)
        narrow_gap = PIPE_GAP - 30
        pipe_bottom = Pipe(False, xpos, size, resource_facade)
        pipe_top = Pipe(True, xpos, SCREEN_HEIGHT - size - narrow_gap, resource_facade)
        # Marca o par com um id único
        pair_id = uuid.uuid4().hex
        pipe_bottom.pair_id = pair_id
        pipe_top.pair_id = pair_id
        return [pipe_bottom, pipe_top]
