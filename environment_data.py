from environment_types import EnvironmentData
from climate_type import *
from zone_data import *

ENV_WILDERNESS_HIGHLAND = EnvironmentData(
    name="highland wilderness",
    minimum_level=1,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE],
    zones=[ZONE_OUTPOST2])

ENV_WATCH_TOWER_ABANDONED = EnvironmentData(
    name="abandoned watch tower",
    minimum_level=1,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
    zones=[ZONE_WATCHTOWER2, ZONE_RIVER2, ZONE_WOODLAND2])

ENV_WATCH_TOWER_HAUNTED = EnvironmentData(
    name="haunted watch tower",
    minimum_level=3,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
    zones=[ZONE_WATCHTOWER2])

ENV_WATCH_TOWER_EVIL = EnvironmentData(
    name="evil watch tower",
    minimum_level=7,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
    zones=[ZONE_WATCHTOWER2])

ENV_WATCH_TOWER_POPULATED = EnvironmentData(
    name="populated watch tower",
    minimum_level=1,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
    zones=[ZONE_WATCHTOWER2])

ENV_VILLAGE_ABANDONED = EnvironmentData(
    name="abandoned village",
    minimum_level=1,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
    zones=[ZONE_VILLAGE2])

ENV_VILLAGE_POPULATED = EnvironmentData(
    name="populated village",
    minimum_level=1,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
    zones=[ZONE_VILLAGE2])

ENV_VILLAGE_POPULATED_FISHING = EnvironmentData(
    name="populated fishing village",
    minimum_level=1,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
    zones=[ZONE_VILLAGE2])

ENV_VILLAGE_FORTIFIED = EnvironmentData(
    name="fortified village",
    minimum_level=1,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
    zones=[ZONE_VILLAGE2])

ENV_VILLAGE_HAUNTED = EnvironmentData(
    name="haunted village",
    minimum_level=3,
    maximum_level=10,
    climates=[CLIMATE_TEMPERATE],
    zones=[ZONE_VILLAGE2])

ENVIRONMENT_DB:[EnvironmentData] = [
    ENV_VILLAGE_HAUNTED,
    ENV_VILLAGE_FORTIFIED,
    ENV_VILLAGE_POPULATED_FISHING,
    ENV_VILLAGE_POPULATED,
    ENV_VILLAGE_ABANDONED,
    ENV_WATCH_TOWER_POPULATED,
    ENV_WATCH_TOWER_EVIL,
    ENV_WATCH_TOWER_HAUNTED,
    ENV_WATCH_TOWER_ABANDONED,
    ENV_WILDERNESS_HIGHLAND,
]
