from climate_type import ClimateData
from season_data import SEASON_AUTUMN, SEASON_WINTER, SEASON_SPRING, SEASON_SUMMER, SEASON_CONSTANT

CLIMATE_TEMPERATE_KEY = "temperate"
CLIMATE_TEMPERATE = ClimateData(
    name=CLIMATE_TEMPERATE_KEY,
    description="Temperate climates are found in the middle latitudes, between the polar and tropical regions. These climates have four seasons, with warm summers and cold winters.",
    seasons=[SEASON_SPRING, SEASON_AUTUMN, SEASON_SUMMER, SEASON_WINTER],
    minimum_temperature=-5,
    maximum_temperature=80)

CLIMATE_DESERT_KEY = "desert"
CLIMATE_DESERT = ClimateData(
    name=CLIMATE_DESERT_KEY,
    description="Desert climates are found in the polar regions. These climates have two seasons, with hot summers and warm winters.",
    seasons=[SEASON_SUMMER, SEASON_WINTER],
    minimum_temperature=-10,
    maximum_temperature=130)

CLIMATE_TROPICAL_KEY = "tropical"
CLIMATE_TROPICAL = ClimateData(
    name=CLIMATE_TROPICAL_KEY,
    description="Tropical climates are found in the tropical regions. These climates have two seasons, with hot summers and wet winters.",
    seasons=[SEASON_SUMMER, SEASON_WINTER],
    minimum_temperature=60,
    maximum_temperature=110)

CLIMATE_ALPINE_KEY = "alpine"
CLIMATE_ALPINE = ClimateData(
    name=CLIMATE_ALPINE_KEY,
    description="Alpine climates are found in the polar regions. These climates have two seasons, with warm summers and cold winters.",
    seasons=[SEASON_SPRING, SEASON_AUTUMN, SEASON_SUMMER, SEASON_WINTER],
    minimum_temperature=-10,
    maximum_temperature=70)

CLIMATE_POLAR_KEY = "polar"
CLIMATE_POLAR = ClimateData(
    name=CLIMATE_POLAR_KEY,
    description="Polar climates are found in the polar regions. These climates have two seasons, with cold summers and even colder winters.",
    seasons=[SEASON_SUMMER, SEASON_WINTER],
    minimum_temperature=-40,
    maximum_temperature=30)

CLIMATE_TUNDRA_KEY = 'tundra'
CLIMATE_TUNDRA = ClimateData(
    name=CLIMATE_TUNDRA_KEY,
    description="Tundra climates are found in the polar regions. These climates have two seasons, with cool summers and cold winters.",
    seasons=[SEASON_SUMMER, SEASON_WINTER],
    minimum_temperature=-30,
    maximum_temperature=50)

CLIMATE_SUBTERRANEAN_KEY = "subterranean"
CLIMATE_SUBTERRANEAN = ClimateData(
    name=CLIMATE_SUBTERRANEAN_KEY,
    description="Subterranean climates are found in the polar regions. There are generally no seasons, with a constant temperature.",
    seasons=[SEASON_CONSTANT],
    minimum_temperature=30,
    maximum_temperature=70)

CLIMATES_DB = [CLIMATE_TEMPERATE, CLIMATE_DESERT, CLIMATE_TROPICAL, CLIMATE_ALPINE, CLIMATE_POLAR, CLIMATE_SUBTERRANEAN, CLIMATE_TUNDRA]
