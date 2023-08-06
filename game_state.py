import json
import os

from actions import Actions
from historical_summary import HistoricalSummary
from npcs import NPCs
from player_type import Players
from scenario import Scenario


class GameState:
    _instance = None
    _non_player_characters = None
    _players = None
    _scenario = None
    _performed_actions = None
    _historical_info = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameState, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.load_state()

    @classmethod
    def load_state(cls):
        cls._non_player_characters = NPCs()
        cls._players = Players()
        cls._scenario = Scenario()
        cls._performed_actions = Actions()
        cls._historical_info = HistoricalSummary()


GameState()
