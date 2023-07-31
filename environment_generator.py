import random

from empty_structures import EmptyStructures


class EnvironmentGenerator:
    adjectives = [
        "Blossoming",
        "Bountiful",
        "Brambly",
        "Canopied",
        "Dappled",
        "Deciduous",
        "Dense",
        "Emerald-hued",
        "Evergreen",
        "Fern-filled",
        "Fertile",
        "Fir-lined",
        "Flourishing",
        "Fragrant",
        "Frosted"
        "Fungal",
        "Gnarled",
        "Humid",
        "Hushed",
        "Jagged",
        "Knotted",
        "Leafy",
        "Looming",
        "Lush",
        "Majestic",
        "Moss-covered",
        "Mossy",
        "Murmuring",
        "Nestled",
        "Overgrown",
        "Primeval",
        "Pristine",
        "Resilient",
        "Resounding",
        "Restful",
        "Root-riddled",
        "Rustling",
        "Secluded",
        "Serene",
        "Shady",
        "Shimmering",
        "Sprawling",
        "Stately",
        "Sun-dappled",
        "Sylvan",
        "Tangled",
        "Teeming",
        "Thicketed",
        "Time-worn",
        "Tormented",
        "Tranquil",
        "Twisted",
        "Undergrowth",
        "Unspoiled",
        "Untamed",
        "Verdant",
        "Vibrant",
        "Whispering",
        "Wild",
        "Wind-whispered",
        "Winding",
        "Wooded",
    ]
    locations = [
        {"descriptor": "alcove (hidden)"},
        {"descriptor": "animal burrow", "encounters": ["skirmish", "hazard"]},
        {"descriptor": "animal pens"},
        {"descriptor": "apothecary"},
        {"descriptor": "armory"},
        {"descriptor": "avalanche site"},
        {"descriptor": "bakery"},
        {"descriptor": "barn", "adjectives": ["burnt out", "ruined", "abandoned", "occupied working", "hostile occupied"], "encounters": []},
        {"descriptor": "barnyard"},
        {"descriptor": "barracks"},
        {"descriptor": "beach (lakeside)"},
        {"descriptor": "beach", "adjectives": ["sandy", "rocky"]},
        {"descriptor": "boat", "adjectives": ["abandoned"], "encounters": ["skirmish", "hazard", "puzzle", "quest"]},
        {"descriptor": "bog", "encounters": []},
        {"descriptor": "boggy patch"},
        {"descriptor": "boulder", "encounters": ["quest", "puzzle", "skirmish"]},
        {"descriptor": "bramble", "encounters": []},
        {"descriptor": "branch", "encounters": []},
        {"descriptor": "bridge (natural)", "encounters": []},
        {"descriptor": "bridge", "adjectives": ["wooden", "stone", "arched", "crumbling", "ruined", "destroyed"], "encounters": ["skirmish", "quest", "social", "puzzle", "hazard"]},
        {"descriptor": "brook", "encounters": []},
        {"descriptor": "brush", "encounters": []},
        {"descriptor": "bunker"},
        {"descriptor": "bush (berry)", "encounters": []},
        {"descriptor": "bushland", "encounters": []},
        {"descriptor": "cabin (fisherman's)"},
        {"descriptor": "camp", "adjectives": ["bandit", "abandoned", "hastily"], "encounters": []},
        {"descriptor": "canopy", "encounters": []},
        {"descriptor": "canyon floor"},
        {"descriptor": "canyon"},
        {"descriptor": "cave (hermit's)"},
        {"descriptor": "cave (hidden)"},
        {"descriptor": "cave (hillside)", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "cave", "adjectives": ["widening"]},
        {"descriptor": "cavern", "encounters": []},
        {"descriptor": "cellar"},
        {"descriptor": "cemetery"},
        {"descriptor": "chamber"},
        {"descriptor": "church"},
        {"descriptor": "circle (faerie)"},
        {"descriptor": "circle (mushroom)", "adjectives": [], "encounters": ["skirmish", "quest", "puzzle"]},
        {"descriptor": "circle (stone)", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "circle", "adjectives": ["rock", "mushroom", "fairy"], "encounters": []},
        {"descriptor": "clearing", "adjectives": ["sunlit"], "encounters": ["skirmish", "quest", "social", "rest", "puzzle"]},
        {"descriptor": "clearwater", "encounters": []},
        {"descriptor": "cliff edge"},
        {"descriptor": "cliff", "encounters": []},
        {"descriptor": "colony (seabird)"},
        {"descriptor": "colony (seal)"},
        {"descriptor": "commander's quarter's"},
        {"descriptor": "community hall"},
        {"descriptor": "copse", "encounters": ["skirmish", "hazard", "puzzle"]},
        {"descriptor": "cottage (peasant's)", "encounter": ["skirmish", "hazard", "puzzle", "social", "rest", "quest"]},
        {"descriptor": "cove (hidden)"},
        {"descriptor": "creek bed", "adjectives": ["dry"], "encounters": []},
        {"descriptor": "dell", "encounters": []},
        {"descriptor": "den", "encounters": []},
        {"descriptor": "ditch"},
        {"descriptor": "dock"},
        {"descriptor": "dormitory"},
        {"descriptor": "echo point"},
        {"descriptor": "entrance (cave)"},
        {"descriptor": "entrance (cave)"},
        {"descriptor": "farmhouse", "adjectives": ["burnt out", "ruined", "abandoned", "occupied working", "hostile occupied"], "encounters": []},
        {"descriptor": "farmlands"},
        {"descriptor": "fen", "encounters": ["skirmish", "hazard", "puzzle"]},
        {"descriptor": "fernery", "encounters": []},
        {"descriptor": "field (boulder)", "encounters": []},
        {"descriptor": "field (flower)", "encounters": []},
        {"descriptor": "field (mushroom)"},
        {"descriptor": "field (rolling)", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "fishing spot"},
        {"descriptor": "fjord", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "foothill", "encounters": []},
        {"descriptor": "formations"},
        {"descriptor": "fungi colony", "encounters": []},
        {"descriptor": "garden (hidden)"},
        {"descriptor": "gatehouse"},
        {"descriptor": "general store"},
        {"descriptor": "geode"},
        {"descriptor": "glade", "adjectives": ["sunny", "overgrown", "restful"], "encounters": ["skirmish", "rest", "quest", "social"]},
        {"descriptor": "grain mill"},
        {"descriptor": "knoll", "adjectives": ["grassy", "barren"], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "graveyard", "encounters": []},
        {"descriptor": "green"},
        {"descriptor": "grotto", "encounters": []},
        {"descriptor": "grove", "encounters": ["quest", "skirmish", "social", "rest"]},
        {"descriptor": "gully", "encounters": []},
        {"descriptor": "hall"},
        {"descriptor": "herbalist's garden"},
        {"descriptor": "hidden grove", "adjectives": [], "encounters": ["skirmish", "puzzle"]},
        {"descriptor": "hideout", "encounters": ["skirmish", "hazard", "puzzle"]},
        {"descriptor": "hill crest", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "hill", "adjectives": ["flower-covered"], "encounters": []},
        {"descriptor": "hollow", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "homestead"},
        {"descriptor": "hut (marsh)"},
        {"descriptor": "hut (shepherding)", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "idol (ancient)"},
        {"descriptor": "infirmary"},
        {"descriptor": "inn", "adjectives": ["burnt out", "ruined", "abandoned", "hostile occupied"], "encounters": ["rest", "social", "skirmish", "quest"]},
        {"descriptor": "island (duck)", "encounters": ["puzzle", "rest", "social"]},
        {"descriptor": "island (reedy)", "encounters": ["skirmish", "puzzle", "rest", "social"]},
        {"descriptor": "island", "encounters": ["skirmish", "puzzle", "rest", "social"]},
        {"descriptor": "jetty", "adjectives": ["old"]},
        {"descriptor": "kitchen"},
        {"descriptor": "knoll", "encounters": []},
        {"descriptor": "lair", "encounters": []},
        {"descriptor": "lake", "encounters": []},
        {"descriptor": "landing (longboat)"},
        {"descriptor": "landslide", "adjectives": ["old"]},
        {"descriptor": "latrine"},
        {"descriptor": "ledge", "adjectives": ["rocky"]},
        {"descriptor": "lights (marsh)", "encounters": ["skirmish", "hazard", "puzzle"]},
        {"descriptor": "lodge (hunting)", "adjectives": ["burnt out", "ruined", "abandoned", "occupied working", "hostile occupied"], "encounters": []},
        {"descriptor": "log (fallen) ", "adjectives": ["rotting", "freshly", "lightning struck", "mushroom covered"], "encounters": ["skirmish", "quest"]},
        {"descriptor": "log (floating)", "adjectives": ["rotting", "freshly", "smelly", "slippery", "mushroom covered"], "encounters": ["skirmish", "quest"]},
        {"descriptor": "market (fish)"},
        {"descriptor": "market"},
        {"descriptor": "marsh", "encounters": []},
        {"descriptor": "mayor's house"},
        {"descriptor": "meadow", "adjectives": ["wildflower"], "encounters": ["skirmish", "hazard", "puzzle", "social"]},
        {"descriptor": "mess hall"},
        {"descriptor": "mine", "adjectives": ["abandoned", "deserted"], "encounters": []},
        {"descriptor": "moat"},
        {"descriptor": "mossbed", "encounters": []},
        {"descriptor": "mound (barrow)", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "mountain"},
        {"descriptor": "mouth (cave)"},
        {"descriptor": "naze"},
        {"descriptor": "nest (eagle's)"},
        {"descriptor": "nest", "adjectives": ["abandoned", "occupied"]},
        {"descriptor": "officer's quarters"},
        {"descriptor": "orchard", "adjectives": ["old"]},
        {"descriptor": "outcrop", "adjectives": ["rocky", "precarious", "crumbling", "overgrown", "jagged", "sharp", "eroded", "rugged", "scenic", "striated", "exposed", "crystalline", "ancient", "volcanic", "sedimentary", "geological", "stony", "fossilized", "prominent", "bare", "towering", "granitic", "precipitous"], "encounters": ["skirmish", "quest", "social", "puzzle", "hazard"]},
        {"descriptor": "paddock"},
        {"descriptor": "pass (mountain)"},
        {"descriptor": "passage", "adjectives": ["twisting", "narrow", "crumbling"], "encounters": ["skirmish", "quest", "social", "puzzle", "trap", "hazard"]},
        {"descriptor": "patch (lichen)", "encounters": []},
        {"descriptor": "patch", "adjectives": ["wilderflower"], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "path", "adjectives": ["pine cone-littered", "narrow"], "encounters": []},
        {"descriptor": "peak", "encounters": []},
        {"descriptor": "pile (driftwood)"},
        {"descriptor": "pile (leaf)", "encounters": []},
        {"descriptor": "pillar", "adjectives": ["stone"], "encounters": []},
        {"descriptor": "pit (sinking)"},
        {"descriptor": "plateau", "encounters": []},
        {"descriptor": "pond", "adjectives": ["stagnant", "fetid", "muddy", "foul", "stinking", "fetid", "foul-smell", "quiet"]},
        {"descriptor": "pool (alligator)"},
        {"descriptor": "pool (bog)", "encounters": ["skirmish", "hazard", "puzzle", "quest"]},
        {"descriptor": "pool (marsh)"},
        {"descriptor": "pool (underground)"},
        {"descriptor": "pool", "adjectives": [], "encounters": ["skirmish", "quest", "rest", "puzzle"]},
        {"descriptor": "outpost (observation)"},
        {"descriptor": "prairie"},
        {"descriptor": "precipice"},
        {"descriptor": "quagmire"},
        {"descriptor": "quarry", "encounters": []},
        {"descriptor": "quartermaster's office"},
        {"descriptor": "rapids", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle", "hazard"]},
        {"descriptor": "ravine", "encounters": []},
        {"descriptor": "ridge", "encounters": []},
        {"descriptor": "ring (fairy)", "encounters": []},
        {"descriptor": "river (underground)"},
        {"descriptor": "river bank", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "river bend", "adjectives": ['meandering', 'serene', 'picturesque', 'twisting', 'flowing', 'tranquil', 'lush', 'winding', 'sweeping', 'murmuring', 'verdant', 'peaceful', 'shimmering', 'glistening', 'inviting', 'scenic', 'undulating', 'quiet', 'rustic', 'idyllic'], "encounters": ["skirmish", "quest", "social", "puzzle", "hazard"]},
        {"descriptor": "river", "adjectives": ["rapid"], "encounters": []},
        {"descriptor": "riverbed", "adjectives": ["rocky", "muddy", "sandy", "dry", "flooded", "damp", "overgrown", "sun-baked", "lush", "barren", "winding", "deep", "shallow", "rugged", "slippery", "smooth", "pebbly", "shadowy", "meandering", "serene"], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "room (storage)"},
        {"descriptor": "roost"},
        {"descriptor": "root", "encounters": []},
        {"descriptor": "ruins (hill fort)", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "ruins", "adjectives": ["tumbledown", "burnt out", "crumbling"], "encounters": []},
        {"descriptor": "schoolhouse"},
        {"descriptor": "scrub", "encounters": ["skirmish", "hazard", "puzzle"]},
        {"descriptor": "sea view"},
        {"descriptor": "sewer"},
        {"descriptor": "shallows"},
        {"descriptor": "shelf", "adjectives": ["rocky"]},
        {"descriptor": "shop (cobbler's)"},
        {"descriptor": "shore (reedy)"},
        {"descriptor": "slope (scree)", "adjectives": [], "encounters": ["skirmish", "quest", "social", "hazard"]},
        {"descriptor": "slope", "adjectives": ["rocky"]},
        {"descriptor": "spring (hot)"},
        {"descriptor": "spring (mountain)"},
        {"descriptor": "spring (underground)"},
        {"descriptor": "spring", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "square"},
        {"descriptor": "stable"},
        {"descriptor": "stag's leap", "encounters": ["hazard", "skirmish", "social"]},
        {"descriptor": "stalactites", "adjectives": ["dripping"], "encounters": ["skirmish", "hazard", "puzzle"]},
        {"descriptor": "stalagmites"},
        {"descriptor": "stand", "encounters": []},
        {"descriptor": "stockade"},
        {"descriptor": "stream (underground)"},
        {"descriptor": "stream", "encounters": []},
        {"descriptor": "swamp", "encounters": []},
        {"descriptor": "tavern"},
        {"descriptor": "thicket", "adjectives": [], "encounters": ["skirmish", "quest"]},
        {"descriptor": "timberland", "encounters": []},
        {"descriptor": "tower", "adjectives": ["abandoned", "guard"], "encounters": []},
        {"descriptor": "track (animal)", "adjectives": [], "encounters": ["skirmish", "quest"]},
        {"descriptor": "outpost (trading)"},
        {"descriptor": "trail (cart)", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "trail", "adjectives": ["dusty", "overgrown", "muddy", "rough", "rugged"], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "training ground"},
        {"descriptor": "tree (ancient)", "adjectives": [], "encounters": ["skirmish", "puzzle"]},
        {"descriptor": "tree (archway)", "encounters": []},
        {"descriptor": "tree (fallen)", "encounters": []},
        {"descriptor": "tree (hollow)", "adjectives": [], "encounters": ["skirmish", "quest", "rest", "puzzle"]},
        {"descriptor": "tree (lone)", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "tree (standing)"},
        {"descriptor": "tree (stump)", "encounters": []},
        {"descriptor": "tree-line", "encounters": []},
        {"descriptor": "treetop", "encounters": []},
        {"descriptor": "trench"},
        {"descriptor": "trunk", "encounters": []},
        {"descriptor": "tunnel"},
        {"descriptor": "tunnel (tree)"},
        {"descriptor": "underbrush", "encounters": []},
        {"descriptor": "undergrowth", "adjectives": ["bushy"], "encounters": ["skirmish", "quest"]},
        {"descriptor": "understory", "encounters": []},
        {"descriptor": "vale", "encounters": []},
        {"descriptor": "valley"},
        {"descriptor": "village (fishing)"},
        {"descriptor": "vine (creeping)"},
        {"descriptor": "vine (tangle)", "encounters": []},
        {"descriptor": "wagon ruts"},
        {"descriptor": "wall", "adjectives": ["glistening", "fossil"], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "watch post"},
        {"descriptor": "watchtower", "adjectives": ["old"]},
        {"descriptor": "water well"},
        {"descriptor": "waterfall", "adjectives": [], "encounters": ["skirmish", "quest", "social", "puzzle"]},
        {"descriptor": "will-o'-the-wisp spot"},
        {"descriptor": "tree (willow)"},
        {"descriptor": "hut (witch's)", "encounters": ["skirmish", "hazard", "puzzle", "quest"]},
        {"descriptor": "trail (woodland)", "adjectives": [], "encounters": ["skirmish"]},
        {"descriptor": "workshop (artisan's)"},
        {"descriptor": "workshop (blacksmith's)"},
        {"descriptor": "workshop (carpenter's)"},
        {"descriptor": "workshop (weaver's)"},
        {"descriptor": "workshop"},
    ]

    environments = [
                       {
                           "type": "highland wilderness",
                           "zones": [
                               {
                                   "zone": "woodland",
                                   "locations_to_use": {"minimum": 2, "maximum": 3},
                                   "locations": []
                               },
                               {
                                   "zone": "forest",
                                   "locations": []
                               },
                               {
                                   "zone": "river",
                                   "locations": []
                               },
                               {
                                   "zone": "mountain",
                                   "locations": []
                               },
                               {
                                   "zone": "lake",
                                   "locations": []
                               },
                               {
                                   "zone": "marsh",
                                   "locations": []
                               },
                               {
                                   "zone": "canyon",
                                   "locations": []
                               },
                               {
                                   "zone": "cave",
                                   "locations": []
                               },
                               {
                                   "zone": "hill",
                                   "locations": []
                               },
                               {
                                   "zone": "meadow",
                                   "locations": []
                               },
                               {
                                   "zone": "cavern",
                                   "locations_to_use": {"minimum": 2, "maximum": 6},
                                   "locations": [
                                   ]
                               },
                               {
                                   "zone": "swamp",
                                   "locations_to_use": {"minimum": 2, "maximum": 3},
                               },
                               {
                                   "zone": "bog",
                                   "locations_to_use": {"minimum": 2, "maximum": 3},
                                   "locations": []
                               },
                               {
                                   "zone": "outpost",
                                   "locations_to_use": {"minimum": 3, "maximum": 6},
                               }],
                           "seasons": ["spring", "summer", "autumn", "winter"],
                           "climates": ["temperate"],
                       },
                       {
                           "subtypes": ["abandoned military", "working military", "abandoned hunting", "working hunting"],
                           "seasons": ["spring", "summer", "autumn", "winter"],
                           "climates": ["temperate", "alpine", "desert", "tundra", "tropical", "polar"],
                           "locations": []
                       },
                       {
                           "type": "watchtower",
                           "subtypes": ["abandoned military", "working military"],
                           "seasons": ["spring", "summer", "autumn", "winter"],
                           "climates": ["temperate", "alpine", "desert", "tundra", "tropical", "polar"],
                           "locations": ["barracks", "storage room", "armory", "dormitory", "latrine", "cellar", "stable", "stockade", "sewer"]
                       },
                       {
                           "type": "village",
                           "subtypes": ["abandoned", "populated", "haunted", "fortified", "fishing", "market", "nomadic"],
                           "seasons": ["spring", "summer", "autumn", "winter"],
                           "climates": ["temperate", "alpine", "desert", "tundra", "tropical", "polar"],
                       },

                       {
                           "type": "desert oasis",
                           "subtypes": ["dried", "occupied", "fortified"],
                           "seasons": ["spring", "summer", "autumn", "winter"],
                           "climates": ["temperate", "alpine", "desert"]
                       },
                       {
                           "type": "mountainous",
                           "subtypes": [],
                           "seasons": ["spring", "summer", "autumn", "winter"],
                           "climates": ["temperate", "alpine"]
                       },
                       {
                           "type": "ruins",
                           "seasons": ["spring", "summer", "autumn", "winter"],
                           "climates": ["temperate", "desert", "tropical"]
                       },
                       {
                           "type": "dungeon",
                           "seasons": ["constant"],
                           "climates": ["underground"],
                           "locations": []
                       },
                       {"type": "underground caverns", "seasons": ["constant"], "climates": ["underground"]},
                       {"type": "swampland", "seasons": ["spring", "summer", "autumn", "winter"], "climates": ["tropical", "temperate"]},
                       {"type": "coastal", "seasons": ["spring", "summer", "autumn", "winter"], "climates": ["tropical", "temperate", "polar"]},
                       {"type": "urban", "seasons": ["spring", "summer", "autumn", "winter"], "climates": ["temperate", "desert", "tropical", "polar"]},
                       {"type": "arctic", "seasons": ["summer", "winter"], "climates": ["polar"]},
                       {"type": "jungle", "seasons": ["spring", "summer", "autumn", "winter"], "climates": ["tropical"]},
                   ] \
 \
                   @ classmethod


def generate_random_environment(cls):
    environment_type = random.choice(cls.environments)
    season = random.choice(environment_type["seasons"])
    climate = random.choice(environment_type["climates"])
    environment = EmptyStructures.get_environment_structure()
    environment['type'] = environment_type['type']
    environment['climate']['type'] = climate
    environment['climate']['season'] = season

    return environment


@classmethod
def verify_locations(cls, locations, encounter_types):
    descriptors = []
    for location in locations:
        # Check if all required fields are in each location
        if not all(k in location for k in ("descriptor", "adjectives", "encounters")):
            return False

        # Check if the descriptor is unique
        if location['descriptor'] in descriptors:
            return False
        descriptors.append(location['descriptor'])

        # Check if there's at least one adjective and no duplicate adjectives
        if not location['adjectives'] or len(location['adjectives']) != len(set(location['adjectives'])):
            return False

        # Check if there's at least one encounter
        if not location['encounters']:
            return False

        # Check if all encounters are valid and there are no duplicates
        if not set(location['encounters']).issubset(encounter_types) or len(location['encounters']) != len(set(location['encounters'])):
            return False

    # If all checks pass
    return True
