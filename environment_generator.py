import random

from empty_structures import EmptyStructures
from constants import *


class EnvironmentGenerator:
    NOUN_BANDIT = "bandit"
    NOUN_HERMIT = "hermit"
    NOUN_HUNTER = "hunter"
    NOUN_BEAR = "bear"
    NOUN_WOLF = "wolf"
    NOUN_BERRY = "berry"
    NOUN_WOOD = "wood"
    NOUN_STONE = "stone"
    NOUN_NATURAL = "natural"

    ADJ_ABANDONED = "abandoned"
    ADJ_ANCIENT = "ancient"
    ADJ_ARCHED = "arched"
    ADJ_BARE = "bare"
    ADJ_BARREN = "barren"
    ADJ_BLOSSOMING = "blossoming"
    ADJ_BOUNTIFUL = "bountiful"
    ADJ_BRAMBLY = "brambly"
    ADJ_BURNT_OUT = "burnt-out"
    ADJ_BUSHY = "bushy"
    ADJ_CANOPIED = "canopied"
    ADJ_COLLAPSED = "collapsed"
    ADJ_COOL = "cool"
    ADJ_CREEPING = "creeping"
    ADJ_CRUMBLING = "crumbling"
    ADJ_CRYSTALLINE = "crystalline"
    ADJ_DAMP = "damp"
    ADJ_DAPPLED = "dappled"
    ADJ_DECAYING = "decaying"
    ADJ_DECIDUOUS = "deciduous"
    ADJ_DEEP = "deep"
    ADJ_DENSE = "dense"
    ADJ_DESERTED = "deserted"
    ADJ_DESTROYED = "destroyed"
    ADJ_DRIPPING = "dripping"
    ADJ_DRY = "dry"
    ADJ_DUSTY = "dusty"
    ADJ_EMPTIED = "emptied"
    ADJ_ERODED = "eroded"
    ADJ_EVERGREEN = "evergreen"
    ADJ_EXPOSED = "exposed"
    ADJ_FALLEN = "fallen"
    ADJ_FERN_FILLED = "fern-filled"
    ADJ_FERTILE = "fertile"
    ADJ_FETID = "fetid"
    ADJ_FIR_LINED = "fir-lined"
    ADJ_FLOODED = "flooded"
    ADJ_FLOURISHING = "flourishing"
    ADJ_FLOWER_COVERED = "flower-covered"
    ADJ_FLOWING = "flowing"
    ADJ_FORTIFIED = 'fortified'
    ADJ_FOSSIL = "fossil"
    ADJ_FOSSILIZED = "fossilized"
    ADJ_FOSSIl = "fossil"
    ADJ_FOUL = "foul"
    ADJ_FOUL_SMELLING = "foul-smelling"
    ADJ_FRAGRANT = "fragrant"
    ADJ_FRESH = "fresh"
    ADJ_FRESHLY = "freshly"
    ADJ_FROSTED = 'frosted'
    ADJ_FUNGAL = "fungal"
    ADJ_GEOLOGICAL = "geological"
    ADJ_GLISTENING = "glistening"
    ADJ_GNARLED = "gnarled"
    ADJ_GRANITIC = "granitic"
    ADJ_HASTILY = 'hastily'
    ADJ_HIDDEN = "hidden"
    ADJ_HOLLOW = "hollow"
    ADJ_HOLY = "holy"
    ADJ_HOSTILE = 'hostile'
    ADJ_HUMID = "humid"
    ADJ_HUMMING = "humming"
    ADJ_HUSHED = "hushed"
    ADJ_IDYLLIC = 'idyllic'
    ADJ_INVITING = "inviting"
    ADJ_JAGGED = "jagged"
    ADJ_KNOTTED = "knotted"
    ADJ_LEAFY = "leafy"
    ADJ_LEAF_STREWN = "leaf-strewn"
    ADJ_LICHEN_COVERED = "lichen-covered"
    ADJ_LIGHTING_STRUCK = "lightning-struck"
    ADJ_LONE = "lone"
    ADJ_LOOMING = "looming"
    ADJ_LUSH = "lush"
    ADJ_MAJECTIC = "majestic"
    ADJ_MAJESTIC = "majestic"
    ADJ_MEANDERING = "meandering"
    ADJ_MOSSY = "mossy"
    ADJ_MOSS_COVERED = "moss-covered"
    ADJ_MUDDY = "muddy"
    ADJ_MURKY = "murky"
    ADJ_MURMURING = "murmuring"
    ADJ_MUSHROOM_COVERED = "mushroom-covered"
    ADJ_NARROW = "narrow"
    ADJ_NESTLED = "nestled"
    ADJ_OCCUPIED = "occupied"
    ADJ_ODOUROUS = "odourous"
    ADJ_OLD = "old"
    ADJ_OVERGROWN = "overgrown"
    ADJ_PARTIALLY_STOCKED = "partially-stocked"
    ADJ_PEACEFUL = "peaceful"
    ADJ_PEBBLY = "pebbly"
    ADJ_PICTURESQUE = "picturesque"
    ADJ_PINE_CONE_LITTERED = "pine-cone-littered"
    ADJ_PRECARIOUS = "precarious"
    ADJ_PRECIPITOUS = "precipitous"
    ADJ_PRIMEVAL = "primeval"
    ADJ_PRISTINE = "pristine"
    ADJ_PROMINENT = "prominent"
    ADJ_QUIET = "quiet"
    ADJ_RAPID = "rapid"
    ADJ_RESILIENT = "resilient"
    ADJ_RESOUNDING = "resounding"
    ADJ_RESTFUL = "restful"
    ADJ_ROCKY = "rocky"
    ADJ_ROOT_RIDDLED = "root-riddled"
    ADJ_ROTTING = "rotting"
    ADJ_ROUGH = "rough"
    ADJ_RUGGED = "rugged"
    ADJ_RUINED = "ruined"
    ADJ_RUNE_COVERED = "rune-covered"
    ADJ_RUSTIC = "rustic"
    ADJ_RUSTLING = "rustling"
    ADJ_SACRIFICIAL = "sacrificial"
    ADJ_SANDY = "sandy"
    ADJ_SCENIC = "scenic"
    ADJ_SCOURED = "scoured"
    ADJ_SECLUDED = "secluded"
    ADJ_SEDIMENTARY = "sedimentary"
    ADJ_SERENE = "serene"
    ADJ_SHADOWY = "shadowy"
    ADJ_SHADY = "shady"
    ADJ_SHALLOW = "shallow"
    ADJ_SHARP = "sharp"
    ADJ_SHIMMERING = "shimmering"
    ADJ_SILENT = "silent"
    ADJ_SLIPPERY = "slippery"
    ADJ_SMELLY = "smelly"
    ADJ_SMOOTH = "smooth"
    ADJ_SPRAWLING = "sprawling"
    ADJ_STAGNANT = "stagnant"
    ADJ_STANDING = "standing"
    ADJ_STATELY = "stately"
    ADJ_STINKING = "stinking"
    ADJ_STONY = "stony"
    ADJ_STRIATED = "striated"
    ADJ_SUN_BAKED = "sun-baked"
    ADJ_SWEEPING = "sweeping"
    ADJ_SYLVAN = "sylvan"
    ADJ_TANGLED = "tangled"
    ADJ_TEEMING = "teeming"
    ADJ_THICKETED = "thicketed"
    ADJ_TIME_WORN = "time-worn"
    ADJ_TORMENTED = "tormented"
    ADJ_TOWERING = "towering"
    ADJ_TRANQUIL = "tranquil"
    ADJ_TUMBLEDOWN = "tumbledown"
    ADJ_TWISTED = 'twisted'
    ADJ_TWISTING = "twisting"
    ADJ_UNDERGROWTH = "undergrowth"
    ADJ_UNDUlATING = "undulating"
    ADJ_UNSPOILED = "unspoiled"
    ADJ_UNTAMED = "untamed"
    ADJ_VERDANT = "verdant"
    ADJ_VIBRANT = "vibrant"
    ADJ_VOLCANIC = "volcanic"
    ADJ_WHISPERING = "whispering"
    ADJ_WIDENING = "widening"
    ADJ_WILD = "wild"
    ADJ_WINDING = "winding"
    ADJ_WIND_WHISPERED = "wind-whispered"
    ADJ_WOODED = "wooded"

    adjectives = [

        ADJ_ABANDONED,
        ADJ_ANCIENT,
        ADJ_ARCHED,
        ADJ_BARE,
        ADJ_BARREN,
        ADJ_BLOSSOMING,
        ADJ_BOUNTIFUL,
        ADJ_BRAMBLY,
        ADJ_BURNT_OUT,
        ADJ_BUSHY,
        ADJ_CANOPIED,
        ADJ_COLLAPSED,
        ADJ_CREEPING,
        ADJ_CRUMBLING,
        ADJ_CRYSTALLINE,
        ADJ_DAPPLED,
        ADJ_DECIDUOUS,
        ADJ_DENSE,
        ADJ_DESTROYED,
        ADJ_DRY,
        ADJ_DUSTY,
        ADJ_EMPTIED,
        ADJ_ERODED,
        ADJ_EVERGREEN,
        ADJ_EXPOSED,
        ADJ_FALLEN,
        ADJ_FERN_FILLED,
        ADJ_FERTILE,
        ADJ_FIR_LINED,
        ADJ_FLOURISHING,
        ADJ_FLOWER_COVERED,
        ADJ_FLOWING,
        ADJ_FORTIFIED,
        ADJ_FOSSILIZED,
        ADJ_FOSSIl,
        ADJ_FRAGRANT,
        ADJ_FRESH,
        ADJ_FROSTED,
        ADJ_FUNGAL,
        ADJ_GEOLOGICAL,
        ADJ_GLISTENING,
        ADJ_GNARLED,
        ADJ_GRANITIC,
        ADJ_HASTILY,
        ADJ_HIDDEN,
        ADJ_HOLLOW,
        ADJ_HOSTILE,
        ADJ_HUMID,
        ADJ_HUMMING,
        ADJ_HUSHED,
        ADJ_IDYLLIC,
        ADJ_INVITING,
        ADJ_JAGGED,
        ADJ_KNOTTED,
        ADJ_LEAFY,
        ADJ_LONE,
        ADJ_LOOMING,
        ADJ_LUSH,
        ADJ_MAJECTIC,
        ADJ_MEANDERING,
        ADJ_MOSSY,
        ADJ_MOSS_COVERED,
        ADJ_MURMURING,
        ADJ_NARROW,
        ADJ_NESTLED,
        ADJ_OCCUPIED,
        ADJ_ODOUROUS,
        ADJ_OLD,
        ADJ_OVERGROWN,
        ADJ_PARTIALLY_STOCKED,
        ADJ_PEACEFUL,
        ADJ_PICTURESQUE,
        ADJ_PRECARIOUS,
        ADJ_PRECIPITOUS,
        ADJ_PRIMEVAL,
        ADJ_PRISTINE,
        ADJ_PROMINENT,
        ADJ_QUIET,
        ADJ_RAPID,
        ADJ_RESILIENT,
        ADJ_RESOUNDING,
        ADJ_RESTFUL,
        ADJ_ROCKY,
        ADJ_ROOT_RIDDLED,
        ADJ_ROUGH,
        ADJ_RUINED,
        ADJ_RUSTIC,
        ADJ_RUSTLING,
        ADJ_SANDY,
        ADJ_SCENIC,
        ADJ_SCOURED,
        ADJ_SECLUDED,
        ADJ_SEDIMENTARY,
        ADJ_SERENE,
        ADJ_SHADY,
        ADJ_SHIMMERING,
        ADJ_SLIPPERY,
        ADJ_SPRAWLING,
        ADJ_STANDING,
        ADJ_STATELY,
        ADJ_STONY,
        ADJ_STRIATED,
        ADJ_SWEEPING,
        ADJ_SYLVAN,
        ADJ_TANGLED,
        ADJ_TEEMING,
        ADJ_THICKETED,
        ADJ_TIME_WORN,
        ADJ_TORMENTED,
        ADJ_TOWERING,
        ADJ_TRANQUIL,
        ADJ_TWISTED,
        ADJ_TWISTING,
        ADJ_UNDERGROWTH,
        ADJ_UNDUlATING,
        ADJ_UNSPOILED,
        ADJ_UNTAMED,
        ADJ_VERDANT,
        ADJ_VIBRANT,
        ADJ_VOLCANIC,
        ADJ_WHISPERING,
        ADJ_WIDENING,
        ADJ_WILD,
        ADJ_WINDING,
        ADJ_WIND_WHISPERED,
        ADJ_WOODED,
    ]

    LOC_MOUNTAIN_PASS = {"descriptor": "mountain pass", "adjectives": [ADJ_ROCKY, ADJ_WINDING, ADJ_RUGGED, ADJ_SHADOWY, ADJ_JAGGED, ADJ_NARROW, ADJ_STONY, ADJ_SCENIC, ADJ_ROUGH, ADJ_PRECIPITOUS, ADJ_LOOMING, ADJ_GRANITIC, ADJ_BARE, ADJ_MAJESTIC, ADJ_TOWERING, ADJ_PRECARIOUS, ADJ_PICTURESQUE], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    LOC_ALCOVE = {"descriptor": "alcove (hidden)", "adjectives": [ADJ_HIDDEN, ADJ_SECLUDED, ADJ_SHADOWY, ADJ_NARROW, ADJ_QUIET, ADJ_MOSSY, ADJ_DAMP, ADJ_COOL, ADJ_SILENT, ADJ_PEACEFUL, ADJ_LONE, ADJ_HUSHED, ADJ_VERDANT, ADJ_STONY, ADJ_FRESH], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST]}
    LOC_ALTAR = {
        "descriptor": "altar",
        "nouns": ["plant", "wooden", "stone"],
        "adjectives": [
            ADJ_ANCIENT, ADJ_HOLY, ADJ_RUNE_COVERED, ADJ_MOSS_COVERED,
            ADJ_ABANDONED, ADJ_SHADOWY, ADJ_IDYLLIC, ADJ_FLOURISHING, ADJ_BARE,
            ADJ_STONY, ADJ_VERDANT, ADJ_CRUMBLING, ADJ_FORTIFIED, ADJ_RUINED,
            ADJ_TWISTED, ADJ_DECAYING, ADJ_GNARLED, ADJ_TORMENTED, ADJ_TIME_WORN,
            ADJ_SACRIFICIAL
        ],
        "encounters": [
            ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST, ENCOUNTER_REST
        ]
    }

    LOC_ANIMAL_BURROW = {
        "descriptor": "animal burrow",
        "adjectives": [
            ADJ_ABANDONED, ADJ_COLLAPSED, ADJ_OCCUPIED, ADJ_DEEP, ADJ_NARROW,
            ADJ_WINDING, ADJ_DARK, ADJ_DAMP, ADJ_MUDDY, ADJ_FRESHLY, ADJ_SHADOWY,
            ADJ_HIDDEN, ADJ_OVERGROWN, ADJ_TWISTING, ADJ_MUSHROOM_COVERED, ADJ_ROOT_RIDDLED,
            ADJ_FERN_FILLED, ADJ_COZY, ADJ_FOUL_SMELLING, ADJ_LEAF_STREWN, ADJ_FLOURISHING, ADJ_UNDERGROWTH,
            ADJ_BUSHY
        ],
        "encounters": [
            ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE
        ]
    }

    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ANIMAL_PENS = {"descriptor": "animal pens", "adjectives": [ADJ_ABANDONED, ADJ_COLLAPSED, ADJ_OCCUPIED, ADJ_ODOUROUS, ADJ_HOSTILE, ADJ_BURNT_OUT], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST, ENCOUNTER_REST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_APOTHECARY = {"descriptor": "apothecary", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ARMORY = {"descriptor": "armory", "adjectives": [ADJ_EMPTIED, ADJ_SCOURED, ADJ_PARTIALLY_STOCKED, ], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_REST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_AVALANCHE_SITE = {"descriptor": "avalanche site", "adjectives": [ADJ_FRESH], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BAKERY = {"descriptor": "bakery", "adjectives": [ADJ_ABANDONED, ADJ_BURNT_OUT], "encounters": [ENCOUNTER_SOCIAL, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BARN = {"descriptor": "barn", "adjectives": [ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_OCCUPIED, ADJ_HOSTILE], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BARNYARD = {"descriptor": "barnyard", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BARRACKS = {"descriptor": "barracks", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BEACH = {"descriptor": "beach", "adjectives": [ADJ_SANDY, ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BEACH_LAKESIDE = {"descriptor": "lakeside beach", "adjectives": [ADJ_SANDY, ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BOAT = {"descriptor": "boat", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BOG = {"descriptor": "bog", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BOGGY_PATCH = {"descriptor": "boggy patch", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BOULDER = {"descriptor": "boulder", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_QUEST, ENCOUNTER_PUZZLE, ENCOUNTER_SKIRMISH]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BRAMBLE = {"descriptor": "bramble", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BRANCH = {"descriptor": "branch", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BRIDGE = {"descriptor": "bridge", "nouns": [NOUN_NATURAL, NOUN_STONE, NOUN_WOOD], "adjectives": [ADJ_ARCHED, ADJ_CRUMBLING, ADJ_RUINED, ADJ_DESTROYED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BROOK = {"descriptor": "brook", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BRUSH = {"descriptor": "brush", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BUNKER = {"descriptor": "bunker", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BUSH = {"descriptor": "bush", "adjectives": [ADJ_ABANDONED], "nouns": [NOUN_BERRY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_SOCIAL, ENCOUNTER_REST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_BUSHLAND = {"descriptor": "bushland", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CABIN = {"descriptor": "cabin (fisherman's)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CAMP = {"descriptor": "camp", "nouns": [NOUN_BANDIT], "adjectives": [ADJ_ABANDONED, ADJ_HASTILY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CANYON = {"descriptor": "canyon", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CANYON_FLOOR = {"descriptor": "canyon floor", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CAVE = {"descriptor": "cave", "nouns": ["hermit", "hillside"], "adjectives": [ADJ_HIDDEN, ADJ_WIDENING], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_REST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CAVERN = {"descriptor": "cavern", "adjectives": [ADJ_HIDDEN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CAVE_ENTRANCE = {"descriptor": "cave entrance", "adjectives": [ADJ_HIDDEN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CAVE_MOUTH = {"descriptor": "cave mouth", "adjectives": [ADJ_HIDDEN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CELLAR = {"descriptor": "cellar", "adjectives": [ADJ_HIDDEN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CEMETERY = {"descriptor": "cemetery", "adjectives": [ADJ_HUSHED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CHAMBER = {"descriptor": "chamber", "adjectives": [ADJ_HUSHED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CHURCH = {"descriptor": "church", "adjectives": [ADJ_HUSHED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CIRCLE = {"descriptor": "circle", "nouns": ["rock", "mushroom", "fairy"], "adjectives": [ADJ_OLD], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CIRCLE_FAERIE = {"descriptor": "circle (faerie)", "adjectives": [ADJ_HUSHED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CIRCLE_MUSHROOM = {"descriptor": "circle (mushroom)", "adjectives": [ADJ_HUSHED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CIRCLE_STONE = {"descriptor": "circle (stone)", "adjectives": [ADJ_HUSHED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CLEARING = {"descriptor": "clearing", "adjectives": [ADJ_DAPPLED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_REST, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CLEARWATER = {"descriptor": "clearwater", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CLIFF = {"descriptor": "cliff", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CLIFF_EDGE = {"descriptor": "cliff edge", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_COLONY_SEABIRD = {"descriptor": "colony (seabird)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_COLONY_SEAL = {"descriptor": "colony (seal)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_COMMUNITY_HALL = {"descriptor": "community hall", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_COPSE = {"descriptor": "copse", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_COTTAGE_PEASANT = {"descriptor": "cottage (peasant's)", "encounter": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_SOCIAL, ENCOUNTER_REST, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_COVE_HIDDEN = {"descriptor": "cove (hidden)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_CREEK_BED = {"descriptor": "creek bed", "adjectives": [ADJ_DRY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_DELL = {"descriptor": "dell", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_DEN = {"descriptor": "den", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_DITCH = {"descriptor": "ditch", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_DOCK = {"descriptor": "dock", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_DORMITORY = {"descriptor": "dormitory", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ECHO_POINT = {"descriptor": "echo point", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_FARMHOUSE = {"descriptor": "farmhouse", "adjectives": [ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_OCCUPIED, ADJ_HOSTILE], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_FARMLANDS = {"descriptor": "farmlands", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_FEN = {"descriptor": "fen", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_FERNERY = {"descriptor": "fernery", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_FIELD = {"descriptor": "field", "nouns": ["boulder", "flower", "mushroom"], "adjectives": [], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SPOT_FISHING = {"descriptor": "fishing spot", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_FJORD = {"descriptor": "fjord", "adjectives": [ADJ_DRY, ADJ_SANDY, ADJ_RAPID], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_FOOTHILL = {"descriptor": "foothill", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_FORMATIONS = {"descriptor": "formations", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_FUNGI_COLONY = {"descriptor": "fungi colony", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GARDEN_HERBALIST = {"descriptor": "herbalist's garden", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GARDEN_HIDDEN = {"descriptor": "garden (hidden)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GATEHOUSE = {"descriptor": "gatehouse", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GEODE = {"descriptor": "geode", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GLADE = {"descriptor": "glade", "adjectives": [ADJ_DAPPLED, ADJ_OVERGROWN, ADJ_RESTFUL], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_REST, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GRAIN_MILL = {"descriptor": "grain mill", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GRAVEYARD = {"descriptor": "graveyard", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GREEN = {"descriptor": "green", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GROTTO = {"descriptor": "grotto", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GROVE = {"descriptor": "grove", "encounters": [ENCOUNTER_QUEST, ENCOUNTER_SKIRMISH, ENCOUNTER_SOCIAL, ENCOUNTER_REST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GROVE_HIDDEN = {"descriptor": "hidden grove", "adjectives": [], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_GULLY = {"descriptor": "gully", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HALL = {"descriptor": "hall", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HIDEOUT = {"descriptor": "hideout", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HILL = {"descriptor": "hill", "adjectives": [ADJ_FLOWER_COVERED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HILL_CREST = {"descriptor": "hill crest", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HOLLOW = {"descriptor": "hollow", "adjectives": [], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HOMESTEAD = {"descriptor": "homestead", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HOUSE_MAYOR = {"descriptor": "mayor's house", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HUT_MARSH = {"descriptor": "hut (marsh)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HUT_SHEPHERDING = {"descriptor": "hut (shepherding)", "adjectives": [], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_HUT_WITCH = {"descriptor": "hut (witch's)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_IDOL = {"descriptor": "idol (ancient)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_INFIRMARY = {"descriptor": "infirmary", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_INN = {"descriptor": "inn", "adjectives": [ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED], "encounters": [ENCOUNTER_REST, ENCOUNTER_SOCIAL, ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ISLAND = {"descriptor": "island", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE, ENCOUNTER_REST, ENCOUNTER_SOCIAL]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ISLAND_DUCK = {"descriptor": "island (duck)", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_PUZZLE, ENCOUNTER_REST, ENCOUNTER_SOCIAL]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ISLAND_REEDY = {"descriptor": "island (reedy)", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE, ENCOUNTER_REST, ENCOUNTER_SOCIAL]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_JETTY = {"descriptor": "jetty", "adjectives": [ADJ_SLIPPERY, ADJ_OLD], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_KITCHEN = {"descriptor": "kitchen", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_KNOLL = {"descriptor": "knoll", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LAIR = {"descriptor": "lair", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LAKE = {"descriptor": "lake", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LANDING = {"descriptor": "landing (longboat)", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LANDSLIDE = {"descriptor": "landslide", "adjectives": [ADJ_OLD, ADJ_FRESH], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LATRINE = {"descriptor": "latrine", "adjectives": [ADJ_ODOUROUS], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LEDGE = {"descriptor": "ledge", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LIGHTS = {"descriptor": "lights (marsh)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LODGE_HUNTING = {"descriptor": "lodge (hunting)", "adjectives": [ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LOG_FALLEN = {"descriptor": "log (fallen) ", "adjectives": [ADJ_ROTTING, ADJ_FRESHLY, ADJ_LIGHTING_STRUCK, ADJ_MUSHROOM_COVERED, ADJ_LICHEN_COVERED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_LOG_FLOATING = {"descriptor": "log (floating)", "adjectives": [ADJ_ROTTING, ADJ_FRESHLY, ADJ_SMELLY, ADJ_ODOUROUS, ADJ_SLIPPERY, ADJ_MUSHROOM_COVERED, ADJ_LICHEN_COVERED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MARKET = {"descriptor": "market", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MARKET_FISH = {"descriptor": "market (fish)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MARSH = {"descriptor": "marsh", "adjectives": [ADJ_ODOUROUS], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MEADOW = {"descriptor": "meadow", "nouns": ["wildflower"], "adjectives": [ADJ_IDYLLIC], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_SOCIAL]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MESS_HALL = {"descriptor": "mess hall", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MINE = {"descriptor": "mine", "adjectives": [ADJ_ABANDONED, ADJ_DESERTED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MOAT = {"descriptor": "moat", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MOSSBED = {"descriptor": "mossbed", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MOUND_BARROW = {"descriptor": "mound (barrow)", "adjectives": [], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_MOUNTAIN = {"descriptor": "mountain", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_NAZE = {"descriptor": "naze", "adjectives": [ADJ_PROMINENT], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_NEST = {"descriptor": "nest", "adjectives": [ADJ_ABANDONED, ADJ_OCCUPIED]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_NEST_EAGLE = {"descriptor": "nest (eagle's)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_OFFICE_QUARTERMASER = {"descriptor": "quartermaster's office", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ORCHARD = {"descriptor": "orchard", "adjectives": [ADJ_OLD], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_OUTCROP = {"descriptor": "outcrop", "adjectives": [ADJ_ROCKY, ADJ_PRECARIOUS, ADJ_CRUMBLING, ADJ_OVERGROWN, ADJ_JAGGED, ADJ_SHARP, ADJ_ERODED, ADJ_RUGGED, ADJ_SCENIC, ADJ_STRIATED, ADJ_EXPOSED, ADJ_CRYSTALLINE, ADJ_ANCIENT, ADJ_VOLCANIC, ADJ_SEDIMENTARY, ADJ_GEOLOGICAL, ADJ_STONY, ADJ_FOSSILIZED, ADJ_PROMINENT, ADJ_BARE, ADJ_TOWERING, ADJ_GRANITIC, ADJ_PRECIPITOUS], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_OUTPOST_OBSERVATION = {"descriptor": "outpost (observation)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_OUTPOST_TRADING = {"descriptor": "outpost (trading)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PADDOCK = {"descriptor": "paddock", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PASSAGE = {"descriptor": "passage", "adjectives": [ADJ_TWISTING, ADJ_NARROW, ADJ_CRUMBLING], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_TRAP, ENCOUNTER_HAZARD]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PATCH = {"descriptor": "patch", "nouns": ["wildflower"], "adjectives": [ADJ_OVERGROWN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PATCH_LICHEN = {"descriptor": "patch (lichen)", "adjectives": [ADJ_FLOODED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PATH = {"descriptor": "path", "adjectives": [ADJ_PINE_CONE_LITTERED, ADJ_LEAF_STREWN, ADJ_NARROW], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PEAK = {"descriptor": "peak", "adjectives": [ADJ_BARREN], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PILE_DRIFTWOOD = {"descriptor": "pile (driftwood)", "adjectives": [ADJ_SLIPPERY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PILE_LEAF = {"descriptor": "pile (leaf)", "adjectives": [ADJ_SLIPPERY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PILLAR = {"descriptor": "pillar", "nouns": ["stone"], "adjectives": [ADJ_ANCIENT], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PIT_SINKING = {"descriptor": "pit (sinking)", "adjectives": [ADJ_FLOWER_COVERED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PLATEAU = {"descriptor": "plateau", "adjectives": [ADJ_FLOWER_COVERED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_POND = {"descriptor": "pond", "adjectives": [ADJ_STAGNANT, ADJ_FETID, ADJ_MUDDY, ADJ_FOUL, ADJ_STINKING, ADJ_FOUL_SMELLING, ADJ_QUIET]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_POOL = {"descriptor": "pool", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_REST, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_POOL_ALLIGATOR = {"descriptor": "pool (alligator)", "adjectives": [ADJ_PEACEFUL], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_POOL_BOG = {"descriptor": "bog pool", "adjectives": [ADJ_ODOUROUS], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_POOL_MARSH = {"descriptor": "marsh pool", "adjectives": [ADJ_SANDY, ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_POOL_UNDERGROUND = {"descriptor": "undergound pool", "adjectives": [ADJ_SANDY, ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PRAIRIE = {"descriptor": "prairie", "adjectives": [ADJ_SANDY, ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_PRECIPICE = {"descriptor": "precipice", "adjectives": [ADJ_SANDY, ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_QUAGMIRE = {"descriptor": "quagmire", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_QUARRY = {"descriptor": "quarry", "adjectives": [ADJ_SANDY, ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_QUARTERS_COMMANDER = {"descriptor": "commander's quarter's", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_QUARTERS_OFFICER = {"descriptor": "officer's quarters", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RAPIDS = {"descriptor": "rapids", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RAVINE = {"descriptor": "ravine", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RIDGE = {"descriptor": "ridge", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RING_FAIRY = {"descriptor": "ring (fairy)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RIVER = {"descriptor": "river", "adjectives": [ADJ_RAPID], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RIVERBED = {"descriptor": "riverbed", "adjectives": [ADJ_ROCKY, ADJ_MUDDY, ADJ_SANDY, ADJ_DRY, ADJ_FLOODED, ADJ_DAMP, ADJ_OVERGROWN, ADJ_SUN_BAKED, ADJ_LUSH, ADJ_BARREN, ADJ_WINDING, ADJ_DEEP, ADJ_SHALLOW, ADJ_RUGGED, ADJ_SLIPPERY, ADJ_SMOOTH, ADJ_PEBBLY, ADJ_SHADOWY, ADJ_MEANDERING, ADJ_SERENE], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RIVER_BANK = {"descriptor": "river bank", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RIVER_BEND = {"descriptor": "river bend", "adjectives": [ADJ_MEANDERING, ADJ_SERENE, ADJ_PICTURESQUE, ADJ_TWISTING, ADJ_FLOWING, ADJ_TRANQUIL, ADJ_LUSH, ADJ_WINDING, ADJ_SWEEPING, ADJ_MURMURING, ADJ_VERDANT, ADJ_PEACEFUL, ADJ_SHIMMERING, ADJ_GLISTENING, 'inviting', 'scenic', 'undulating', 'quiet', 'rustic', ADJ_IDYLLIC], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RIVER_UNDERGROUND = {"descriptor": "river (underground)", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ROOM_STORAGE = {"descriptor": "room (storage)", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ROOST = {"descriptor": "roost", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_ROOT = {"descriptor": "root", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RUINS = {"descriptor": "ruins", "adjectives": [ADJ_TUMBLEDOWN, ADJ_BURNT_OUT, ADJ_CRUMBLING], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_RUINS_HILL_FORT = {"descriptor": "ruins (hill fort)", "adjectives": [], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SCHOOLHOUSE = {"descriptor": "schoolhouse", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SCRUB = {"descriptor": "scrub", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SEA_VIEW = {"descriptor": "sea view", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SEWER = {"descriptor": "sewer", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SHALLOWS = {"descriptor": "shallows", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SHELF = {"descriptor": "shelf", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SHOP_COBBLER = {"descriptor": "shop (cobbler's)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SHORE_REEDY = {"descriptor": "shore (reedy)", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SLOPE = {"descriptor": "slope", "adjectives": [ADJ_ROCKY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SLOPE_SCREE = {"descriptor": "slope (scree)", "adjectives": [ADJ_FRESH], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_HAZARD]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SPRING = {"descriptor": "spring", "adjectives": [ADJ_OLD], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SPRING_HOT = {"descriptor": "spring (hot)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SPRING_MOUNTAIN = {"descriptor": "spring (mountain)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SPRING_UNDERGROUND = {"descriptor": "spring (underground)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SQUARE = {"descriptor": "square", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_STABLE = {"descriptor": "stable", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_STAGS_LEAP = {"descriptor": "stag's leap", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_HAZARD, ENCOUNTER_SKIRMISH, ENCOUNTER_SOCIAL]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_STALACTITES = {"descriptor": "stalactites", "adjectives": [ADJ_DRIPPING], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_STALAGMITES = {"descriptor": "stalagmites", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_STAND = {"descriptor": "stand", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_STOCKAdE = {"descriptor": "stockade", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_STORE_GENERAL = {"descriptor": "general store", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_STREAM = {"descriptor": "stream", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_STREAM_UNDERGROUND = {"descriptor": "stream (underground)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SWAMP = {"descriptor": "swamp", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TAVERN = {"descriptor": "tavern", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_THICKET = {"descriptor": "thicket", "adjectives": [ADJ_BUSHY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TIMBERLAND = {"descriptor": "timberland", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TOWER = {"descriptor": "tower", "nouns": ["guard"], "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TRAIL = {"descriptor": "trail", "nouns": ["animal", "cart", "woodland"], "adjectives": [ADJ_DUSTY, ADJ_OVERGROWN, ADJ_MUDDY, ADJ_ROUGH, ADJ_RUGGED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TRAINING_GROUND = {"descriptor": "training ground", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TREE = {"descriptor": "tree", "adjectives": [ADJ_ANCIENT, ADJ_FALLEN, ADJ_HOLLOW, ADJ_LONE, ADJ_STANDING], "nouns": ["archway", "lone", "stump"], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_REST, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TREE_LINE = {"descriptor": "tree-line", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TREE_TUNNEL = {"descriptor": "tunnel (tree)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TREE_WILLOW = {"descriptor": "  (willow)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TRENCH = {"descriptor": "trench", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TRUNK = {"descriptor": "trunk", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_TUNNEL = {"descriptor": "tunnel", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_UNDERBRUSH = {"descriptor": "underbrush", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_UNDERGROWTH = {"descriptor": "undergrowth", "adjectives": [ADJ_BUSHY], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_UNDERSTORY = {"descriptor": "understory", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_VALLEY = {"descriptor": "valley", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_VALUE = {"descriptor": "vale", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_VILLAGE = {"descriptor": "village (fishing)", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_VINE = {"descriptor": "vine", "nouns": "tangle", "adjectives": [ADJ_CREEPING], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WAGON_RUTS = {"descriptor": "wagon ruts", "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WALL = {"descriptor": "wall", "adjectives": [ADJ_GLISTENING, ADJ_FOSSIL], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WATCHPOST = {"descriptor": "watch post", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WATCHTOWER = {"descriptor": "watchtower", "adjectives": [ADJ_ABANDONED, ADJ_OLD, ADJ_RUINED, ADJ_HOSTILE, ADJ_BURNT_OUT], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_REST]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WATERFALL = {"descriptor": "waterfall", "adjectives": [ADJ_IDYLLIC, ADJ_WHISPERING], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WATER_WELL = {"descriptor": "water well", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_SPOT_WILL_O_WISP = {"descriptor": "will-o'-the-wisp spot", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WORKSHOP_ARTISAN = {"descriptor": "workshop (artisan's)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WORKSHOP_BLACKSMITH = {"descriptor": "workshop (blacksmith's)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WORKSHOP_CARPENTER = {"descriptor": "workshop (carpenter's)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}
    # TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
    LOC_WORKSHOP_WEAVER = {"descriptor": "workshop (weaver's)", "adjectives": [ADJ_ABANDONED], "encounters": [ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE]}

    locations = [
        LOC_ALCOVE,
        LOC_ANIMAL_BURROW,
        LOC_ANIMAL_PENS,
        LOC_APOTHECARY,
        LOC_ARMORY,
        LOC_MARSH,
        LOC_CANYON,
        LOC_CANYON_FLOOR,
        LOC_CAVE,
        LOC_ISLAND,
        LOC_ISLAND_DUCK,
        LOC_AVALANCHE_SITE,
        LOC_POOL_MARSH,
        LOC_JETTY,
        LOC_BAKERY,
        LOC_BARN,
        LOC_BARNYARD,
        LOC_BARRACKS,
        LOC_BOAT,
        LOC_WALL,
        LOC_WATERFALL,
        LOC_WATCHPOST,
        LOC_UNDERBRUSH,
        LOC_UNDERGROWTH,
        LOC_TRENCH,
        LOC_TREE,
        LOC_TRUNK,
        LOC_THICKET,
        LOC_TOWER,
        LOC_VINE,
        LOC_FJORD,
        LOC_CAVE_ENTRANCE,
        LOC_CAVE_MOUTH,
        LOC_WORKSHOP_ARTISAN,
        LOC_WORKSHOP_BLACKSMITH,
        LOC_WORKSHOP_CARPENTER,
        LOC_WORKSHOP_WEAVER,
        LOC_SPRING,
        LOC_TREE_TUNNEL,
        LOC_RIVER,
        LOC_RAPIDS,
        LOC_BRIDGE,
        LOC_RIVER_BANK,
        LOC_RIVER_BEND,
        LOC_MOUNTAIN,
        LOC_MOUNTAIN_PASS,
        LOC_SPRING_MOUNTAIN,
        LOC_LAKE,
        LOC_MEADOW,
        LOC_HILL,
        LOC_SWAMP,
        LOC_CAVERN,
        LOC_PATCH,
        LOC_POOL,
        LOC_BOG,
        LOC_BOGGY_PATCH,
        LOC_POOL_BOG,
        LOC_OUTPOST_OBSERVATION,
        LOC_OUTPOST_TRADING,
        LOC_HILL_CREST,
        LOC_POOL_UNDERGROUND,
    ]

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_WOODLAND = {
        "zone": "woodland",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_WATCHPOST, LOC_WATERFALL, LOC_UNDERGROWTH, LOC_UNDERBRUSH, LOC_TRENCH, LOC_TREE, LOC_VINE, LOC_TRUNK, LOC_THICKET, LOC_TOWER, LOC_SPRING]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_FOREST = {
        "zone": "forest",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_WATERFALL, LOC_TREE, LOC_TREE_TUNNEL]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_RIVER = {
        "zone": "river",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_RIVER, LOC_BRIDGE, LOC_RIVER_BANK, LOC_RIVER_BEND, LOC_FJORD, LOC_RAPIDS]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_MOUNTAIN = {
        "zone": "mountain",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_MOUNTAIN, LOC_SPRING_MOUNTAIN, LOC_MOUNTAIN_PASS]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_LAKE = {
        "zone": "lake",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_LAKE, LOC_JETTY]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_MARSH = {
        "zone": "marsh",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_MARSH, LOC_POOL_MARSH, LOC_ISLAND, LOC_ISLAND_DUCK]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_CANYON = {
        "zone": "canyon",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_CANYON, LOC_CANYON_FLOOR]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_CAVE = {
        "zone": "cave",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_CAVE, LOC_CAVE_ENTRANCE, LOC_CAVE_MOUTH, LOC_POOL_UNDERGROUND]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_HILL = {
        "zone": "hill",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_HILL, LOC_HILL_CREST]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_MEADOW = {
        "zone": "meadow",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_MEADOW]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_CAVERN = {
        "zone": "cavern",
        "locations_to_use": {"minimum": 2, "maximum": 9},
        "locations": [LOC_CAVERN]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_SWAMP = {
        "zone": "swamp",
        "locations_to_use": {"minimum": 4, "maximum": 8},
        "locations": [LOC_SWAMP, LOC_BOAT, LOC_PATCH, LOC_BRIDGE, LOC_POOL]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_BOG = {
        "zone": "bog",
        "locations_to_use": {"minimum": 2, "maximum": 3},
        "locations": [LOC_BOG, LOC_BOGGY_PATCH, LOC_POOL_BOG, LOC_BOAT, LOC_TREE]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_OUTPOST = {
        "zone": "outpost",
        "locations_to_use": {"minimum": 3, "maximum": 6},
        "locations": [LOC_OUTPOST_OBSERVATION, LOC_OUTPOST_TRADING]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_WATCHTOWER = {
        "zone": "outpost",
        "locations_to_use": {"minimum": 3, "maximum": 6},
        "locations": [LOC_WATCHTOWER, LOC_TRENCH, LOC_MOAT, LOC_WATCHPOST, LOC_GATEHOUSE, LOC_ALCOVE, LOC_ARMORY, LOC_MESS_HALL, LOC_BRIDGE]
    }

    # TODO add in more locations to the locations field that would be relevant to the zone type
    ZONE_VILLAGE = {
        "zone": "outpost",
        "locations_to_use": {"minimum": 3, "maximum": 6},
        "locations": [LOC_BRIDGE, LOC_BAKERY, LOC_MARKET, LOC_MARKET_FISH, LOC_WORKSHOP_BLACKSMITH, LOC_WORKSHOP_CARPENTER, LOC_WORKSHOP_WEAVER]
    }

    zones = [
        ZONE_WOODLAND,
        ZONE_FOREST,
        ZONE_RIVER,
        ZONE_MOUNTAIN,
        ZONE_LAKE,
        ZONE_MARSH,
        ZONE_CANYON,
        ZONE_CAVE,
        ZONE_HILL,
        ZONE_MEADOW,
        ZONE_CAVERN,
        ZONE_SWAMP,
        ZONE_BOG,
        ZONE_OUTPOST,
    ]

    environments = [
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "highland wilderness",
            "levels": {"minimum": 1, "maximum": 10},
            "zones": [ZONE_WOODLAND, ZONE_FOREST, ZONE_RIVER, ZONE_MOUNTAIN, ZONE_LAKE, ZONE_MARSH, ZONE_CANYON, ZONE_CAVE, ZONE_HILL, ZONE_MEADOW, ZONE_CAVERN, ZONE_SWAMP, ZONE_BOG, ZONE_OUTPOST],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE],
        },

        # watchtowers
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "abandoned watchtower",
            "adjectives": ["abandoned, ruined, derelict, deserted, empty, forsaken, neglected, uninhabited, unoccupied, vacant"],
            "levels": {"minimum": 1, "maximum": 10},
            "zones": [ZONE_WOODLAND, ZONE_RIVER, ZONE_WATCHTOWER],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
        },
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "haunted watchtower",
            "adjectives": ["haunted", "ghostly", "ghastly", "spectral", "undead", "unearthly"],
            "levels": {"minimum": 3, "maximum": 10},
            "zones": [ZONE_WATCHTOWER],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
        },
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "evil watchtower",
            "adjectives": ["haunted", "cursed", "evil", "demonic", "ghostly", "ghastly", "spectral", "spiritual", "supernatural", "undead", "unearthly", "vampiric", "zombie"],
            "levels": {"minimum": 7, "maximum": 10},
            "zones": [ZONE_WATCHTOWER],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
        },
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "populated watchtower populated",
            "levels": {"minimum": 1, "maximum": 10},
            "zones": [ZONE_WATCHTOWER],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
        },
        # villages
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "abandoned village",
            "adjectives": ["abandoned, ruined, derelict, deserted, empty, forsaken, neglected, uninhabited, unoccupied, vacant"],
            "levels": {"minimum": 1, "maximum": 10},
            "zones": [ZONE_VILLAGE],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
        },
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "populated village",
            "adjectives": ["populated", "inhabited", "occupied", "peopled", "settled", "tenanted"],
            "levels": {"minimum": 1, "maximum": 10},
            "zones": [ZONE_VILLAGE],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
        },
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "populated fishing village",
            "adjectives": ["populated", "inhabited", "occupied", "peopled", "settled", "tenanted", "fishing"],
            "levels": {"minimum": 1, "maximum": 10},
            "zones": [ZONE_VILLAGE],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
        },
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "fortified village",
            "adjectives": ["fortified"],
            "levels": {"minimum": 1, "maximum": 10},
            "zones": [ZONE_VILLAGE],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
        },
        # TODO add in more zones to the zones field that would be relevant to the environment type
        # TODO add in more adjectives to the adjectives field that would be relevant to the environment type
        {
            "type": "haunted village",
            "adjectives": ["haunted", "ghostly", "ghastly", "spectral", "undead", "unearthly"],
            "levels": {"minimum": 1, "maximum": 10},
            "zones": [ZONE_VILLAGE],
            "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
            "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE, CLIMATE_DESERT, CLIMATE_TUNDRA, CLIMATE_TROPICAL, CLIMATE_POLAR],
        },

        # {
        #     "type": "oasis",
        #
        #     "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
        #     "climates": [CLIMATE_ALPINE, CLIMATE_DESERT]
        # },
        # {
        #     "type": "mountainous",
        #     "subtypes": [],
        #     "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
        #     "climates": [CLIMATE_TEMPERATE, CLIMATE_ALPINE]
        # },
        # {
        #     "type": "ruins",
        #     "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER],
        #     "climates": [CLIMATE_TEMPERATE, CLIMATE_DESERT, CLIMATE_TROPICAL, CLIMATE_ALPINE, CLIMATE_POLAR]
        # },
        # {
        #     "type": "dungeon",
        #     "seasons": [SEASON_CONSTANT],
        #     "climates": [CLIMATE_SUBTERRANEAN],
        #     "locations": []
        # },
        # {"type": "underground caverns", "seasons": [SEASON_CONSTANT], "climates": [CLIMATE_SUBTERRANEAN]},
        # {"type": "swampland", "seasons": ["spring", "summer", "autumn", "winter"], "climates": [CLIMATE_TROPICAL, CLIMATE_TEMPERATE]},
        # {"type": "coastal", "seasons": ["spring", "summer", "autumn", "winter"], "climates": [CLIMATE_TROPICAL, CLIMATE_TEMPERATE, CLIMATE_POLAR]},
        # {"type": "urban", "seasons": ["spring", "summer", "autumn", "winter"], "climates": [CLIMATE_TEMPERATE, CLIMATE_DESERT, CLIMATE_TROPICAL, CLIMATE_POLAR]},
        # {"type": "arctic", "seasons": [SEASON_SUMMER, SEASON_WINTER], "climates": [CLIMATE_POLAR]},
        # {"type": "jungle", "seasons": [SEASON_SPRING, SEASON_SUMMER, SEASON_AUTUMN, SEASON_WINTER], "climates": [CLIMATE_TROPICAL]},
    ]

    @classmethod
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
    def verify_locations(cls, locations, encounter_types, valid_adjectives):
        descriptors = []
        for location in locations:
            # Check if all required fields are in each location
            if not all(k in location for k in ("descriptor", "adjectives", "encounters")):
                missing_keys = [k for k in ("descriptor", "adjectives", "encounters") if k not in location]
                raise ValueError(f"Location {location} is missing keys: {missing_keys}")

            # Check if the descriptor is unique
            if location['descriptor'] in descriptors:
                raise ValueError(f"Descriptor '{location['descriptor']}' is not unique.")
            descriptors.append(location['descriptor'])

            # Check if there's at least one adjective and no duplicate adjectives
            if not location['adjectives'] or len(location['adjectives']) != len(set(location['adjectives'])):
                if not location['adjectives']:
                    raise ValueError(f"Location {location['descriptor']} does not contain any adjectives.")
                else:
                    raise ValueError(f"Location {location['descriptor']} contains duplicate adjectives.")

            # Check if the adjectives are in the valid_adjectives list
            invalid_adjectives = set(location['adjectives']) - set(valid_adjectives)
            if invalid_adjectives:
                raise ValueError(f"Location {location['descriptor']} contains invalid adjectives: {invalid_adjectives}")

            # Check if there's at least one encounter
            if not location['encounters']:
                raise ValueError(f"Location {location['descriptor']} does not contain any encounters.")

            # Check if all encounters are valid and there are no duplicates
            invalid_encounters = set(location['encounters']) - set(encounter_types)
            duplicate_encounters = len(location['encounters']) != len(set(location['encounters']))
            if invalid_encounters:
                raise ValueError(f"Location {location['descriptor']} contains invalid encounters: {invalid_encounters}")
            elif duplicate_encounters:
                raise ValueError(f"Location {location['descriptor']} contains duplicate encounters.")

        return True

    @classmethod
    def verify_zones(cls, zones, locations):
        location_descriptors = {location['descriptor'] for location in locations}
        for zone in zones:
            print(f"Checking zone {zone}")
            # Check if 'zone' key is present and is a string
            if 'zone' not in zone or not isinstance(zone['zone'], str):
                raise ValueError(f"Zone entry {zone} does not contain a 'zone' key or the key is not a string.")

            cls.verify_locations_to_use(zone)
            cls.verify_locations_list(location_descriptors, zone)

        return True

    @classmethod
    def verify_locations_list(cls, location_descriptors, zone):
        # Check 'locations' key exists, is a list, and has at least one entry
        if 'locations' not in zone or not isinstance(zone['locations'], list) or not zone['locations']:
            raise ValueError(f"Zone {zone['zone']} does not contain a 'locations' key, or the key is not a list, or the list is empty.")
        # Check all items in 'locations' list exist in location_descriptors and there are no duplicates
        for location in zone['locations']:
            if location['descriptor'] not in location_descriptors:
                raise ValueError(f"Zone {zone['zone']} contains invalid location: {location['descriptor']}")
        print([location['descriptor'] for location in zone['locations']])
        print(len(zone['locations']))
        if len(zone['locations']) != len(set([location['descriptor'] for location in zone['locations']])):
            from collections import Counter
            location_counts = Counter(zone['locations'])
            duplicates = [k for k, v in location_counts.items() if v > 1]
            raise ValueError(f"Zone {zone['zone']} contains duplicate locations: {duplicates}")

    @classmethod
    def verify_locations_to_use(cls, zone):
        # Check 'locations_to_use' key exists, is a dictionary, and has 'minimum' and 'maximum' keys
        if 'locations_to_use' not in zone or not isinstance(zone['locations_to_use'], dict):
            raise ValueError(f"Zone {zone['zone']} does not contain a 'locations_to_use' key or the key is not a dictionary.")
        if 'minimum' not in zone['locations_to_use'] or 'maximum' not in zone['locations_to_use']:
            raise ValueError(f"Zone {zone['zone']} does not contain 'minimum' and 'maximum' keys in 'locations_to_use'.")
        # Check 'minimum' and 'maximum' values are numeric and minimum is less than maximum
        if not isinstance(zone['locations_to_use']['minimum'], (int, float)) or not isinstance(zone['locations_to_use']['maximum'], (int, float)):
            raise ValueError(f"Zone {zone['zone']} has non-numeric 'minimum' or 'maximum' values in 'locations_to_use'.")
        if zone['locations_to_use']['minimum'] >= zone['locations_to_use']['maximum']:
            raise ValueError(f"Zone {zone['zone']} has 'minimum' value greater than or equal to 'maximum' in 'locations_to_use'.")

    @classmethod
    def verify_seasons(cls, seasons):
        if not isinstance(seasons, list) or not seasons:
            raise ValueError("The 'seasons' key must exist and it must be a non-empty list.")
        if len(seasons) != len(set(seasons)):
            from collections import Counter
            season_counts = Counter(seasons)
            duplicates = [k for k, v in season_counts.items() if v > 1]
            raise ValueError(f"'seasons' contains duplicate seasons: {duplicates}")
        if not set(seasons).issubset(SEASON_TYPES):
            invalid_seasons = set(seasons) - set(SEASON_TYPES)
            raise ValueError(f"'seasons' contains invalid seasons: {invalid_seasons}")
        return True

    @classmethod
    def verify_climates(cls, climates):
        if not isinstance(climates, list) or not climates:
            raise ValueError("The 'climates' key must exist and it must be a non-empty list.")
        if len(climates) != len(set(climates)):
            from collections import Counter
            climate_counts = Counter(climates)
            duplicates = [k for k, v in climate_counts.items() if v > 1]
            raise ValueError(f"'climates' contains duplicate climates: {duplicates}")
        if not set(climates).issubset(CLIMATE_TYPES):
            invalid_climates = set(climates) - set(CLIMATE_TYPES)
            raise ValueError(f"'climates' contains invalid climates: {invalid_climates}")
        return True

    @classmethod
    def validate_data(cls):
        cls.check_for_duplicates(cls.adjectives)
        cls.verify_environments(cls.environments, cls.zones)
        cls.verify_zones(cls.zones, cls.locations)
        cls.verify_locations(cls.locations, ENCOUNTER_TYPES, cls.adjectives)

    @classmethod
    def check_for_duplicates(cls, adjectives):
        # Converting the list to a set will remove any duplicates because sets cannot contain duplicate values
        # If the length of the set is less than the length of the list, that means there were duplicates
        if len(set(adjectives)) < len(adjectives):
            # Creating a dictionary with counts of each adjective
            from collections import Counter
            adj_counts = Counter(adjectives)

            # Find the adjectives where count is more than 1, those are our duplicates
            duplicates = [k for k, v in adj_counts.items() if v > 1]
            raise ValueError(f"The following adjectives are duplicated: {duplicates}")

    @classmethod
    def verify_environments(cls, environments, zones):
        for env in environments:
            # Verify 'type' key
            if 'type' not in env or not isinstance(env['type'], str) or not env['type']:
                raise ValueError("Each environment must have a 'type' key, it must be a string, and it cannot be empty.")
            print(env['type'])

            # Verify 'zones' key
            if 'zones' not in env or not isinstance(env['zones'], list) or not env['zones']:
                raise ValueError("Each environment must have a 'zones' key, it must be a list, and it cannot be empty.")

            env_zone_names = [zone['zone'] for zone in env['zones']]
            valid_zone_names = [zone['zone'] for zone in zones]

            if not set(env_zone_names).issubset(valid_zone_names):
                invalid_zones = set(env_zone_names) - set(valid_zone_names)
                raise ValueError(f"'zones' contains invalid zones: {invalid_zones}")

            if len(env_zone_names) != len(set(env_zone_names)):
                from collections import Counter
                zone_counts = Counter(env_zone_names)
                duplicates = [k for k, v in zone_counts.items() if v > 1]
                raise ValueError(f"'zones' contains duplicate zones: {duplicates}")

            cls.verify_seasons(env.get('seasons', []))
            cls.verify_climates(env.get('climates', []))

        return True

    # TODO create a list of environments that cover the specified level of the party
    # TODO pick a random environment from that list
    # TODO pick the season and climate that the environment supports
    # TODO decide on how manyy zones we will use and limit it to the number of zones in the environment
    # TODO select a random set of zones
    # TODO decide how many locations will be in each zone, this is zone specific, different zones will have a different number of locations
    # TODO select a random set of locations from the zone
    # TODO set the adjectives for the zone
    # TODO select a random encounter type for each location
    # TODO select the adjectives for the location
    # TODO select the nouns for the location
    # TODO build the graph for the environment
    # TODO set all of the connections for each location from the graph
    # TODO send the entire map to the GPT4 model to generate the descriptions for each location
    # TODO generate npcs for each skirmish & boss fight encounter
    # TODO generate loot for each skirmish & boss fight encounter
    # TODO generate the puzzles for each puzzle encounter
    # TODO generate the traps for each trap encounter
    # TODO generate the treasure for each puzzle encounter
    # TODO generate traps for each puzzle encounter
    # TODO generate the social encounters for each social encounter
    # TODO generate the main quest
    # TODO generate the side quest
    # TODO generate the npcs for the main quest
    # TODO generate the npcs for the side quest
    # TODO generate the loot for the main quest
    # TODO generate the loot for the side quest
    # TODO generate how each hazard encounter will manifest itself
    # TODO generate how each exploration encounter will manifest itself


EnvironmentGenerator.validate_data()
