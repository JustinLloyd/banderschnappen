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

class Encounter:
    def __init__(self, data:EncounterData = None):
        self.name = data.name if data else ''
        self.description = data.description if data else ''
        self.difficulty_level = data.challenge_rating if data else 1
        self.details = ''

class SkirmishEncounter(Encounter):
    def __init__(self, data:EncounterData = None):
        super().__init__(data)
        self.npcs= []

class PuzzleStage:
    def __init__(self, description: str = None, clues: [str] = None, solution_verification: str = None):
        self.description = description
        self.clues = clues
        self.solution_verification = solution_verification


class PuzzleEncounter(Encounter):
    def __init__(self, data:EncounterData = None):
        super().__init__(data)
        self.puzzle_stages = []
        self.partial_success_enabled= False
        self.partial_success_clue = ''
        self.reduced_consequences = ''


    __empty_encounter = {
        "type": "",
        "description": "",
        "difficulty_level": "",
        "details": {}  # attach a puzzle structure or a skirmish structure or a hazard structure or a boss fight structure
    }


