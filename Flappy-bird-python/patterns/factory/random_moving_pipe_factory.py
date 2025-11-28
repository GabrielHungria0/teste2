import random
from typing import List
import uuid
from config import PIPE_GAP, SCREEN_HEIGHT
from entities.moving_pipe import MovingPipe
from entities.pipe import Pipe
from patterns.factory.abstract_factory import ObstacleFactory


class RandomMovingPipeFactory(ObstacleFactory):

    def create_obstacle(self, xpos, resource_facade) -> List[Pipe]:
        size = random.randint(100, 300)

        movement_range = random.randint(30, 70)
        movement_speed = random.uniform(1.5, 3.5)

        pipe_bottom = MovingPipe(
            inverted=False,
            xpos=xpos,
            ysize=size,
            resource_facade=resource_facade,
            movement_range=movement_range,
            movement_speed=movement_speed,
        )

        pipe_top = MovingPipe(
            inverted=True,
            xpos=xpos,
            ysize=SCREEN_HEIGHT - size - PIPE_GAP,
            resource_facade=resource_facade,
            movement_range=movement_range,
            movement_speed=movement_speed,
        )

        # Marca o par com um id único
        pair_id = uuid.uuid4().hex
        pipe_bottom.pair_id = pair_id
        pipe_top.pair_id = pair_id
        return [pipe_bottom, pipe_top]
