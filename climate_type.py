import random
from statistics import mean
from season_data import *
from season_types import Season


class ClimateData:
    def __init__(self, name: str = None, description: str = None, seasons: [SeasonData] = None, minimum_temperature: int = -40, maximum_temperature: int = 130):
        self.name = name
        self.seasons = seasons
        self.minimum_temperature = minimum_temperature
        self.maximum_temperature = maximum_temperature
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "seasons": [season.to_dict() for season in self.seasons],
            "minimum_temperature": self.minimum_temperature,
            "maximum_temperature": self.maximum_temperature
        }


class Climate:
    def __init__(self, data: ClimateData = None):
        self.name = data.name
        self.possible_seasons = [Season(season) for season in data.seasons]
        self.season = None
        self.minimum_temperature = data.minimum_temperature
        self.maximum_temperature = data.maximum_temperature
        self.description = data.description
        self.weather = ''
        self.temperature = mean([data.minimum_temperature, data.maximum_temperature])

    def generate_random_climate(self):
        self.season = Season(random.choice(self.possible_seasons))
        self.weather = '$describe the weather based on the season, temperature, and other factors'
        self.temperature = random.randint(max(self.minimum_temperature, self.season.minimum_temperature), min(self.maximum_temperature, self.season.maximum_temperature))

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "season": self.season.to_dict(),
            "weather": self.weather,
            "minimum_temperature": self.minimum_temperature,
            "maximum_temperature": self.maximum_temperature,
            "temperature": self.temperature,
            "possible_seasons": [season.to_dict() for season in self.possible_seasons]
        }
