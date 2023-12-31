import copy
import random
from typing import Optional, List

from adjective_data import ADJECTIVES_DB
from encounter_type import EncounterData, Encounter


class LocationData:
    def __init__(self, descriptor: Optional[str] = None, nouns: Optional[List[str]] = None, adjectives: Optional[List[str]] = None, encounters: Optional[List[str]] = None):
        self.descriptor = descriptor
        self.nouns = nouns
        self.adjectives = adjectives
        self.encounters = encounters

    def __str__(self) -> str:
        return f"{self.descriptor} {self.nouns} {self.adjectives} {self.encounters}"

    def validate(self):
        if not self.descriptor:
            raise ValueError("Each location must have a descriptor, and it cannot be empty.")

        if not isinstance(self.descriptor, str):
            raise ValueError(f"The descriptor must be a string. {self.descriptor} is not a string.")

        # if not self.nouns or not isinstance(self.nouns, list):
        #     raise ValueError("Each location must have a nouns list, and it cannot be empty.")

        if not self.adjectives or not isinstance(self.adjectives, list):
            raise ValueError(f"Each location must have an adjectives list, and it cannot be empty. {self.descriptor} is missing any adjectives.")

        # Check if the adjectives are in the valid_adjectives list
        invalid_adjectives = set(self.adjectives) - set(ADJECTIVES_DB)
        if invalid_adjectives:
            raise ValueError(f"Location {self.descriptor} contains invalid adjectives: {invalid_adjectives}")

        if not self.encounters or not isinstance(self.encounters, list):
            raise ValueError(f"Each location must have an encounters list, and it cannot be empty. {self.descriptor} is missing any encounters.")

        if len(self.encounters) < 1:
            raise ValueError(f"Each location must have at least one encounter. {self.descriptor} has no encounters.")

        for encounter in self.encounters:
            if not isinstance(encounter, EncounterData):
                raise ValueError(f"Each encounter must be an EncounterData object. {encounter} in {self.descriptor} is not an EncounterData object.")
            encounter.validate()

        encounter_descriptors = [encounter.name for encounter in self.encounters]
        if len(encounter_descriptors) != len(set(encounter_descriptors)):
            raise ValueError(f"The encounters list in {self.descriptor} cannot contain duplicate values.")

        for adjective in self.adjectives:
            if not isinstance(adjective, str):
                raise ValueError(f"Each adjective must be a string. {adjective} is not a string in {self.descriptor}.")

        if len(self.adjectives) != len(set(self.adjectives)):
            raise ValueError(f"The adjectives list cannot contain duplicate values in {self.descriptor}.")

        if self.nouns and isinstance(self.nouns, list):
            for noun in self.nouns:
                if not isinstance(noun, str):
                    raise ValueError(f"Each noun must be a string. {noun} is not a string in {self.descriptor}.")

            if len(self.nouns) != len(set(self.nouns)):
                raise ValueError("The nouns list cannot contain duplicate values in {self.descriptor}.")

    def to_dict(self):
        return {
            "descriptor": self.descriptor,
            "nouns": self.nouns if self.nouns else [],
            "adjectives": self.adjectives if self.adjectives else [],
            "encounters": [encounter.to_dict() for encounter in self.encounters]
        }

class Location:
    def __init__(self, data: LocationData = None):
        self.name: str = ''
        self.possible_nouns: [str] = []
        self.possible_adjectives: [str] = []
        self.possible_encounters: [str] = []
        self.encounter = None
        self.nouns: [str] = []
        self.adjectives = []
        self.depth = 0
        self.zone = None
        self.connections: ["connection_types.Connection"] = []
        if not data:
            return

        self.name = data.descriptor
        self.possible_nouns = copy.deepcopy(data.nouns)
        self.possible_adjectives = copy.deepcopy(data.adjectives)
        self.possible_encounters = copy.deepcopy(data.encounters)
        self.encounter = None
        self.nouns = []
        self.adjectives = []
        self.depth = 0
        self.zone = None
        self.connections: ["connection_types.Connection"] = []

    def add_connection(self, location: "connection_types.Connection"):
        self.connections.append(location)

    def select_random_nouns(self):
        if not self.possible_nouns:
            return
        self.nouns = random.sample(self.possible_nouns, random.randint(0, min(1, len(self.possible_nouns))))

    def select_random_adjectives(self):
        self.adjectives = random.sample(self.possible_adjectives, random.randint(0, min(2, len(self.possible_adjectives))))

    def select_random_encounter(self):
        encounter_data = random.choice(self.possible_encounters)
        self.encounter = Encounter(encounter_data)

    def randomize_location(self):
        self.select_random_nouns()
        self.select_random_adjectives()
        self.select_random_encounter()

    def constructed_name(self) -> str:
        return f"{self.zone.name}_{self.name}_{self.depth}"

    def __str__(self):
        return f"{self.name} (depth {self.depth}) in {self.zone.name}"

    def to_dict(self):
        return {
            "name": self.name,
            "nouns": self.nouns,
            "adjectives": self.adjectives if self.adjectives else [],
            "encounter": self.encounter.name,
            "connections": [connection.name for connection in self.connections]
        }
