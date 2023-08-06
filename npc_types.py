from ability_type import Ability
from alignment_type import Alignment
from armour_class_type import ArmourClass
from class_type import CharacterClass
from constants import ABILITY_STRENGTH_KEY, ABILITY_DEXTERITY_KEY, ABILITY_CONSTITUTION_KEY, ABILITY_CHARISMA_KEY, ABILITY_WISDOM_KEY, ABILITY_INTELLIGENCE_KEY
from die_generator import DieGenerator
from money_type import Money
from race_type import Race
from treasure_type import Treasure
from treasure_vessel_type import TreasureVessel


class NPC:
    def __init__(self, name=None, ac=None, hp=None, challenge_rating=1, level=1, description=None):
        self.name = name
        self.ac = ArmourClass()
        self.hp = hp
        self.challenge_rating = challenge_rating
        self.level = level
        self.description = description if description else "$description of the npc"
        self.age = "$approximate age of the npc"
        self.alignment = Alignment()
        self.languages = ["$languages of the npc"]
        self.skills = []
        self.traits = ["$traits of the npc"]
        self.tactics = "$a description of the tactics that the npc will use in combat based on their class, abilities and skills"
        self.ability_scores = [Ability(ABILITY_STRENGTH_KEY), Ability(ABILITY_DEXTERITY_KEY), Ability(ABILITY_CONSTITUTION_KEY), Ability(ABILITY_INTELLIGENCE_KEY), Ability(ABILITY_WISDOM_KEY), Ability(ABILITY_CHARISMA_KEY)]
        for ability in self.ability_scores:
            ability.roll()
        self.money = Money()
        self.treasure = Treasure()
        self.treasure_vessel = TreasureVessel()


class NPCCreature(NPC):
    def __init__(self):
        super().__init__()
        self.gender = "$gender of the npc"
        self.height = "$height of the npc, in centimetres, appropriate to the npc 's race"
        self.death_cries = ["$death cries of the npc"]
        self.battle_cry = "$the battle cry the npc might use"
        self.race = Race()

    pass


class NPCBeast(NPCCreature):
    pass


class NPCHumanoid(NPCCreature):
    def __init__(self):
        super().__init__()
        self.class_name = CharacterClass()
        self.culture = "$A description of the NPC's culture from where they hail"
        self.environment = "$A description of the environment in which the NPC grew up and now lives."
        self.family = "$A decription of NPC's family background."
        self.occupation = "$A description of the NPC's occupation."
        self.accent = "$regional accent of the npc"
        self.colloquialisms = ["$colloquialisms of the npc"]

    pass


class NPCMonster(NPCCreature):
    pass


class NPCUndead(NPC):
    pass


class NPCConstruct(NPC):
    pass


class NPCFey(NPC):
    pass


class NPCCelestial(NPC):
    pass


class NPCFiend(NPC):
    pass


class NPCDragon(NPC):
    pass


class NPCGiant(NPC):
    pass


class NPCElemental(NPC):
    pass


class NPCAberration(NPC):
    pass


class NPCOoze(NPC):
    pass


class NPCPlant(NPC):
    pass


class NPCMonstrosity(NPC):
    pass


class NPCSwarm(NPC):
    pass


class NPCGolem(NPC):
    pass

# {
#     "skills": {
#     },
#     "abilities": {
#     },
#     "traits": {
#     },
#     "stats": {
#         "STR": {
#             "actual": "integer, actual strength of the npc",
#             "base": "integer, base value strength of the npc",
#             "modifier": "integer, strength modifier for actions involving strength, e.g. strength-related skill checks, saving throws, or attack rolls",
#             "racial bonus": "integer, the racial bonus to strength for the npc"
#         },
#         "DEX": {
#             "actual": "integer, actual dexterity of the npc",
#             "base": "integer, base value dexterity of the npc",
#             "modifier": "integer, dexterity modifier for actions involving dexterity, e.g. dexterity-related skill checks, saving throws, or attack rolls",
#             "racial bonus": "integer, the racial bonus to strength for the npc"
#         },
#         "CON": {
#             "actual": "integer, actual constitution of the npc",
#             "base": "integer, base value constitution of the npc",
#             "modifier": "integer, constitution modifier for actions involving constitution",
#             "racial bonus": "integer, the racial bonus to constitution for the npc"
#         },
#         "INT": {
#             "actual": "integer, actual intelligence of the npc",
#             "base": "integer, base value intelligence of the npc",
#             "modifier": "integer, intelligence modifier for actions involving intelligence",
#             "racial bonus": "integer, the racial bonus to intelligence for the npc"
#         },
#         "WIS": {
#             "actual": "integer, actual wisdom of the npc",
#             "base": "integer, base value wisdom of the npc",
#             "modifier": "integer, wisdom modifier for actions involving wisdom",
#             "racial bonus": "integer, the racial bonus to wisdom for the npc"
#         },
#         "CHA": {
#             "actual": "integer, actual charisma of the npc",
#             "base": "integer, base value charisma of the npc",
#             "modifier": "integer, charisma modifier for actions involving charisma",
#             "racial bonus": "integer, the racial bonus to charisma for the npc"
#         }
#     },
#     "coins": {
#         "gold": "integer, appropriate for the level and race of the npc",
#         "silver": "integer, appropriate for the level and race of the npc",
#         "copper": "integer, appropriate for the level and race of the npc"
#     },
#     "treasure": [
#         {
#             "type": "the type of treasure, e.g. ring, potion, weapon, necklace, armour, appropriate for the race, class and gender of the npc",
#             "name": "name of the treasure item",
#             "description": "description of the treasure item",
#             "is_magic": "boolean, indicating if the treasure item is magical"
#         }
#     ],
