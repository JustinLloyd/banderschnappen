import copy
import json
import random

from chat_gpt import ChatGPT
from die_generator import DieGenerator
from empty_structures import EmptyStructures
from utilities import strip_descriptions, load_state_data, save_state_data, make_prompt


class Players:
    # A simple mapping of classes to their primary and secondary abilities.
    CLASS_ABILITIES = {
        "barbarian": ["strength", "constitution"],
        "bard": ["charisma", "dexterity"],
        "cleric": ["wisdom", "constitution"],
        "druid": ["wisdom", "constitution"],
        "fighter": ["strength", "constitution"],
        "monk": ["dexterity", "wisdom"],
        "paladin": ["strength", "charisma"],
        "ranger": ["dexterity", "wisdom"],
        "rogue": ["dexterity", "intelligence"],
        "sorcerer": ["charisma", "constitution"],
        "warlock": ["charisma", "constitution"],
        "wizard": ["intelligence", "constitution"]
    }

    RACE_ABILITY_BONUSES = {
        "dwarf": {"constitution": 2},
        "elf": {"dexterity": 2},
        "halfling": {"dexterity": 2},
        "human": {"strength": 1, "dexterity": 1, "constitution": 1, "intelligence": 1, "wisdom": 1, "charisma": 1},
        "dragonborn": {"strength": 2, "charisma": 1},
        "gnome": {"intelligence": 2},
        "half-elf": {"strength": 1, "dexterity": 1, "constitution": 1, "intelligence": 1, "wisdom": 1, "charisma": 2},
        "half-orc": {"strength": 2, "constitution": 1},
        "tiefling": {"intelligence": 1, "charisma": 2},
    }
    HIT_DICE_BY_CLASS = {
        "barbarian": 12,
        "bard": 8,
        "cleric": 8,
        "druid": 8,
        "fighter": 10,
        "monk": 8,
        "paladin": 10,
        "ranger": 10,
        "rogue": 8,
        "sorcerer": 6,
        "warlock": 8,
        "wizard": 6
    }

    XP_LEVEL_THRESHOLDS = [
        0,  # Level 1
        300,  # Level 2
        900,  # Level 3
        2700,  # Level 4
        6500,  # Level 5
        14000,  # Level 6
        23000,  # Level 7
        34000,  # Level 8
        48000,  # Level 9
        64000,  # Level 10
        85000,  # Level 11
        100000,  # Level 12
        120000,  # Level 13
        140000,  # Level 14
        165000,  # Level 15
        195000,  # Level 16
        225000,  # Level 17
        265000,  # Level 18
        305000,  # Level 19
        355000  # Level 20
    ]
    _instance = None
    _players = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Players, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.load_state()

    @classmethod
    def load_state(cls):
        cls._players = load_state_data('players')

    @classmethod
    def save_state(cls):
        save_state_data('players', cls._players)

    @classmethod
    def get_players_without_descriptions(cls):
        stripped_players = []
        for player in cls._players:
            stripped_player = strip_descriptions(player)
            if 'companion' in stripped_player:
                stripped_player['companion'] = strip_descriptions(stripped_player['companion'])
            stripped_players.append(stripped_player)
        return stripped_players

    @classmethod
    def get_players(cls):
        return cls._players

    @classmethod
    def generate_initial_age(cls, player):
        race = player['race'].lower()

        # Define a lookup dictionary for base_age and age_variation for each race
        race_age_data = {
            'human': {'base_age': 15, 'age_variation': 20},
            'elf': {'base_age': 100, 'age_variation': 100},
            'dwarf': {'base_age': 50, 'age_variation': 50},
            'halfling': {'base_age': 20, 'age_variation': 30},
            'gnome': {'base_age': 40, 'age_variation': 70},
            'dragonborn': {'base_age': 15, 'age_variation': 10},
            'orc': {'base_age': 12, 'age_variation': 10},
            'half-orc': {'base_age': 14, 'age_variation': 30},
            'half-elf': {'base_age': 20, 'age_variation': 80},
            'tiefling': {'base_age': 15, 'age_variation': 30},
            # add more races as needed...
        }

        # Fetch the base_age and age_variation based on the character's race
        base_age = race_age_data.get(race, {}).get('base_age', 15)  # default to human age if race not found
        age_variation = race_age_data.get(race, {}).get('age_variation', 20)  # default to human age variation if race not found

        # Calculate the final age
        age = base_age + random.randint(0, age_variation)

        return age

    @classmethod
    def generate_initial_hp(cls, class_name, constitution_modifier):
        base_hp = cls.HIT_DICE_BY_CLASS.get(class_name.lower(), 8)
        total_hp = base_hp + constitution_modifier
        return total_hp

    @classmethod
    def get_half_elf_bonus(cls, character_class, ability):
        # Get the primary and secondary abilities for the class.
        primary, secondary = cls.CLASS_ABILITIES[character_class.lower()]
        # Check if the ability is one of the main ones for the class.
        if ability.lower() in [primary, secondary]:
            return 1
        else:
            return 0

    @classmethod
    def get_racial_bonus(cls, ability_name, ability_score, character_race, character_class=None):
        if character_race.lower() == "half-elf":
            return cls.get_half_elf_bonus(character_class, ability_name)
        else:
            return cls.RACE_ABILITY_BONUSES[character_race.lower()].get(ability_name.lower(), 0)

    @staticmethod
    def calculate_ability_modifier(ability_score):
        return (ability_score - 10) // 2

    @staticmethod
    def get_starting_equipment(character_class):
        starter_packages = {
            'barbarian': ['GreatAxe', 'Two Handaxes', 'Explorer\'s Pack', 'Four Javelins'],
            'bard': ['Rapier', 'Diplomat\'s Pack', 'Lute', 'Leather Armor', 'Dagger'],
            'cleric': ['Mace', 'Scale Mail', 'Light Crossbow and 20 Bolts', 'Priest\'s Pack', 'Shield', 'Holy Symbol'],
            'druid': ['Wooden Staff', 'Leather Armor', 'Explorer\'s Pack', 'Druidic Focus'],
            'fighter': ['Longsword', 'Chain Mail', 'Light Crossbow and 20 Bolts', 'Dungeoneer\'s Pack', 'Shield', 'Two Handaxes'],
            'monk': ['Shortsword', 'Dungeoneer\'s Pack', '10 Darts'],
            'paladin': ['Longsword', 'Chain Mail', 'Shield', 'Holy Symbol', 'Priest\'s Pack', '5 Javelins'],
            'ranger': ['Longsword', 'Leather Armor', 'Longbow and 20 Arrows', 'Explorer\'s Pack'],
            'rogue': ['Rapier', 'Shortbow and 20 Arrows', 'Burglar\'s Pack', 'Leather Armor', 'Two Daggers'],
            'sorcerer': ['Quarterstaff', 'Component Pouch', 'Scholar\'s Pack', 'Two Daggers'],
            'warlock': ['Quarterstaff', 'Leather Armor', 'Scholar\'s Pack', 'Dagger', 'Component Pouch'],
            'wizard': ['Quarterstaff', 'Component Pouch', 'Scholar\'s Pack', 'Spellbook', 'Dagger'],
        }

        if character_class in starter_packages:
            return starter_packages[character_class]
        else:
            raise ValueError(f"Unknown character class: {character_class}")

    @classmethod
    def calculate_ac(self):
        dm = ChatGPT()
        # Prepare the information to be sent to GPT-4
        ability_scores = self.character_sheet['ability_scores']
        equipment = self.character_sheet['equipment']
        proficiency = self.character_sheet['proficiency']

        message = f"Calculate the AC for the player character and how that AC was derived."
        "The player character has the following ability scores: {ability_scores}, the following equipment: {equipment}, and a proficiency bonus of {proficiency}. What is their Armor Class (AC)?"

        # Add the system message
        self.chat_gpt.add_system_message(system_message)

        # Send the message to GPT-4 and retrieve the response
        response = self.chat_gpt.invoke_gpt_4k()

        # Extract the AC from the response (requires additional error checking and validation)
        ac = int(response.split(":")[-1].strip())

        return ac

    @classmethod
    def generate_player_character(cls):
        player = EmptyStructures.get_player_structure()
        player['player'] = cls.generate_player_name()  # Assuming there's a generate_player_name method
        player['location'] = ""
        player['level'] = 1
        player['HP'] = cls.generate_initial_hp()  # Assuming there's a generate_initial_hp method
        player['age'] = cls.generate_initial_age()
        player['sex'] = cls.get_random_gender()
        # player['race'] = random.choice(cls.get_playable_races())

        ability_scores = cls.generate_ability_scores()
        for ability in ability_scores:
            player[ability.lower()] = {
                "actual": ability_scores[ability],
                "base": ability_scores[ability] - cls.get_racial_bonus(player['race'], ability),  # Assuming there's a get_racial_bonus method
                "modifier": cls.calculate_ability_modifier(ability_scores[ability]),  # Assuming there's a calculate_modifier method
                "racial bonus": cls.get_racial_bonus(player['race'], ability)
            }

        player['ac'] = {'value': cls.calculate_initial_ac(player['class']['name'], player['dexterity']['modifier']), 'derived': []}  # Assuming there's a calculate_initial_ac method
        player['speed'] = cls.calculate_initial_speed(player['race'])  # Assuming there's a calculate_initial_speed method
        player['equipment'] = cls.generate_initial_equipment(player['class']['name'])  # Assuming there's a generate_initial_equipment method
        player['coins'] = {'gold': cls.generate_initial_gold(player['class']['name']), 'silver': 0, 'copper': 0}  # Assuming there's a generate_initial_gold method
        player['proficiencies'] = cls.generate_proficiencies(player['class']['name'])  # Assuming there's a generate_proficiencies method
        player['proficiency bonus'] = 2
        player['abilities'] = cls.generate_class_abilities(player['class']['name'], player['level'])  # Assuming there's a generate_class_abilities method
        player['languages'] = cls.generate_initial_languages(player['race'])  # Assuming there's a generate_initial_languages method
        player['hit_dice'] = cls.get_hit_dice(player['class']['name'])  # Assuming there's a get_hit_dice method
        player['short_rest_recovery'] = cls.get_short_rest_recovery(player['class']['name'])  # Assuming there's a get_short_rest_recovery method
        player['XP'] = 0
        player['next_level'] = cls.calculate_next_level(player['level'])  # Assuming there's a calculate_next_level method

        return player

    @classmethod
    def generate_player_character(cls):
        raise NotImplemented()

    @classmethod
    def get_random_gender(cls):
        genders = ["Male", "Female", "Non-binary"]
        return random.choice(genders)

    @classmethod
    def roll_4d6_drop_lowest(cls):
        rolls = DieGenerator.roll_d6(num=4)
        return sorted(rolls)[1:]

    @classmethod
    def generate_ability_scores(cls):
        abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
        return {ability: cls.roll_4d6_drop_lowest() for ability in abilities}

    @classmethod
    def get_playable_races(cls):
        return ["Human", "Dwarf", "Elf", "Halfling", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]

    @classmethod
    def get_playable_classes(cls):
        return ["Barbarian",
                "Bard",
                "Cleric",
                "Druid",
                "Fighter",
                "Monk",
                "Paladin",
                "Ranger",
                "Rogue",
                "Sorcerer",
                "Warlock",
                "Wizard"]

    @classmethod
    def get_playable_alignments(cls):
        # Ethics: Lawful, Neutral, Chaotic
        ethics = ['Lawful', 'Neutral', 'Chaotic']

        # Morals: Good, Neutral, Evil
        morals = ['Good', 'Neutral', 'Evil']

        # Generate all combinations of ethics and morals
        alignments = [f'{ethic} {moral}' for ethic in ethics for moral in morals]

        return alignments

    @classmethod
    def get_level(cls, experience_points):
        for i in range(len(cls.XP_LEVEL_THRESHOLDS)):
            if experience_points < cls.XP_LEVEL_THRESHOLDS[i]:
                return i
        return 20  # If experience points exceed the level 20 threshold

    @classmethod
    def get_experience_for_next_level(cls, current_level):
        if current_level <= 0 or current_level >= 20:
            return "Invalid level. Please enter a level between 1 and 19."
        else:
            return cls.XP_LEVEL_THRESHOLDS[current_level]

    @classmethod
    def get_players_prompt(cls):
        return make_prompt(cls._players,"players")

    @classmethod
    def get_party_composition_as_string(cls):
        return f"There are {len(cls._players)} players in the party, " + " and ".join([f'a level {player["level"]} {player["race"]} {player["class"]["name"]} named {player["name"]}' for player in cls._players]) + ".\n"
