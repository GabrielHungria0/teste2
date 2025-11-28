
from abc import ABC, abstractmethod
import pygame
from config import HIT_SOUND, WING_SOUND



class GameEventObserver(ABC):
    
    @abstractmethod
    def update(self, event_type, data=None):
        pass


class ScoreObserver(GameEventObserver):
    
    def __init__(self):
        self.score = 0
    
    def update(self, event_type, data=None):
        if event_type == "PIPE_PASSED":
            self.score += 1
        elif event_type == "GAME_OVER":
            print(f"Game Over Pontuação final: {self.score}")
        elif event_type == "RESET":
            self.score = 0
            print("Pontuação resetada!")
    
    def get_score(self):
        return self.score


class SoundObserver(GameEventObserver):
    
    def update(self, event_type, data=None):
        if event_type == "COLLISION":
            pygame.mixer.music.load(HIT_SOUND)
            pygame.mixer.music.play()
        elif event_type == "JUMP":
            pygame.mixer.music.load(WING_SOUND)
            pygame.mixer.music.play()


class GameEventSubject:
    
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, event_type, data=None):
        for observer in self._observers:
            observer.update(event_type, data)