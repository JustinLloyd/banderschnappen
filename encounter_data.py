from encounter_type import EncounterData

ENCOUNTER_SKIRMISH_KEY = "skirmish"
ENCOUNTER_QUEST_KEY = "quest"
ENCOUNTER_SOCIAL_KEY = "social"
ENCOUNTER_PUZZLE_KEY = "puzzle"
ENCOUNTER_BOSS_FIGHT_KEY = "boss-fight"
ENCOUNTER_TRAP_KEY = "trap"
ENCOUNTER_HAZARD_KEY = "hazard"
ENCOUNTER_EXPLORATION_KEY = "exploration"
ENCOUNTER_REST_KEY = "rest"

ENCOUNTER_SKIRMISH = EncounterData(name=ENCOUNTER_SKIRMISH_KEY, description="your standard combat encounter that is level appropriate for the player characters, details to be filled in later.", challenge_rating=1)
ENCOUNTER_TRAP = EncounterData(name=ENCOUNTER_TRAP_KEY, description="The players may encounter traps that are either mundane or magical in nature, which can be disarmed, avoided, or triggered.", challenge_rating=1)
ENCOUNTER_HAZARD = EncounterData(name=ENCOUNTER_HAZARD_KEY, description="Players may face environmental challenges, such as a treacherous landslide, a sudden storm, or a hazardous river crossing.", challenge_rating=1)
ENCOUNTER_EXPLORATION = EncounterData(name=ENCOUNTER_HAZARD_KEY, description="The players may encounter unique landmarks, hidden caves, or ancient ruins, leading to exciting discoveries or uncovering forgotten lore.", challenge_rating=1)
ENCOUNTER_REST = EncounterData(name=ENCOUNTER_REST_KEY, description="the players may safely rest here, though there might be wandering monsters that come through.", challenge_rating=1)
ENCOUNTER_QUEST = EncounterData(name=ENCOUNTER_QUEST_KEY, description="The players may encounter friendly or hostile NPCs in the locations who can offer information, quests, or trade goods.", challenge_rating=1)
ENCOUNTER_SOCIAL = EncounterData(name=ENCOUNTER_SOCIAL_KEY, description="The players might encounter friendly or hostile NPCs in the locations who can offer information, quests, or trade goods.", challenge_rating=1)
ENCOUNTER_PUZZLE = EncounterData(name=ENCOUNTER_PUZZLE_KEY, description="the players will need to solve a puzzle that either blocks their way, reveals a hidden clue for the scenario or locks away treasure.", challenge_rating=1)
ENCOUNTER_BOSS_FIGHT = EncounterData(name=ENCOUNTER_BOSS_FIGHT_KEY, description="The players will face a powerful foe that is much stronger than a regular NPC and may minions with them.", challenge_rating=1)

ENCOUNTER_TYPES = [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_BOSS_FIGHT, ENCOUNTER_TRAP, ENCOUNTER_HAZARD, ENCOUNTER_EXPLORATION, ENCOUNTER_REST]

