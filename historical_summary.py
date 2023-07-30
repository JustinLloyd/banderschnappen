import json

from actions import Actions
from chat_gpt import ChatGPT
from game_rules import GameRules
from players import Players
from utilities import load_state_data, save_state_data, make_prompt


class HistoricalSummary:
    _instance = None
    _historical_info = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(HistoricalSummary, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.load_state()

    @classmethod
    def add_summary(cls):
        dm = ChatGPT()
        dm.add_system_message(GameRules.get_summarize_actions_prompt())
        message = '\n\nPlayers: """ \n'
        message += make_prompt(Players.get_players_without_descriptions(), "players")
        message += '\n"""\n\n'
        message = 'Previous Actions: """ \n'
        message += make_prompt(Actions.get_actions(), "actions")
        message += '"""'
        dm.add_system_message(message)

        dm.invoke_gpt_16k()
        content = dm.get_content()
        print(type(content))
        print(content)
        history = json.loads(content)
        cls._historical_info.append(history)
        save_state_data('historical', cls._historical_info)
        print(history['summary'])

    @classmethod
    def load_state(cls):
        cls._historical_info = load_state_data("historical")

    @classmethod
    def save_state(cls):
        save_state_data('historical', cls._historical_info)
