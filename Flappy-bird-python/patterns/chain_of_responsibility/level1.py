from patterns.chain_of_responsibility.difficulty_level import DifficultyLevel
from patterns.factory.factory import PipeFactory


class Level1(DifficultyLevel):
    def get_threshold(self):
        return 0
    
    def create_factory(self):
        return PipeFactory()