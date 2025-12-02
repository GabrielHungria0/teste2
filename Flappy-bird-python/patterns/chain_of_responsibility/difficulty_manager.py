
from patterns.chain_of_responsibility.level1 import Level1
from patterns.chain_of_responsibility.level2 import Level2
from patterns.chain_of_responsibility.level3 import Level3
from patterns.chain_of_responsibility.level4 import Level4


class DifficultyManager:
    def __init__(self):
        self._last_score = 0
        self._chain = self._build_chain()
    
    def _build_chain(self):
        level1 = Level1()
        level2 = Level2()
        level3 = Level3()
        level4 = Level4()
        
        level1.set_next(level2).set_next(level3).set_next(level4)
        return level1
    
    def get_factory_for_score(self, score, current_factory):
        if score == self._last_score:
            return current_factory
        
        self._last_score = score
        return self._chain.handle(score, current_factory)