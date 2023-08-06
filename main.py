import copy
import json

from actions import Actions
from chat_gpt import ChatGPT

from game_rules import GameRules
from game_state import GameState
from gem_generator import GemGenerator
from historical_summary import HistoricalSummary
from npcs import NPCs

from scenario import Scenario
from treasure_vessel_generator import TreasureVesselGenerator
from utilities import make_prompt
from world_types import GameWorld

world = None

def perform_player_action(performer, message):
    Actions.perform_action(performer, message)


def summarize_story_so_far():
    HistoricalSummary.add_summary()


def repl():
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "npc":
            NPCs.generate_npc('')
        elif user_input.lower() == "rules":
            GameRules.describe_rules()
        elif user_input.lower() == "scenario":
            generate_scenario()
        elif user_input.lower() == "summarize":
            summarize_story_so_far()
        else:
            perform_player_action("scrumm", user_input)


def generate_scenario():
    Scenario.generate_scenario()


def test_function():
    global world
    world = GameWorld.generate_random_world()
    # Scenario.generate_scenario()
    # dm = ChatGPT()
    #
    # prompt=Scenario.generate_scenario()
    # Scenario.get
    """
A pack of feral beasts, remnants of the city's once thriving wildlife, may attack adventurers wandering the square.
The fight will take place at Market Square.
The encounter consists of 3 adversarial NPCs that are all level 3.
There are 2 players in the party. A level 3 human fighter and a level 3 human ranger.
Total treasure carried by the NPCs is not to exceed 100gp.

Once the center of trade and commerce, the market square now lies in disarray. Abandoned vendor stalls still bear fragments of colorful tapestries and broken goods, hinting at a time of prosperity. A beautiful stone fountain, now dry, stands at the center of the square. The fountain depicts a robed figure, believed to be the city's ancient seer, holding an orb.
"""
# #    dm.add_system_message(GameRules.get_encounter_treasure_prompt())
#     print(dm.get_message())
#     dm.estimate_token_message()
#     dm.invoke_gpt()
#
#     content = dm.get_content()
#     print(content)
#     data = json.loads(content)


if __name__ == '__main__':
    test_function()

    # messages.append({"role": "system", "content": message})
    # messages.append({"role": "assistant", "content": "It seems that you are currently in the middle of a scenario where you need to rescue villagers from a gang of goblins. Do you wish to continue with this scenario or create a new one?"})
    # messages.append({"role": "user", "content": "let's continue on"})

    # prompt_tokens = response['usage']['prompt_tokens']
    # if prompt_tokens > 14000:
    #     summary_response = summarize_story_so_far()
    # print(response)
    # print(determine_message_significance())

    # for historical_entry in historical:
    #     print(historical_entry['summary'])
    repl()
