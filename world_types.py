import random

from adjective_data import *
from climate_type import *
from environment_data import ENVIRONMENT_DB
from environment_types import Environment
from location_data import LOCATIONS_DB
from season_data import SEASONS_DB
from zone_data import ZONE_DB


class WorldData:
    environments = ENVIRONMENT_DB
    zones = ZONE_DB
    locations = LOCATIONS_DB
    adjectives = ADJECTIVES_DB
    seasons = SEASONS_DB
    climates = CLIMATES_DB

    @classmethod
    def validate(cls):
        for environment in ENVIRONMENT_DB:
            environment.validate()


class GameWorld:
    def __init__(self, environment: Environment = None):
        self.environment = environment


    @staticmethod
    def generate_random_world():
        world = GameWorld()
        environment_type = random.choice(WorldData.environments)
        climate = random.choice(environment_type.climates)
        season = random.choice(climate.seasons)
        environment = Environment(environment_type)
        environment.climate = climate
        environment.season = season
        world.environment = environment
        world.environment.select_random_zones()
        return world
