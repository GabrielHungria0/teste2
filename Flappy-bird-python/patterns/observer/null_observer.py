from typing import List
from patterns.event import Event
from patterns.observer.abstract_game_event_observer import AbstractGameEventObserver


class NullEventObserver(AbstractGameEventObserver):
    def update(self, event: Event):
        pass

    def get_event_types(self) -> List[type]:
        return []
