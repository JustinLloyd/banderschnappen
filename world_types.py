import json
import random
from dataclasses import dataclass

from actions import Actions
from adjective_data import *
from climate_data import CLIMATES_DB
from climate_type import *
from environment_data import ENVIRONMENT_DB
from environment_types import Environment, EnvironmentData
from historical_summary import HistoricalSummary
from location_data import LOCATIONS_DB
from location_types import LocationData
from npcs import NPCs
from party_type import Party
from scenario import Scenario
from season_data import SEASONS_DB
from utilities import save_state_data
from zone_data import ZONE_DB
from zone_types import ZoneData


class WorldData:
    environments: [EnvironmentData] = ENVIRONMENT_DB
    zones: [ZoneData] = ZONE_DB
    locations: [LocationData] = LOCATIONS_DB
    adjectives: [str] = ADJECTIVES_DB
    seasons: [SeasonData] = SEASONS_DB
    climates: [ClimateData] = CLIMATES_DB

    @classmethod
    def validate(cls):
        for environment in cls.environments:
            environment.validate()


class GameWorld:
    def __init__(self):
        self.non_player_characters = None
        self.party = None
        self.scenario = None

        self.performed_actions = None
        self.historical_info = None
        self.environment = None
        self.minutes_elapsed: int = 0
        self.time_of_day_started: int = 0

    def save_state(self):
        print(self.to_dict())
        save_state_data('world', self.to_dict())

    def load_state(self):
        self.non_player_characters = NPCs()
        self.non_player_characters.load_state()
        self.party = Party()
        self.party.load_state()
        self.scenario = Scenario()
        self.scenario.load_state()
        self.performed_actions = Actions()
        self.performed_actions.load_state()
        self.historical_info = HistoricalSummary()
        self.historical_info.load_state()

    @staticmethod
    def generate_random_world():
        new_world = GameWorld()
        environment_data_type = random.choice(WorldData.environments)
        climate_data = random.choice(environment_data_type.climates)
        # season_data = random.choice(climate_data.seasons)
        environment = Environment(environment_data_type)
        environment.climate = Climate(climate_data)
        environment.climate.generate_random_climate()
        # environment.season = Season(season_data)
        environment.build_environment()
        new_world.environment = environment
        return new_world

    def to_dict(self):
        return {
            #            'non_player_characters': self.non_player_characters.to_dict(),
            #            'party': self.party.to_dict(),
            #            'scenario': self.scenario.to_dict(),
            #            'performed_actions': self.performed_actions.to_dict(),
            #            'historical_info': self.historical_info.to_dict(),
            'environment': self.environment.to_dict(),
            'minutes_elapsed': self.minutes_elapsed,
            'time_of_day_started': self.time_of_day_started,
        }
