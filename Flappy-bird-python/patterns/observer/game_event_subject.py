from typing import Dict, List

from patterns.event import Event
from patterns.observer.abstract_game_event_observer import AbstractGameEventObserver
from patterns.observer.null_observer import NullEventObserver


class GameEventSubject:

    def __init__(self):
        self._observers: Dict[type, List[AbstractGameEventObserver]] = {}

    def attach(self, observer: AbstractGameEventObserver):
        for t in observer.get_event_types():
            if self._observers.get(t) is None:
                self._observers[t] = []

            self._observers[t].append(observer)

    def detach(self, observer: AbstractGameEventObserver):
        for t in observer.get_event_types():
            if self._observers.get(t) is not None:
                if observer in self._observers[t]:
                    self._observers[t].remove(observer)

    def notify(self, event: Event):
        if self._observers.get(type(event)) is not None:
            for obs in self._observers[type(event)]:
                obs.update(event)
