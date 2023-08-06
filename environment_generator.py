import random
from pprint import pprint

from adjective_data import ADJECTIVES_DB
from empty_structures import EmptyStructures
from constants import *
from environment_types import EnvironmentData, Environment
from location_types import LocationData
from world_types import WorldData
from zone_types import ZoneData


class EnvironmentGenerator:

    #
    #     # {
    #     #     "type": "oasis",
    #     #
    #     #     "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
    #     #     "climates": [CLIMATE_ALPINE, CLIMATE_DESERT]
    #     # },
    #     # {
    #     #     "type": "mountainous",
    #     #     "subtypes": [],
    #     #     "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
    #     #     "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE]
    #     # },
    #     # {
    #     #     "type": "ruins",
    #     #     "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
    #     #     "climates": [CLIMATE_TEMPERATE, CLIMATE_DESERT, CLIMATE_TROPICAL, CLIMATE_ALPINE, CLIMATE_POLAR]
    #     # },
    #     # {
    #     #     "type": "dungeon",
    #     #     "seasons": [SEASON_CONSTANT],
    #     #     "climates": [CLIMATE_SUBTERRANEAN],
    #     #     "locations": []
    #     # },
    #     # {"type": "underground caverns", "seasons": [SEASON_CONSTANT], "climates": [CLIMATE_SUBTERRANEAN]},
    #     # {"type": "swampland", "seasons": ["spring", "summer", "autumn", "winter"], "climates": [CLIMATE_TROPICAL, CLIMATE_TEMPERATE]},
    #     # {"type": "coastal", "seasons": ["spring", "summer", "autumn", "winter"], "climates": [CLIMATE_TROPICAL, CLIMATE_TEMPERATE, CLIMATE_POLAR]},
    #     # {"type": "urban", "seasons": ["spring", "summer", "autumn", "winter"], "climates": [CLIMATE_TEMPERATE, CLIMATE_DESERT, CLIMATE_TROPICAL, CLIMATE_POLAR]},
    #     # {"type": "arctic", "seasons": [SEASON_SUMMER, SEASON_WINTER], "climates": [CLIMATE_POLAR]},
    #     # {"type": "jungle", "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER], "climates": [CLIMATE_TROPICAL]},
    # ]

    @classmethod
    def generate_random_environment(cls):
        environment_type = random.choice(WorldData.environments)
        climate = random.choice(environment_type.climates)
        season = random.choice(climate.possible_seasons)
        environment = Environment(environment_type)
        environment.climate = climate
        environment.season = season

        return environment

    # @classmethod
    # def verify_locations(cls, locations, encounter_types, valid_adjectives):
    #     descriptors = []
    #     for location in locations:
    #         # Check if all required fields are in each location
    #         if not all(k in location for k in ("descriptor", "adjectives", "encounters")):
    #             missing_keys = [k for k in ("descriptor", "adjectives", "encounters") if k not in location]
    #             raise ValueError(f"Location {location} is missing keys: {missing_keys}")
    #
    #         # Check if the descriptor is unique
    #         if location['descriptor'] in descriptors:
    #             raise ValueError(f"Descriptor '{location['descriptor']}' is not unique.")
    #         descriptors.append(location['descriptor'])
    #
    #         # Check if there's at least one adjective and no duplicate adjectives
    #         if not location['adjectives'] or len(location['adjectives']) != len(set(location['adjectives'])):
    #             if not location['adjectives']:
    #                 raise ValueError(f"Location {location['descriptor']} does not contain any adjectives.")
    #             else:
    #                 raise ValueError(f"Location {location['descriptor']} contains duplicate adjectives.")
    #
    #         # Check if the adjectives are in the valid_adjectives list
    #         invalid_adjectives = set(location['adjectives']) - set(valid_adjectives)
    #         if invalid_adjectives:
    #             raise ValueError(f"Location {location['descriptor']} contains invalid adjectives: {invalid_adjectives}")
    #
    #         # Check if there's at least one encounter
    #         if not location['encounters']:
    #             raise ValueError(f"Location {location['descriptor']} does not contain any encounters.")
    #
    #         # Check if all encounters are valid and there are no duplicates
    #         invalid_encounters = set(location['encounters']) - set(encounter_types)
    #         duplicate_encounters = len(location['encounters']) != len(set(location['encounters']))
    #         if invalid_encounters:
    #             raise ValueError(f"Location {location['descriptor']} contains invalid encounters: {invalid_encounters}")
    #         elif duplicate_encounters:
    #             raise ValueError(f"Location {location['descriptor']} contains duplicate encounters.")
    #
    #     return True

    # @classmethod
    # def verify_zones(cls, zones, locations):
    #     location_descriptors = {location['descriptor'] for location in locations}
    #     for zone in zones:
    #         # print(f"Checking zone {zone}")
    #         # Check if 'zone' key is present and is a string
    #         if 'zone' not in zone or not isinstance(zone['zone'], str):
    #             raise ValueError(f"Zone entry {zone} does not contain a 'zone' key or the key is not a string.")
    #
    #         cls.verify_locations_to_use(zone)
    #         cls.verify_locations_list(location_descriptors, zone)
    #
    #     return True
    #
    # @classmethod
    # def verify_locations_list(cls, location_descriptors, zone):
    #     # Check 'locations' key exists, is a list, and has at least one entry
    #     if 'locations' not in zone or not isinstance(zone['locations'], list) or not zone['locations']:
    #         raise ValueError(f"Zone {zone['zone']} does not contain a 'locations' key, or the key is not a list, or the list is empty.")
    #     # Check all items in 'locations' list exist in location_descriptors and there are no duplicates
    #     for location in zone['locations']:
    #         if location['descriptor'] not in location_descriptors:
    #             raise ValueError(f"Zone {zone['zone']} contains invalid location: {location['descriptor']}")
    #     # print([location['descriptor'] for location in zone['locations']])
    #     # print(len(zone['locations']))
    #     if len(zone['locations']) != len(set([location['descriptor'] for location in zone['locations']])):
    #         from collections import Counter
    #         location_counts = Counter(zone['locations'])
    #         duplicates = [k for k, v in location_counts.items() if v > 1]
    #         raise ValueError(f"Zone {zone['zone']} contains duplicate locations: {duplicates}")

    # @classmethod
    # def verify_locations_to_use(cls, zone):
    #     # Check 'locations_to_use' key exists, is a dictionary, and has 'minimum' and 'maximum' keys
    #     if 'locations_to_use' not in zone or not isinstance(zone['locations_to_use'], dict):
    #         raise ValueError(f"Zone {zone['zone']} does not contain a 'locations_to_use' key or the key is not a dictionary.")
    #     if 'minimum' not in zone['locations_to_use'] or 'maximum' not in zone['locations_to_use']:
    #         raise ValueError(f"Zone {zone['zone']} does not contain 'minimum' and 'maximum' keys in 'locations_to_use'.")
    #     # Check 'minimum' and 'maximum' values are numeric and minimum is less than maximum
    #     if not isinstance(zone['locations_to_use']['minimum'], (int, float)) or not isinstance(zone['locations_to_use']['maximum'], (int, float)):
    #         raise ValueError(f"Zone {zone['zone']} has non-numeric 'minimum' or 'maximum' values in 'locations_to_use'.")
    #     if zone['locations_to_use']['minimum'] >= zone['locations_to_use']['maximum']:
    #         raise ValueError(f"Zone {zone['zone']} has 'minimum' value greater than or equal to 'maximum' in 'locations_to_use'.")

    # @classmethod
    # def verify_seasons(cls, seasons):
    #     if not isinstance(seasons, list) or not seasons:
    #         raise ValueError("The 'seasons' key must exist and it must be a non-empty list.")
    #     if len(seasons) != len(set(seasons)):
    #         from collections import Counter
    #         season_counts = Counter(seasons)
    #         duplicates = [k for k, v in season_counts.items() if v > 1]
    #         raise ValueError(f"'seasons' contains duplicate seasons: {duplicates}")
    #     if not set(seasons).issubset(SEASON_TYPES):
    #         invalid_seasons = set(seasons) - set(SEASON_TYPES)
    #         raise ValueError(f"'seasons' contains invalid seasons: {invalid_seasons}")
    #     return True

    # @classmethod
    # def verify_climates(cls, climates):
    #     if not isinstance(climates, list) or not climates:
    #         raise ValueError("The 'climates' key must exist and it must be a non-empty list.")
    #     if len(climates) != len(set(climates)):
    #         from collections import Counter
    #         climate_counts = Counter(climates)
    #         duplicates = [k for k, v in climate_counts.items() if v > 1]
    #         raise ValueError(f"'climates' contains duplicate climates: {duplicates}")
    #     if not set(climates).issubset(CLIMATE_TYPES):
    #         invalid_climates = set(climates) - set(CLIMATE_TYPES)
    #         raise ValueError(f"'climates' contains invalid climates: {invalid_climates}")
    #     return True

    @classmethod
    def validate_data(cls):
        cls.check_for_adjective_duplicates()
        cls.verify_world()

    @classmethod
    def check_for_adjective_duplicates(cls):
        # Converting the list to a set will remove any duplicates because sets cannot contain duplicate values
        # If the length of the set is less than the length of the list, that means there were duplicates
        if len(set(ADJECTIVES_DB)) < len(ADJECTIVES_DB):
            # Creating a dictionary with counts of each adjective
            from collections import Counter
            adj_counts = Counter(ADJECTIVES_DB)

            # Find the adjectives where count is more than 1, those are our duplicates
            duplicates = [k for k, v in adj_counts.items() if v > 1]
            raise ValueError(f"The following adjectives are duplicated: {duplicates}")

    # @classmethod
    # def verify_environments(cls, environments, zones):
    #     print(cls.LOC_MOUNTAIN_PASS2)
    #     for env in environments:
    #         pprint(env)
    #         if not isinstance(env, EnvironmentData):
    #             raise ValueError("This is not an environment type")
    #
    #         env.validate()
    #
    #         env_zone_names = [zone.name for zone in env.zones]
    #         valid_zone_names = [zone.name for zone in zones]
    #
    #         if not set(env_zone_names).issubset(valid_zone_names):
    #             invalid_zones = set(env_zone_names) - set(valid_zone_names)
    #             raise ValueError(f"'zones' contains invalid zones: {invalid_zones}")
    #
    #         if len(env_zone_names) != len(set(env_zone_names)):
    #             from collections import Counter
    #             zone_counts = Counter(env_zone_names)
    #             duplicates = [k for k, v in zone_counts.items() if v > 1]
    #             raise ValueError(f"'zones' contains duplicate zones: {duplicates}")
    #
    #         cls.verify_seasons(env.get('seasons', []))
    #         cls.verify_climates(env.get('climates', []))
    #
    #     return True

    # TODO create a list of environments that cover the specified level of the party
    # TODO pick a random environment from that list
    # TODO pick the season and climate that the environment supports
    # TODO decide on how manyy zones we will use and limit it to the number of zones in the environment
    # TODO select a random set of zones
    # TODO decide how many locations will be in each zone, this is zone specific, different zones will have a different number of locations
    # TODO select a random set of locations from the zone
    # TODO set the adjectives for the zone
    # TODO select a random encounter type for each location
    # TODO select the adjectives for the location
    # TODO select the nouns for the location
    # TODO build the graph for the environment
    # TODO set all of the connections for each location from the graph
    # TODO send the entire map to the GPT4 model to generate the descriptions for each location
    # TODO generate npcs for each skirmish & boss fight encounter
    # TODO generate loot for each skirmish & boss fight encounter
    # TODO generate the puzzles for each puzzle encounter
    # TODO generate the traps for each trap encounter
    # TODO generate the treasure for each puzzle encounter
    # TODO generate traps for each puzzle encounter
    # TODO generate the social encounters for each social encounter
    # TODO generate the main quest
    # TODO generate the side quest
    # TODO generate the npcs for the main quest
    # TODO generate the npcs for the side quest
    # TODO generate the loot for the main quest
    # TODO generate the loot for the side quest
    # TODO generate how each hazard encounter will manifest itself
    # TODO generate how each exploration encounter will manifest itself
    @classmethod
    def verify_world(cls):
        WorldData.validate()


EnvironmentGenerator.validate_data()
