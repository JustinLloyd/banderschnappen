import copy
import random

import networkx as nx

from climate_type import ClimateData
from zone_types import ZoneData


class EnvironmentData:
    def __init__(self, name: str = None, minimum_level: int = 0, maximum_level: int = 0, zones: [ZoneData] = None, climates: [ClimateData] = None):
        self.name = name
        self.minimum_level = minimum_level
        self.maximum_level = maximum_level
        self.zones = zones
        self.climates = climates

    def __repr__(self):
        return f"{self.name} {self.minimum_level} {self.maximum_level} {self.zones} {self.climates}"

    def validate(self):
        if not self.name:
            raise ValueError("Each environment must have a name, and it cannot be empty.")

        if not isinstance(self.minimum_level, int) or not isinstance(self.maximum_level, int):
            raise ValueError("Minimum and maximum level must be integers.")

        if self.minimum_level >= self.maximum_level:
            raise ValueError("Minimum level must be less than maximum level.")

        if not self.zones or not isinstance(self.zones, list):
            raise ValueError("Each environment must have a zones list, and it cannot be empty.")

        for zone in self.zones:
            if not isinstance(zone, ZoneData):
                raise ValueError(f"Each zone must be a ZoneData object. {zone} is not a ZoneData object.")
            zone.validate()

        if not self.climates or not isinstance(self.climates, list):
            raise ValueError("Each environment must have a climates list, and it cannot be empty.")

        # TODO verify there are no duplicate climates


class Environment:
    def __init__(self, data: EnvironmentData = None):
        self.name = data.name
        self.minimum_level = data.minimum_level
        self.maximum_level = data.maximum_level
        self.possible_zones = copy.deepcopy(data.zones)
        self.climates = copy.deepcopy(data.climates)
        self.zones= None
        self.climate = None
        self.season = None
        self.level = 0
        self.description = ''
        self.depth = 0
        self.graph = nx.Graph()

    def select_random_zones(self):
        # TODO implement this
        zones = []
        selected_zones = random.sample(self.possible_zones, random.randint(len(self.possible_zones) // 2, len(self.possible_zones)))
        for zone in selected_zones:
            zone.randomize_zone()

    def __str__(self):
        return f"{self.name} (depth {self.depth})"
