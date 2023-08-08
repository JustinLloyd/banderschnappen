import copy
import random

from location_types import LocationData, Location


class ZoneData:
    def __init__(self, name=None, adjectives=None, locations=None, minimum_locations_to_use=0, maximum_locations_to_use=0):
        self.name = name
        self.adjectives = adjectives
        self.locations = locations
        self.minimum_locations_to_use = minimum_locations_to_use
        self.maximum_locations_to_use = maximum_locations_to_use

    def __str__(self):
        return f"{self.name} {self.adjectives}"

    def validate(self):
        if not self.name:
            raise ValueError("Each zone must have a name, and it cannot be empty.")

        # if not self.adjectives or not isinstance(self.adjectives, list):
        #     raise ValueError(f"Each zone must have an adjectives list, and it cannot be empty. {self.name} is missing any adjectives.")

        if not self.locations or not isinstance(self.locations, list):
            raise ValueError(f"Each zone must have a locations list, and it cannot be empty. {self.name} is missing any locations.")

        if not isinstance(self.minimum_locations_to_use, int) or not isinstance(self.maximum_locations_to_use, int):
            raise ValueError(f"Minimum and maximum locations to use must be integers in {self.name}")

        if self.minimum_locations_to_use > self.maximum_locations_to_use:
            raise ValueError(f"Minimum locations to use must be less than maximum locations to use in {self.name}.")

        for location in self.locations:
            if not isinstance(location, LocationData):
                raise ValueError(f"Each location must be a LocationData object. {location} is not a LocationData object in zone f{self.name}.")
            location.validate()

        if self.adjectives and isinstance(self.adjectives, list):
            for adjective in self.adjectives:
                if not isinstance(adjective, str):
                    raise ValueError(f"Each adjective must be a string. {adjective} is not a string  in zone f{self.name}.")

            # only test for duplicate adjectives if there are actually adjectives
            if len(self.adjectives) != len(set(self.adjectives)):
                raise ValueError(f"The adjectives list cannot contain duplicate values for zone f{self.name}.")

        if self.maximum_locations_to_use > len(self.locations):
            raise ValueError(f"The maximum locations to use value of {self.maximum_locations_to_use} is greater than the number of locations in the locations list for zone f{self.name}.")

        if self.minimum_locations_to_use > len(self.locations):
            raise ValueError(f"The minimum locations to use value of {self.minimum_locations_to_use} is greater than the number of locations in the locations list for zone f{self.name}.")

    def to_dict(self):
        return {
            "name": self.name,
            "adjectives": self.adjectives if self.adjectives else [],
            "locations": [location.to_dict() for location in self.locations],
            "minimum_locations_to_use": self.minimum_locations_to_use,
            "maximum_locations_to_use": self.maximum_locations_to_use
        }

class Zone:
    def __init__(self, data=None):
        self.name = data.name
        self.possible_adjectives = copy.deepcopy(data.adjectives)
        self.possible_locations = copy.deepcopy(data.locations)
        self.minimum_locations_to_use = data.minimum_locations_to_use
        self.maximum_locations_to_use = data.maximum_locations_to_use
        self.depth = 0
        self.locations = []
        self.adjectives = None

    def randomize_zone(self):
        self.select_random_adjectives()
        self.select_random_locations()

    def select_random_adjectives(self):
        if self.possible_adjectives:
            self.adjectives = random.sample(self.possible_adjectives, min(0, min(len(self.possible_adjectives), 2)))

    def select_random_locations(self):
        number_of_locations = random.randint(self.minimum_locations_to_use, self.maximum_locations_to_use)
        selected_locations = random.sample(self.possible_locations, number_of_locations)
        for location_data in selected_locations:
            location = Location(location_data)
            location.depth = random.randint(1, len(selected_locations))
            location.zone = self
            location.randomize_location()
            self.locations.append(location)

    def __str__(self):
        return f"{self.name} (depth {self.depth})"

    def constructed_name(self):
        return f"{self.name}_{self.depth}"

    def to_dict(self):
        return {
            "name": self.name,
            "adjectives": self.adjectives if self.adjectives else [],
            "possible_adjectives": self.possible_adjectives if self.possible_adjectives else [],
            "possible_locations": [location.to_dict() for location in self.possible_locations],
            "locations": [location.to_dict() for location in self.locations],
            "minimum_locations_to_use": self.minimum_locations_to_use,
            "maximum_locations_to_use": self.maximum_locations_to_use,
            "depth": self.depth
        }
