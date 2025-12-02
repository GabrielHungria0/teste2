from typing import List
from patterns.event import CollisionEvent, Event, JumpEvent
from patterns.observer.abstract_game_event_observer import AbstractGameEventObserver
from service.sound_service import SoundService


class SoundObserver(AbstractGameEventObserver):
    """Observador que reproduz sons em resposta a eventos do jogo."""
    def __init__(self, resource_facade):
        self._sound_service = SoundService()
        self._resource_facade = resource_facade

    def update(self, event: Event):
        """Reproduz som apropriado baseado no tipo de evento."""
        sound_map = {
            CollisionEvent: "hit",
            JumpEvent: "wing"
        }
        sound_name = sound_map.get(type(event))
        if sound_name:
            sound = self._resource_facade.get_sound(sound_name)
            if sound:
                self._sound_service.play(sound)
                
    def get_event_types(self) -> List[type]:
        return [CollisionEvent, JumpEvent]