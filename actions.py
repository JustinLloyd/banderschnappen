import json

from chat_gpt import ChatGPT
from game_rules import GameRules
from utilities import load_state_data, save_state_data


class Actions:
    _actions = []

    def __init__(self):
        self.load_state()

    @classmethod
    def load_state(cls):
        cls._actions = load_state_data('actions')

    @classmethod
    def save_state(cls):
        save_state_data('actions', cls._actions)

    @classmethod
    def get_actions(cls):
        return cls._actions

    @classmethod
    def perform_action(cls, performer, message):
        cls._actions.append({"role": "user", "performer": performer, "message": message})
        # build up the rules that the llm will operate under
        dm = ChatGPT()
        dm.add_system_message(GameRules.get_global_rules_prompt())

        # TODO build the player character state for the llm
        # TODO build up the environment that makes the world for the llm
        # TODO build up the actions that the players' have performed so far that the llm can use as past history
        for action in cls._actions:
            if 'recipient' in action:

                packed_content = json.dumps({"recipient": f"{action['recipient']}", "message": f"{action['message']}"})
                dm.add_assistant_message(f"{packed_content}")
            elif 'performer' in action:
                packed_content = json.dumps({"performer": f"{action['performer']}", "message": f"{action['message']}"})
                dm.add_user_message(f"{packed_content}")
            else:
                raise Exception(f"Performer or recipient key not found in {action}")
        # TODO bring this up to spec on the modern way of invoking the chatgpt api through our chatgpt module
        dm.invoke_warm_4k()
        content = dm.get_content()
        print(type(content))
        print(content)
