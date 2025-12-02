from patterns.chain_of_responsibility.difficulty_level import DifficultyLevel
from patterns.factory.moving_pipe_factory import MovingPipeFactory


class Level2(DifficultyLevel):
    def get_threshold(self):
        return 3
    
    def create_factory(self):
        return MovingPipeFactory()
