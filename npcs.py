import json

from chat_gpt import ChatGPT
from empty_structures import EmptyStructures
from game_rules import GameRules
from players import Players
from scenario import Scenario
from utilities import load_state_data, save_state_data


class NPCs:
    _instance = None
    _nonplayer_characters = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(NPCs, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.load_state()

    @classmethod
    def load_state(cls):
        cls._nonplayer_characters = load_state_data('npcs')

    @classmethod
    def save_state(cls):
        save_state_data('npcs', cls._nonplayer_characters)

    @staticmethod
    def generate_npc(self, location_id):
        dm = ChatGPT('generate-npc')

        # dm.add_system_message(GameRules.get_global_prompt())
        dm.add_system_message(f'Generate the NPC for the {location_id} location')
        dm.add_system_message(GameRules.get_adversarial_npc_generation_prompt())
        dm.add_system_message(f'Players: """\n{Players.get_players_without_descriptions()}"""\n\n')
        dm.add_system_message(f'Scenario: """\n{Scenario.get_scenario_prompt()}"""\n\n')
        dm.add_system_message(f'Empty NPC Structure: """\n{EmptyStructures.get_npc_structure()}"""\n')

        response = dm.invoke_gpt_16k()
        content = dm.get_content()
        npc = json.loads(content)
        NPCs.remember_new_npc(npc)

        print(content)
        print(response)

    @classmethod
    def remember_new_npc(cls, npc):
        cls._non_player_characters.append(npc['npc'])
        save_state_data('npcs', cls._nonplayer_characters)
