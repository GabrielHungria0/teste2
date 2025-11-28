from abc import ABC, abstractmethod


class Event(ABC):
    pass


class PipePassedEvent(Event):
    def __init__(self, score):
        self.score = score


class GameOverEvent(Event):
    def __init__(self):
        pass


class ResetEvent(Event):
    def __init__(self):
        pass


class CollisionEvent(Event):
    def __init__(self):
        pass


class JumpEvent(Event):
    def __init__(self):
        pass
