from abc import ABC, abstractmethod

class BirdState(ABC):
    @abstractmethod
    def update(self, bird):
        pass
    
    @abstractmethod
    def bump(self, bird):
        pass
    
    @abstractmethod
    def can_collide(self):
        pass
