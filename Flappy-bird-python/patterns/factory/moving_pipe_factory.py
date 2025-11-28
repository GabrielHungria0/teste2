import random
from typing import List
import uuid
from config import PIPE_GAP, SCREEN_HEIGHT
from entities.moving_pipe import MovingPipe
from entities.pipe import Pipe
from patterns.factory.abstract_factory import ObstacleFactory


class MovingPipeFactory(ObstacleFactory):

    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        size = random.randint(100, 300)

        pipe_bottom = MovingPipe(
            inverted=False,
            xpos=xpos,
            ysize=size,
            resource_facade=resource_facade,
            movement_range=40,
            movement_speed=2,
        )

        pipe_top = MovingPipe(
            inverted=True,
            xpos=xpos,
            ysize=SCREEN_HEIGHT - size - PIPE_GAP,
            resource_facade=resource_facade,
            movement_range=40,
            movement_speed=2,
        )

        # Marca o par com um id único
        pair_id = uuid.uuid4().hex
        pipe_bottom.pair_id = pair_id
        pipe_top.pair_id = pair_id
        return [pipe_bottom, pipe_top]
