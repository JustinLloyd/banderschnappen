import json

from chat_gpt import ChatGPT
from game_rules import GameRules
from utilities import load_state_data, save_state_data


class Actions:
    _instance = None
    _actions = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Actions, cls).__new__(cls, *args, **kwargs)
        return cls._instance

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
        cls._actions.append({"role": "user", f"performer": "{performer}", f"message": "{message}"})
        data = []
        # build up the rules that the llm will operate under
        dm = ChatGPT()
        dm.add_system_message(GameRules.get_global_rules_prompt())

        # build the player character state for the llm
        # build up the environment that makes the world for the llm
        # build up the actions that the players' have performed so far that the llm can use as past history
        for action in cls._actions:
            if 'recipient' in action:

                packed_content = json.dumps({"recipient": f"{action['recipient']}", "message": f"{action['message']}"})
                dm.add_assistant_message(f"{packed_content}")
            elif 'performer' in action:
                packed_content = json.dumps({"performer": f"{action['performer']}", "message": f"{action['message']}"})
                dm.add_user_message(f"{packed_content}")
            else:
                raise Exception(f"Performer or recipient key not found in {action}")
        # data = {"rules": rules, "environment": environment, "historical": historical, "actions": actions}
        # jsondata = json.dumps(data)
        print(data)
