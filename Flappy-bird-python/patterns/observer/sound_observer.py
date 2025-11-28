from typing import List
import pygame
from config import HIT_SOUND, WING_SOUND
from patterns.event import CollisionEvent, Event, JumpEvent
from patterns.loader.asset_loader import AssetLoader
from patterns.observer.abstract_game_event_observer import AbstractGameEventObserver
from patterns.service.sound_service import SoundService


class SoundObserver(AbstractGameEventObserver):

    def __init__(self):
        self.service = SoundService()

    def update(self, event: Event):
        if isinstance(event, CollisionEvent):
            self.service.play(HIT_SOUND, "hit")

        elif isinstance(event, JumpEvent):
            self.service.play(WING_SOUND, "wing")

    def get_event_types(self) -> List[type]:
        return [CollisionEvent, JumpEvent]
