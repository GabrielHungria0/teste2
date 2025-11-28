from typing import List
from patterns.event import Event, GameOverEvent, PipePassedEvent, ResetEvent
from patterns.observer.abstract_game_event_observer import AbstractGameEventObserver


class ScoreObserver(AbstractGameEventObserver):

    def __init__(self):
        self.score = 0

    def update(self, event: Event):
        if isinstance(event, PipePassedEvent):
            self.score += event.score
        elif isinstance(event, GameOverEvent):
            print(f"Game Over Pontuação final: {self.score}")
        elif isinstance(event, ResetEvent):
            self.score = 0
            print("Pontuação resetada!")

    def get_score(self):
        return self.score

    def get_event_types(self) -> List[type]:
        return [PipePassedEvent, GameOverEvent, ResetEvent]
