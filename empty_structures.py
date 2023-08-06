import copy

from utilities import make_prompt, load_prompt


class EmptyStructures:
    _npc = None

    def __init__(self):
        # TODO this prompt load doesn't belong here, it needs to move
        EmptyStructures._npc = load_prompt("npc-structure")

    # TODO this function doesn't belong here, it needs to move
    # @classmethod
    # def get_npc_structure_prompt(cls):
    #     return make_prompt(cls._npc)
    #
    # @classmethod
    # def get_npc_structure(cls):
    #     return copy.deepcopy(cls._npc)

    @classmethod
    def get_player_structure(cls):
        # implement this function
        pass

    # TODO this function doesn't belong here, it needs to move
    @classmethod
    def get_player_structure_prompt(cls):
        # implement this function
        pass

    @classmethod
    def get_treasure_structure(cls):
        return copy.deepcopy(cls.__empty_treasure)

    @classmethod
    def create_empty_player(cls):
        return cls.__empty_player.copy()

    __empty_party = []
    __empty_skirmish_encounter = {}
    __empty_boss_encounter = {}
    __empty_social_encounter = {}
    __empty_rest_encounter = {}
    __empty_hazard_encounter = {}

    # __empty_connection = {
    #     "connects_to": "",
    #     "direction": "",
    #     "navigation": ""
    # }

    # __empty_location = {
    #     "id": "",
    #     "name": "",
    #     "encounter": {},
    #     "full_description": "",
    #     "brief_description": "",
    #     "noteworthy": "",
    #     "connections": []
    # }

    __empty_puzzle_encounter = {
        ""
        "puzzle_stages": [
            {
                "description": "",
                "clues": [""],
                "solution_verification": ""
            }
        ],
        "partial_success": {
            "enabled": '',
            "partial_clue": "",
            "reduced_consequences": ""
        }

    }

    __empty_encounter = {
        "type": "",
        "description": "",
        "difficulty_level": "",
        "details": {}  # attach a puzzle structure or a skirmish structure or a hazard structure or a boss fight structure
    }
    #
    # __empty_environment = {
    #     "type": "",
    #     "name": "",
    #     "description": "",
    #     "climate": {
    #         "type": "",
    #         "season": "",
    #         "weather": ""
    #     },  # replace with the climate structure
    # }

    __empty_scenario = {
        "title": "",
        "party_size": '',
        "level": '',
        "environment": {},  # replace with the environment structure
        "scenario": "",
        "starting_area": "",
        "quest": "",
        "quest_objective": "",
        "side_quest": "",
        "side_quest_objective": "",
        "locations": []
    }

    __empty_player = {
        'player': "",
        'location': "",
        'level': 0,
        'class': {
            'name': '',
            'description': 'get_player_class_description(string name of player)'
        },
        'HP': 0,
        'age': 0,
        'sex': '',
        'race': '',
        'Alignment': '',
        'background': {
            'name': '',
            'description': 'get_player_background_description(string name of player)'
        },
        'strength': {
            'actual': 0,
            'base': 0,
            'modifier': 0,
            'racial bonus': 0
        },
        'dexterity': {
            'actual': 0,
            'base': 0,
            'modifier': 0,
            'racial bonus': 0
        },
        'constitution': {
            'actual': 0,
            'base': 0,
            'modifier': 0,
            'racial bonus': 0
        },
        'intelligence': {
            'actual': 0,
            'base': 0,
            'modifier': 0,
            'racial bonus': 0
        },
        'Wisdom': {
            'actual': 0,
            'base': 0,
            'modifier': 0,
            'racial bonus': 0
        },
        'charisma': {
            'actual': 0,
            'base': 0,
            'modifier': 0,
            'racial bonus': 0
        },
        'ac': {
            'value': 0,
            'derived': ''
        },
        'speed': 0,
        'equipment': [''],
        'coins': {
            'gold': 0,
            'silver': 0,
            'copper': 0
        },
        'fighting style': '',
        'proficiencies': [''],
        'proficiency bonus': 0,
        'abilities': [
            {
                'name': '',
                'level': 0,
                'description': 'get_player_abilities_description(name of the ability to describe)'
            },
        ],
        'features': [
            {
                'name': '',
                'value': ''
            },
        ],
        'companion': {
            'name': '',
            'location': '',
            'race': '',
            'gender': '',
            'color': '',
            'size': '',
            'AC': 0,
            'HP': 0,
            'Speed': 0,
            'strength': {
                'actual': 0,
                'modifier': 0
            },
            'dexterity': {
                'actual': 0,
                'modifier': 0
            },
            'constitution': {
                'actual': 0,
                'modifier': 0
            },
            'intelligence': {
                'actual': 0,
                'modifier': 0
            },
            'wisdom': {
                'actual': 0,
                'modifier': 0
            },
            'charisma': {
                'actual': 0,
                'modifier': 0
            },
            'skills': [''],
            'traits': [
                {
                    'name': '',
                    'description': ''
                }
            ]
        },
        'languages': [''],
        'hit_dice': '',
        'short_rest_recovery': '',
        'XP': 0,
        'xp_for_next_level': 0
    }

    __empty_treasure = {
        "type": "",
        "description": "",
        "noteworthy": "",
        "locked": {
            "is_locked": "",
            "description": ""
        },
        "is_trapped": "",
        "trap": {
            "type": "",
            "status": "undetected",
            "effect": "",
            "description": "",
            "detection_difficulty": "",
            "disarm_difficulty": "",
            "damage": "",
            "dodge_difficulty": ""
        },
        "contents": {
            "coins": {
                "copper": "",
                "silver": "",
                "gold": ""
            },
            "gems": [
            ],
            "items": [
            ]
        }

    }

    __empty_gem = {
        'type': '',
        'size': '',
        'designation': '',
        'GP': '',
        'description': ''
    }

    __empty_money = {
        'gp': '',
        'sp': '',
        'cp': ''
    }

    __empty_treasure_vessel = {
        'type': '',
        'size': '',
        'designation': '',
        'value': '',
        'text': '',
        'description': '',
        'noteworthy': ''
    }

    @classmethod
    def get_scenario_structure(cls):
        return copy.deepcopy(cls.__empty_scenario)

    @classmethod
    def get_encounter_structure(cls):
        return copy.deepcopy(cls.__empty_encounter)

    @classmethod
    def get_connection_structure(cls):
        return copy.deepcopy(cls.__empty_connection)
