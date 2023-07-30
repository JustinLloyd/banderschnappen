from chat_gpt import ChatGPT
from utilities import make_prompt


class GameRules:
    _instance = None
    _generate_scenario = None
    _global = None
    _generate_adversarial_npc = None
    _generate_skirmish_encounter = None
    _summarize_actions = None
    _generate_encounter_treasure = None
    _generate_puzzle_encounter = None
    _generate_puzzle_treasure = None
    _0010_generate_scenario_describe_weather = None
    _0020_generate_scenario_describe_environment = None
    _0030_generate_scenario_describe_quest = None
    _0040_generate_scenario_describe_locations_briefly = None
    _0050_generate_scenario_describe_locations_in_depth = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameRules, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.load_rules()

    @classmethod
    def load_rules(cls):
        cls._global = cls.__load_rule_prompt("game-rules")
        cls._generate_scenario = cls.__load_rule_prompt("scenario-generation")
        cls._generate_adversarial_npc = cls.__load_rule_prompt("generate-adversarial-npc-leader")
        cls._summarize_actions = cls.__load_rule_prompt("summarize-actions")
        cls._generate_skirmish_encounter = cls.__load_rule_prompt("generate-skirmish-encounter")
        cls._generate_encounter_treasure = cls.__load_rule_prompt("generate-encounter-treasure")
        cls._generate_puzzle_encounter = cls.__load_rule_prompt('generate-puzzle')
        cls._generate_puzzle_treasure = cls.__load_rule_prompt('generate-puzzle-treasure')
        cls._0010_generate_scenario_describe_weather = cls.__load_rule_prompt('0010-generate-scenario-describe-weather')
        cls._0020_generate_scenario_describe_environment = cls.__load_rule_prompt('0020-generate-scenario-describe-environment')
        cls._0030_generate_scenario_describe_quest = cls.__load_rule_prompt('0030-generate-scenario-describe-quest')
        cls._0040_generate_scenario_describe_locations_briefly = cls.__load_rule_prompt('0040-generate-scenario-describe-locations-briefly')
        cls._0050_generate_scenario_describe_locations_in_depth = cls.__load_rule_prompt('0050-generate-scenario-describe-locations-in-depth')

    @classmethod
    def __load_rule_prompt(cls, prompt):
        with open(f"prompts/{prompt}.prompt") as rule_file:
            return [rule.strip() for rule in rule_file]

    @classmethod
    def get_global_rules(cls):
        return cls._global

    @classmethod
    def get_global_rules_prompt(cls):
        return make_prompt(cls._global)

    @classmethod
    def get_summarize_actions_rules(cls):
        return cls._summarize_actions

    @classmethod
    def get_scenario_generation_rules(cls):
        return cls._generate_scenario

    @classmethod
    def get_scenario_generation_prompt(cls):
        return make_prompt(cls._generate_scenario)

    @classmethod
    def get_adversarial_npc_generation_rules(cls):
        return cls._generate_adversarial_npc

    @classmethod
    def get_skirmish_encounter_rules(cls):
        return cls._generate_skirmish_encounter

    @classmethod
    def get_adversarial_npc_generation_prompt(cls):
        return make_prompt(cls._generate_adversarial_npc)

    @classmethod
    def get_skirmish_encounter_prompt(cls):
        return make_prompt(cls._generate_skirmish_encounter)

    @classmethod
    def get_describe_rules_prompt(cls):
        return f"you are a helpful assistant. describe the rules to the user.\n\nText:\n{make_prompt(cls._generate_adversarial_npc)}"

    @classmethod
    def describe_rules(cls):
        dm = ChatGPT()
        dm.add_system_message(cls.get_describe_rules_prompt())
        dm.invoke_gpt_4k()
        content = dm.get_content()
        print(content)

    @classmethod
    def get_summarize_actions_prompt(cls):
        return make_prompt(cls._summarize_actions)

    @classmethod
    def get_encounter_treasure_prompt(cls):
        return make_prompt(cls._generate_encounter_treasure)
        pass

    @classmethod
    def get_puzzle_generation_prompt(cls):
        return make_prompt(cls._generate_puzzle_encounter)

    @classmethod
    def get_puzzle_treasure_generation_prompt(cls):
        return make_prompt(cls._generate_puzzle_treasure)

    @classmethod
    def get_0010_generate_scenario_prompt_describe_weather(cls):
        return make_prompt(cls._0010_generate_scenario_describe_weather)

    @classmethod
    def get_0020_generate_scenario_describe_environment_prompt(cls):
        return make_prompt(cls._0020_generate_scenario_describe_environment)

    @classmethod
    def get_0030_generate_scenario_describe_quest_prompt(cls):
        return make_prompt(cls._0030_generate_scenario_describe_quest)

    @classmethod
    def get_0040_generate_scenario_describe_locations_briefly_prompt(cls):
        return make_prompt(cls._0040_generate_scenario_describe_locations_briefly)

    @classmethod
    def get_0050_generate_scenario_describe_locations_in_depth_prompt(cls):
        return make_prompt(cls._0050_generate_scenario_describe_locations_in_depth)


GameRules()
