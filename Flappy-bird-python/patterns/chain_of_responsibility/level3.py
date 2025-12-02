from patterns.chain_of_responsibility.difficulty_level import DifficultyLevel
from patterns.factory.narrow_pipe_factory import NarrowPipeFactory


class Level3(DifficultyLevel):
    def get_threshold(self):
        return 6
    
    def create_factory(self):
        return NarrowPipeFactory()