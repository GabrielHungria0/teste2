"""
Padrão FACTORY METHOD - Criação de obstáculos
"""
from abc import ABC, abstractmethod
import random
from entities.pipe import Pipe
import uuid
from entities.moving_pipe import MovingPipe
from config import SCREEN_HEIGHT, PIPE_GAP


class ObstacleFactory(ABC):
    
    @abstractmethod
    def create_obstacle(self, xpos, resource_facade):
        pass


class PipeFactory(ObstacleFactory):
    
    def create_obstacle(self, xpos, resource_facade):
        size = random.randint(100, 300)
        pipe_bottom = Pipe(False, xpos, size, resource_facade)
        pipe_top = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP, resource_facade)
        # Marca o par com um id único para facilitar contagem
        pair_id = uuid.uuid4().hex
        pipe_bottom.pair_id = pair_id
        pipe_top.pair_id = pair_id
        return [pipe_bottom, pipe_top]


class NarrowPipeFactory(ObstacleFactory):
    
    def create_obstacle(self, xpos, resource_facade):
        size = random.randint(100, 300)
        narrow_gap = PIPE_GAP - 30
        pipe_bottom = Pipe(False, xpos, size, resource_facade)
        pipe_top = Pipe(True, xpos, SCREEN_HEIGHT - size - narrow_gap, resource_facade)
        # Marca o par com um id único
        pair_id = uuid.uuid4().hex
        pipe_bottom.pair_id = pair_id
        pipe_top.pair_id = pair_id
        return [pipe_bottom, pipe_top]


class MovingPipeFactory(ObstacleFactory):
    
    def create_obstacle(self, xpos, resource_facade):
        size = random.randint(100, 300)
        
        pipe_bottom = MovingPipe(
            inverted=False, 
            xpos=xpos, 
            ysize=size,
            resource_facade=resource_facade,
            movement_range=40,
            movement_speed=2
        )
        
        pipe_top = MovingPipe(
            inverted=True, 
            xpos=xpos, 
            ysize=SCREEN_HEIGHT - size - PIPE_GAP,
            resource_facade=resource_facade,
            movement_range=40,
            movement_speed=2
        )
        
        # Marca o par com um id único
        pair_id = uuid.uuid4().hex
        pipe_bottom.pair_id = pair_id
        pipe_top.pair_id = pair_id
        return [pipe_bottom, pipe_top]


class AlternatingMovingPipeFactory(ObstacleFactory):
    
    def create_obstacle(self, xpos, resource_facade):
        size = random.randint(100, 300)
        
        pipe_bottom = MovingPipe(
            inverted=False, 
            xpos=xpos, 
            ysize=size,
            resource_facade=resource_facade,
            movement_range=50,
            movement_speed=2
        )
        
        pipe_top = MovingPipe(
            inverted=True, 
            xpos=xpos, 
            ysize=SCREEN_HEIGHT - size - PIPE_GAP,
            resource_facade=resource_facade,
            movement_range=50,
            movement_speed=2
        )
        # Inverte a direção inicial do pipe de cima
        pipe_top.movement_direction = -1
        
        # Marca o par com um id único
        pair_id = uuid.uuid4().hex
        pipe_bottom.pair_id = pair_id
        pipe_top.pair_id = pair_id
        return [pipe_bottom, pipe_top]


class RandomMovingPipeFactory(ObstacleFactory):
    
    def create_obstacle(self, xpos, resource_facade):
        size = random.randint(100, 300)
        
        movement_range = random.randint(30, 70)
        movement_speed = random.uniform(1.5, 3.5)
        
        pipe_bottom = MovingPipe(
            inverted=False, 
            xpos=xpos, 
            ysize=size,
            resource_facade=resource_facade,
            movement_range=movement_range,
            movement_speed=movement_speed
        )
        
        pipe_top = MovingPipe(
            inverted=True, 
            xpos=xpos, 
            ysize=SCREEN_HEIGHT - size - PIPE_GAP,
            resource_facade=resource_facade,
            movement_range=movement_range,
            movement_speed=movement_speed
        )
        
        # Marca o par com um id único
        pair_id = uuid.uuid4().hex
        pipe_bottom.pair_id = pair_id
        pipe_top.pair_id = pair_id
        return [pipe_bottom, pipe_top]