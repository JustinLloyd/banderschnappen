import copy
import json
import random

from chat_gpt import ChatGPT
from die_generator import DieGenerator
from difficulty import Difficulty
from empty_structures import EmptyStructures
from game_rules import GameRules
from player_type import Players
from thinking_generator import ThinkingGenerator
from treasure_generator import TreasureGenerator
from treasure_trap_generator import TreasureTrapGenerator
from treasure_vessel_generator import TreasureVesselGenerator
from utilities import load_state_data, save_state_data, prune_structure, make_prompt, merge_structures, make_quoted_prompt, make_delimited_prompt
from environment_generator import EnvironmentGenerator


class Scenario:
    _instance = None
    _scenario = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Scenario, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        Scenario.load_state()

    @classmethod
    def load_state(cls):
        cls._scenario = load_state_data("scenario")

    @classmethod
    def save_state(cls):
        save_state_data("scenario", cls._scenario)

    @classmethod
    def get_skirmish_encounters(cls):
        return cls._scenario['']

    # @classmethod
    # def generate_scenario(cls):
    #     dm = ChatGPT(response_name='generate-scenario')
    #
    #     number_of_locations = DieGenerator.roll_notation('1d12+6')
    #     prompt = GameRules.get_scenario_generation_prompt()
    #     prompt = prompt.replace("{number-of-locations}", number_of_locations)
    #     prompt = prompt.replace("{party-composition}", Players.get_party_composition_as_string())
    #     prompt = prompt.replace("{}")
    #
    #     # decide how many locations
    #     # add in the treasure items
    #     # add in the gems
    #     # add in the adversarial npc
    #     dm.add_system_message(prompt)
    #
    #     dm.invoke_gpt()
    #     content = dm.get_content()
    #     print(content)
    #     scenario = json.loads(content)
    #     cls.save_state()
    #     print(scenario["scenario"])

    @classmethod
    def generate_scenario(cls):
        cls._scenario = EmptyStructures.get_scenario_structure()

        cls._scenario['level'] = max(Players.get_players(), key=lambda player: player['level'])['level']

        cls._scenario['party_size'] = len(Players.get_players())
        cls.__0010_generate_scenario_describe_weather()
        cls.__0020_generate_scenario_describe_environment()
        cls.__0030_generate_scenario_describe_quest()
        cls.__0040_generate_scenario_describe_locations_briefly()
        # cls.__0050_generate_scenario_describe_locations_in_depth()
        cls.save_state()

    @classmethod
    def __0010_generate_scenario_describe_weather(cls):
        print(f"Deciding if it is going to rain later\n{ThinkingGenerator.random_thinking_statement()}")
        dm = ChatGPT(response_name='0010-generate-scenario-describe-weather')
        environment = EnvironmentGenerator.generate_random_environment()
        cls._scenario['environment'].update(environment)
        environment['climate']['weather'] = "$Describe the weather based on the season, climate type and environment type."
        #
        # environment_structure = cls.__generate_environment_type()
        dm.add_system_message(GameRules.get_0010_generate_scenario_prompt_describe_weather())
        dm.add_user_message(make_delimited_prompt(prune_structure(environment), "environment"))

        # number_of_locations = DieGenerator.roll_d12_total(1, 6)
        # prompt = GameRules.get_0010_generate_scenario_prompt()
        # prompt = prompt.replace("{number-of-locations}", str(number_of_locations))
        #
        # prompt = prompt.replace("{party-composition}", Players.get_party_composition_as_string())

        # encounter_dictionary = {
        #     'combat': {'count': 2, 'weight': 0.68, 'statement': ' of the locations will be combat encounters.'},
        #     'puzzle': {'count': 1, 'weight': 0.15, 'statement': ' of the locations will be puzzle encounters.'},
        #     'exploration': {'count': 0, 'weight': 0.08, 'statement': ' of the locations will be exploration encounters.'},
        #     'social': {'count': 0, 'weight': 0.03, 'statement': ' of the locations will be social encounters.'},
        #     'hazard': {'count': 0, 'weight': 0.03, 'statement': ' of the locations will be hazard encounters.'},
        #     'rest': {'count': 1, 'weight': 0.03, 'statement': ' of the locations will be rest encounters.'},
        # }

        # Start with minimum encounter amounts and subtract from total
        # number_of_locations -= 4

        # assign remaining encounters, using weights in encounter_dictionary
        # encounter_types = list(encounter_dictionary.keys())
        # weights = [encounter['weight'] for encounter in encounter_dictionary.values()]
        # for _ in range(number_of_locations):
        #     encounter_type.py = random.choices(encounter_types, weights=weights, k=1)[0]
        #     encounter_dictionary[encounter_type.py]['count'] += 1
        #
        # encounters = ' '.join([str(encounter_data['count']) + encounter_data['statement'] for encounter_type.py, encounter_data in encounter_dictionary.items() if encounter_data['count'] > 0])
        # prompt = prompt.replace("{encounters}", encounters)
        #

        if dm.has_cached_response():
            dm.load_response()
        else:
            dm.invoke_gpt_4k()

        climate = json.loads(dm.get_content())
        print(cls._scenario)
        environment = merge_structures(cls._scenario['environment'], climate)
        cls._scenario['environment'].update(environment)
        print(cls._scenario)
        cls.save_state()

        # we generate a puzzle for each puzzle encounter, along with the treasure
        # cls.__generate_puzzle_encounters()
        # cls.__generate_puzzle_treasure()
        # cls.save_state()

        # now we go through and generate each combat encounter
        # and then we go through and generate treasure for each combat encounter

        # and then we go through and generate each hazard encounter
        # cls.__generate_hazard_encounter()
        # and then we go through and generate each social encounter
        # and then we go through and generate each exploration encounter

    @classmethod
    def __0020_generate_scenario_describe_environment(cls):
        print(f"Filling in the environment description\n{ThinkingGenerator.random_thinking_statement()}")
        dm = ChatGPT(response_name='0020-generate-scenario-describe-environment')
        dm.add_system_message(GameRules.get_0020_generate_scenario_describe_environment_prompt())
        scenario = copy.deepcopy(cls._scenario)
        scenario['environment']["name"] = "$a creative and interesting name of the environment"
        scenario['environment']["description"] = "$describe the overall environment this adventure will take place in"
        dm.add_user_message(make_delimited_prompt(prune_structure(scenario), "scenario"))
        if dm.has_cached_response():
            dm.load_response()
        else:
            dm.invoke_gpt_4k()
        updated_environment = json.loads(dm.get_content())

        print(updated_environment)
        merged_environment=merge_structures(cls._scenario,updated_environment)
        print(cls._scenario)
        cls._scenario.update(merged_environment)
        print(cls._scenario)
        cls.save_state()

    @classmethod
    def __0030_generate_scenario_describe_quest(cls):
        print(f"Create an interesting scenario in my head\n{ThinkingGenerator.random_thinking_statement()}")
        scenario = copy.deepcopy(cls._scenario)
        scenario["scenario"] = "$Describe in detail an interesting and creative adventure scenario that the players will undertake. Limit the scenario description to less than 500 words."
        scenario['title'] = "$Give the scenario a creative and clever title based on the scenario description and the environment."
        scenario['quest'] = "$Generate the main quest based on the environment and the scenario description in less than 500 words."
        scenario['quest_objective'] = "$Describe the main quest objective in less than 100 words."
        scenario['side_quest'] = "$Generate the main quest based on the environment and the scenario description in less than 200 words."
        scenario['side_quest_objective'] = "$Generate the main quest based on the environment and the scenario description in less than 100 words."

        dm = ChatGPT(response_name='0030-generate-scenario-describe-quest')
        dm.add_system_message(GameRules.get_0030_generate_scenario_describe_quest_prompt())
        dm.add_user_message(make_delimited_prompt(prune_structure(scenario), "scenario"))
        if dm.has_cached_response():
            dm.load_response()
        else:
            dm.invoke_gpt_4k()
        updated_scenario = json.loads(dm.get_content())['scenario']

        merged_scenario = merge_structures(cls._scenario, updated_scenario)
        print(cls._scenario)
        cls._scenario = merged_scenario
        print(cls._scenario)
        cls.save_state()

    @classmethod
    def __0040_generate_scenario_describe_locations_briefly(cls):
        print(f"Building each of the locations to roam around in\n{ThinkingGenerator.random_thinking_statement()}")
        number_of_locations = DieGenerator.roll_d12_total(1, 6)
        encounter_dictionary = {
            'combat': {'count': 2, 'weight': 0.72},
            'puzzle': {'count': 1, 'weight': 0.16},
            'exploration': {'count': 0, 'weight': 0.03},
            'social': {'count': 0, 'weight': 0.03},
            'hazard': {'count': 0, 'weight': 0.03},
            'rest': {'count': 1, 'weight': 0.03},
        }

        # Start with minimum encounter amounts and subtract from total
        number_of_locations -= 4

        # assign remaining encounters, using weights in encounter_dictionary
        encounter_types = list(encounter_dictionary.keys())
        weights = [encounter['weight'] for encounter in encounter_dictionary.values()]
        for _ in range(number_of_locations):
            encounter_type = random.choices(encounter_types, weights=weights, k=1)[0]
            encounter_dictionary[encounter_type]['count'] += 1

        # The data structure provided is a complex one. I need you to focus on fields 'X', 'Y', 'Z'.
        # These fields typically contain instructions in the following format: 'do this, then do that'.
        # Your task is to execute these instructions, performing the required operations on the respective fields.
        # As an example, if field 'X' contains the instruction 'multiply by 2', your output should reflect this operation being performed on 'X'.

        # Step 1 - the user has supplied a nested JSON structure (delimited by XML tags), please focus on the 'brief_description' field and the 'name' field
        # under the 'locations' objects.

        # Step 2 - the user has supplied a nested JSON structure (delimited by XML tags), please focus on the 'connections' list
        # under the 'locations' objects which are nested under

        #     __empty_location = {
        #         "id": "",
        #         "name": "",
        #         "encounter": {},
        #         "full_description": "",
        #         "brief_description": "",
        #         "noteworthy": "",
        #         "connections": []
        #     }
        # Given the following nested JSON structure, please focus on the 'description' field under 'item' objects which are
        # nested under 'inventory'. Suppose each 'description' field contains a sentence, rewrite these sentences to make them more engaging and descriptive.
        #

        # encounters = ' '.join([str(encounter_data['count']) + encounter_data['statement'] for encounter_type.py, encounter_data in encounter_dictionary.items() if encounter_data['count'] > 0])
        # prompt = prompt.replace("{encounters}", encounters)
        locations = []
        for k, v in encounter_dictionary.items():
            for location in range(v['count']):
                new_location = EmptyStructures.get_location_structure()
                new_location['id'] = ""
                new_location['name'] = ""
                del new_location["brief_description"]
                new_location['full_description']
                new_location["noteworthy"]
                new_encounter = EmptyStructures.get_encounter_structure()
                new_encounter['type'] = k
                del new_encounter['description']  # we won't generate the description for the encounter on this pass
                del new_encounter['details']  # we won't generate any details about the encounter on this pass
                del new_encounter['difficulty_level']  # we won't make use of the difficulty level on this pass
                new_location['encounter'] = new_encounter
                number_of_connections = DieGenerator.roll_d3_total()
                new_connection = EmptyStructures.get_connection_structure()
                new_connection['connects_to'] = ""
                new_connection['direction'] = ""
                new_connection['navigation'] = ""
                new_location['connections'].append(new_connection)
                for connection_idx in range(number_of_connections):
                    new_connection = EmptyStructures.get_connection_structure()
                    new_connection['connects_to'] = ""
                    new_connection['direction'] = ""
                    new_connection['navigation'] = ""
                    new_location['connections'].append(new_connection)
                locations.append(new_location)
        random.shuffle(locations)
        print(json.dumps(locations))
        scenario = copy.deepcopy(cls._scenario)
        scenario['locations'] = locations
        dm = ChatGPT(response_name='0040-generate-scenario-describe-locations-briefly')
        dm.add_system_message(GameRules.get_0040_generate_scenario_describe_locations_briefly_prompt())
        dm.add_user_message(f"There are {len(locations)} separate locations.")
        dm.add_user_message(make_delimited_prompt(prune_structure(scenario)))
        estimated_tokens = dm.estimate_token_message() * 1.1
        if dm.has_cached_response():
            dm.load_response()
        else:
            dm.invoke_16k()
        update_locations = json.loads(dm.get_content())

        # assert len(scenario['locations']) == len(json.loads(content)['locations'])
        # merged = merge_structures(scenario['locations'], json.loads(content)['locations'])
        merged_scenario = merge_structures(cls._scenario, update_locations)
        print(cls._scenario)
        cls._scenario = merged_scenario
        print(cls._scenario)
        cls.save_state()

    @classmethod
    def __0050_generate_scenario_describe_locations_in_depth(cls):
        return
        print(f"Describing in excessive detail the number of petals on each flower in the environment (generating in-depth location descriptions)\n{ThinkingGenerator.random_thinking_statement()}")
        scenario_locations = copy.deepcopy(cls._scenario['locations'])
        for current_location in scenario_locations:
            scenario = copy.deepcopy(cls._scenario)
            # remove all existing locations from the scenario copy
            del scenario['locations']
            scenario['locations'] = []
            dm = ChatGPT(response_name=f"0050-generate-scenario-describe-locations-in-depth-{current_location['id']}")
            dm.add_system_message(GameRules.get_0050_generate_scenario_describe_locations_in_depth_prompt())
            current_location['full_description'] = "$Describe the location in detail drawing inspiration from the brief_description. Temper your enthusiasm for emanating magic, mysteries and treasure guarded by fearsome beasts.Stick to factual information about the location. use less than 300 words."
            current_location["noteworthy"] = "$Describe any noteworthy points of interest about the geography, buildings, people, plants or statues that may be in the immediate area. Temper your enthusiasm for emanating magic, mysteries and treasure guarded by fearsome beasts.Stick to factual information about the location. Use less than 100 words."
            scenario['locations'].append(current_location)
            dm.add_user_message(make_delimited_prompt(prune_structure(scenario), "location"))
            if dm.has_cached_response():
                dm.load_response()
            else:
                dm.invoke_gpt_16()
            updated_location = json.loads(dm.get_content(), strict=False)['location']
            current_location['full_description'] = updated_location['full_description']
            current_location['noteworthy'] = updated_location['noteworthy']
            cls._scenario['locations'] = scenario_locations
            cls.save_state()
        # get a copy of the entire scenario
        # get each location into a list of locations
        # for each location in the list of locations
        #       make a copy of the scenario
        #       remove all of the locations from the scenario copy
        #       add the current location from the loop back in to the scenario
        #       Load up the prompt
        #       set the system message
        #       set the user message
        #       invoke the chat gpt
        #       merge the returned content on top of the location data
        #       set the location in the scenario with the new merged data

        pass

    @classmethod
    def __0060_generate_scenario(cls):
        # get all of the rest encounters and populate them with extra detail
        pass

    @classmethod
    def __0070_generate_scenario(cls):
        # get all of the puzzle encounters and populate them with extra detail
        pass

    @classmethod
    def __0080_generate_scenario(cls):
        # get all of the skirmish encounters and populate them with extra detail
        pass

    @classmethod
    def __0090_generate_scenario(cls):
        # get all of the boss encounters and populate them with extra detail
        pass

    @classmethod
    def __0100_generate_scenario(cls):
        # get all of the social encounters and populate them with extra detail
        pass

    @classmethod
    def __0110_generate_scenario(cls):
        # get all of the hazard encounters and populate them with extra detail
        pass

    @classmethod
    def __generate_puzzle_encounters(cls):
        for location in cls.__get_locations("puzzle"):
            dm = ChatGPT(response_name=f"generate-puzzle-{location['id']}")
            prompt = GameRules.get_puzzle_generation_prompt()
            prompt = prompt.replace("{party-composition}", Players.get_party_composition_as_string())
            number_of_stages = random.randint(1, 3)
            prompt = prompt.replace("{number-of-stages}", str(number_of_stages))
            puzzle = location['encounter']
            empty_puzzle = EmptyStructures.get_puzzle_structure()
            puzzle['difficulty-level'] = ''
            puzzle['puzzle-stages'] = []
            for i in range(number_of_stages):
                puzzle['puzzle-stages'].append(
                    {
                        "description": "the title of the stage",
                        "clues": [
                            "a clue of how to solve this stage of the puzzle"
                        ],
                        "solution_verification": "a solution description the DM will use to verify that the puzzle stage has been solved"
                    })

            puzzle["partial_success"] = {
                "enabled": "boolean",
                "partial_clue": "a clue to give the players if they partially solve the puzzle",
                "reduced_consequences": "The reduced consequences, if there is a trap, if the players only partially solve the puzzle."
            }

            prompt = prompt.replace("{location}", json.dumps(location, indent=4))
            print(prompt)
            dm.add_system_message(prompt)
            if dm.has_cached_response():
                dm.load_response()
            else:
                dm.invoke_16k()
            content = dm.get_content()
            print(content)
            new_puzzle_data = json.loads(content)
            location['encounter'] = new_puzzle_data['encounter']

    @classmethod
    def __get_locations(cls, encounter_type):
        rest_encounters = []
        for location in cls._scenario["locations"]:
            if location["encounter"]["type"] == encounter_type:
                rest_encounters.append(location)
        return rest_encounters

    @classmethod
    def __generate_puzzle_treasure(cls):
        for location in cls.__get_locations("puzzle"):
            # get the empty treasure data structure
            puzzle = location['encounter']
            puzzle['treasure'] = {}

            puzzle_difficulty = puzzle['difficulty_level']
            # generate treasure vessel and contents
            vessel = TreasureGenerator.generate_vessel(puzzle_difficulty)
            vessel["description"] = 'create an interesting description based on the vessel properties',
            vessel["noteworthy"] = 'describe anything noteworthy about the vessel that might not be immediately obvious at first glance',
            treasure = {
                'vessel': vessel,
                "locked": {
                    "is_locked": cls.is_locked(puzzle_difficulty),
                    "description": ""
                },
                "is_trapped": cls.is_trapped(puzzle_difficulty),
                "trap": {},
                "contents": {}
            }

            if treasure['is_trapped']:
                trap_type = TreasureTrapGenerator.generate_random_trap(vessel)
                detection_difficulty, disarm_difficulty, dodge_difficulty = cls.get_trap_difficulty(puzzle_difficulty)
                damage = cls.get_trap_damage(puzzle_difficulty)
                treasure['trap'] = {
                    "type": trap_type,
                    "status": "undetected",
                    "effect": "describe what effect this type of trap has",
                    "description": "describe how the trap will activate, what the trap looks like, noises the trap may make when sprung",
                    "detection_difficulty": detection_difficulty,
                    "disarm_difficulty": disarm_difficulty,
                    "damage": damage,
                    "dodge_difficulty": dodge_difficulty
                }

            treasure['contents'] = TreasureGenerator.generate_vessel_treasure(treasure, puzzle_difficulty)
            puzzle['treasure'] = treasure
            return treasure

    @staticmethod
    def is_locked(puzzle_difficulty):
        """Determine if the treasure is locked based on puzzle difficulty"""
        return random.random() < (Difficulty.PUZZLE_DIFFICULTIES.index(puzzle_difficulty) + 1) / 3

    @staticmethod
    def is_trapped(puzzle_difficulty):
        """Determine if the treasure is trapped based on puzzle difficulty"""
        return random.random() < (Difficulty.PUZZLE_DIFFICULTIES.index(puzzle_difficulty) + 1) / 3

    @staticmethod
    def get_trap_difficulty(puzzle_difficulty):
        """Determine detection, disarm and dodge difficulties based on puzzle difficulty"""
        base_difficulty = (Difficulty.PUZZLE_DIFFICULTIES.index(puzzle_difficulty) + 1) * 10
        detection_difficulty = base_difficulty + random.randint(-2, 2)
        disarm_difficulty = base_difficulty + random.randint(-2, 2)
        dodge_difficulty = base_difficulty + random.randint(-2, 2)
        return detection_difficulty, disarm_difficulty, dodge_difficulty

    @staticmethod
    def get_trap_damage(puzzle_difficulty):
        """Determine trap damage based on puzzle difficulty"""
        base_damage = (Difficulty.PUZZLE_DIFFICULTIES.index(puzzle_difficulty) + 1) * 5
        damage = base_damage + random.randint(-2, 2)
        return f'{damage}d6'  # roll notation

    @classmethod
    def __generate_hazard_encounter(cls):
        for location in cls.__get_locations("puzzle"):
            dm = ChatGPT(response_name=f"generate-hazard-{location['id']}")
        pass

    @classmethod
    def __generate_environment_type(cls):
        environment = EnvironmentGenerator.generate_random_environment()
        environment['climate']['weather'] = "Instruction: Describe the weather based on the season, climate type and environment type."
        return environment
