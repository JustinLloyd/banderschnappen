class EncounterData:
    def __init__(self, name: str = None, description: str = None, challenge_rating: int = None):
        self.name = name
        self.description = description
        self.challenge_rating = challenge_rating

    def validate(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Each encounter must have a name, it must be a string, and it cannot be empty.")

        if not self.description or not isinstance(self.description, str):
            raise ValueError(f"Encounter {self.name} must have a description, it must be a string, and it cannot be empty.")

        if self.challenge_rating is None or not isinstance(self.challenge_rating, int):
            raise ValueError(f"Encounter {self.name} must have a challenge rating, it must be an integer, and it cannot be empty.")

        if self.challenge_rating < 1 or self.challenge_rating > 5:
            raise ValueError(f"Encounter {self.name} must have a challenge rating between 1 and 5, inclusive.")

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "challenge_rating": self.challenge_rating
        }


class Encounter:
    def __init__(self, data: EncounterData = None):
        self.name = data.name if data else ''
        self.description = data.description if data else ''
        self.difficulty_level = data.challenge_rating if data else 1
        self.details = ''

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "difficulty_level": self.difficulty_level,
            "details": self.details
        }


class SkirmishEncounter(Encounter):
    def __init__(self, data: EncounterData = None):
        super().__init__(data)
        self.npcs = []

    def to_dict(self) -> dict:
        encounter_dict = {
            "npcs": self.npcs
        }
        encounter_dict.update(super().to_dict())
        return encounter_dict


class PuzzleStage:
    def __init__(self, description: str = None, clues: [str] = None, solution_verification: str = None):
        self.description = description
        self.clues = clues
        self.solution_verification = solution_verification

    def to_dict(self):
        return {
            "description": self.description,
            "clues": self.clues,
            "solution_verification": self.solution_verification
        }


class PuzzleEncounter(Encounter):
    def __init__(self, data: EncounterData = None):
        super().__init__(data)
        self.puzzle_stages = []
        self.partial_success_enabled = False
        self.partial_success_clue = ''
        self.reduced_consequences = ''

    def to_dict(self) -> dict:
        encounter_dict = {
            "puzzle_stages": [stage.to_dict() for stage in self.puzzle_stages],
            "partial_success_enabled": self.partial_success_enabled,
            "partial_success_clue": self.partial_success_clue,
            "reduced_consequences": self.reduced_consequences
        }
        encounter_dict.update(super().to_dict())
        return encounter_dict
