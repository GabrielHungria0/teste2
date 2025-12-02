from patterns.chain_of_responsibility.difficulty_level import DifficultyLevel
from patterns.factory.alternating_move_pipe_factory import AlternatingMovingPipeFactory


class Level4(DifficultyLevel):
    def get_threshold(self):
        return 10
    
    def create_factory(self):
        return AlternatingMovingPipeFactory()
