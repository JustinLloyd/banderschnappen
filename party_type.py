import random

from constants import XP_LEVEL_THRESHOLDS, HIT_DICE_BY_CLASS_DB, RACE_AGE_DB, ABILITY_CONSTITUTION_KEY, ABILITIES_DB
from die_generator import DieGenerator
from player_type import Player
from utilities import load_state_data, save_state_data


class Party:
    players: [Player] = []

    def load_state(self):
        self.players = load_state_data('players')

    def save_state(self):
        save_state_data('players', self.players)

    def get_players_without_descriptions(self):
        return [player.stripped_down() for player in self.players]

    @classmethod
    def generate_initial_age(cls, race:str):
        race = race.lower()

        # Fetch the base_age and age_variation based on the character's race
        base_age = RACE_AGE_DB.get(race, {}).get('base_age', 15)  # default to human age if race not found
        age_variation = RACE_AGE_DB.get(race, {}).get('age_variation', 20)  # default to human age variation if race not found

        # Calculate the final age
        age = base_age + random.randint(0, age_variation)

        return age

    @classmethod
    def generate_initial_hp(cls, class_name, constitution:int):
        base_hp = HIT_DICE_BY_CLASS_DB.get(class_name.lower(), 8)
        total_hp = base_hp + cls.get_modifier_for(ABILITY_CONSTITUTION_KEY,constitution)
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
    def get_starting_equipment(cls,character_class):
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
        player = Player()
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
    def generate_ability_scores(cls):
        return {ability: DieGenerator.roll_drop_lowest_total(6,4) for ability in ABILITIES_DB}


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
    def convert_level_to_xp(cls, level):
        return XP_LEVEL_THRESHOLDS[level]

    @classmethod
    def convert_xp_to_level(cls, xp):
        for i in range(len(XP_LEVEL_THRESHOLDS)):
            if xp < XP_LEVEL_THRESHOLDS[i]:
                return i
        return 20

    @classmethod
    def get_experience_for_next_level(cls, current_level):
        if current_level <= 0 or current_level >= 20:
            return "Invalid level. Please enter a level between 1 and 19."
        else:
            return XP_LEVEL_THRESHOLDS[current_level]

    @classmethod
    def calculate_xp_to_next_level(cls, current_xp):
        current_level = cls.convert_xp_to_level(current_xp)
        return XP_LEVEL_THRESHOLDS[current_level] - current_xp

    # @classmethod
    # def get_players_prompt(cls):
    #     return make_prompt(cls._players, "players")
    #
    def get_party_composition_as_string(self):
        return f"There are {len(self.players)} players in the party, " + " and ".join([f'a level {player["level"]} {player["race"]} {player["class"]["name"]} named {player["name"]}' for player in self.players]) + ".\n"

    @classmethod
    def get_modifier_for(cls, ability_score):
        return (ability_score-10)//2
