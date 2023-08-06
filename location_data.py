from encounter_data import *
from adjective_data import *
from noun_data import *
from location_types import LocationData

LOC_MOUNTAIN_PASS2 = LocationData(
    descriptor='mountain pass',
    nouns=[NOUN_TRAIL, NOUN_PATH, NOUN_ROUTE, NOUN_CORRIDOR, NOUN_CANYON, NOUN_GAP, NOUN_CLIFF, NOUN_PEAK, NOUN_VALLEY, NOUN_GORGE],
    adjectives=[ADJ_ROCKY, ADJ_WINDING, ADJ_RUGGED, ADJ_SHADOWY, ADJ_JAGGED, ADJ_NARROW, ADJ_STONY, ADJ_SCENIC, ADJ_ROUGH, ADJ_PRECIPITOUS, ADJ_LOOMING, ADJ_GRANITIC, ADJ_BARE, ADJ_MAJESTIC, ADJ_TOWERING, ADJ_PRECARIOUS, ADJ_PICTURESQUE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])

LOC_ALCOVE2 = LocationData(
    descriptor='alcove (hidden)',
    nouns=[NOUN_CAVE, NOUN_GROTTO, NOUN_HIDEAWAY, NOUN_RETREAT, NOUN_SANCTUARY, NOUN_RECESS, NOUN_HIDING_PLACE, NOUN_SECRET_SPOT, NOUN_DEN, NOUN_HOLLOW],
    adjectives=[ADJ_HIDDEN, ADJ_SECLUDED, ADJ_SHADOWY, ADJ_NARROW, ADJ_QUIET, ADJ_MOSSY, ADJ_DAMP, ADJ_COOL, ADJ_SILENT, ADJ_PEACEFUL, ADJ_LONE, ADJ_HUSHED, ADJ_VERDANT, ADJ_STONY, ADJ_FRESH, ADJ_DIMLY_LIT, ADJ_GLOOMY, ADJ_MYSTICAL, ADJ_SERENE, ADJ_STRATEGIC, ADJ_UNDISTURBED, ADJ_HUMID, ADJ_SUNKEN, ADJ_ISOLATED, ADJ_OVERGROWN, ADJ_ENCHANTED, ADJ_WINDLESS, ADJ_COVERED, ADJ_FORGOTTEN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST])

LOC_ALTAR2 = LocationData(
    descriptor='altar',
    nouns=[NOUN_SANCTUARY, NOUN_SHRINE, NOUN_RELIC, NOUN_PODIUM, NOUN_MONUMENT, NOUN_STATUE, NOUN_TABLE, NOUN_PLATFORM, NOUN_PILLAR, NOUN_STAND],
    adjectives=[ADJ_ANCIENT, ADJ_HOLY, ADJ_RUNE_COVERED, ADJ_MOSS_COVERED, ADJ_ABANDONED, ADJ_SHADOWY, ADJ_IDYLLIC, ADJ_FLOURISHING, ADJ_BARE, ADJ_STONY, ADJ_VERDANT, ADJ_CRUMBLING, ADJ_FORTIFIED, ADJ_RUINED, ADJ_TWISTED, ADJ_DECAYING, ADJ_GNARLED, ADJ_TORMENTED, ADJ_TIME_WORN, ADJ_SACRIFICIAL],
    encounters=[ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST, ENCOUNTER_REST])

LOC_ANIMAL_BURROW2 = LocationData(
    descriptor='animal burrow',
    nouns=[NOUN_DEN, NOUN_HOLE, NOUN_TUNNEL, NOUN_HIDEOUT, NOUN_LAIR, NOUN_HABITAT, NOUN_NEST, NOUN_RETREAT, NOUN_DUGOUT, NOUN_SHELTER],
    adjectives=[ADJ_ABANDONED, ADJ_COLLAPSED, ADJ_OCCUPIED, ADJ_DEEP, ADJ_NARROW, ADJ_WINDING, ADJ_DARK, ADJ_DAMP, ADJ_MUDDY, ADJ_FRESHLY, ADJ_SHADOWY, ADJ_HIDDEN, ADJ_OVERGROWN, ADJ_TWISTING, ADJ_MUSHROOM_COVERED, ADJ_ROOT_RIDDLED, ADJ_FERN_FILLED, ADJ_COZY, ADJ_FOUL_SMELLING, ADJ_LEAF_STREWN, ADJ_FLOURISHING, ADJ_UNDERGROWTH, ADJ_BUSHY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE])

LOC_ANIMAL_PENS2 = LocationData(
    descriptor='animal pen',
    nouns=[NOUN_BARN, NOUN_SHED, NOUN_ENCLOSURE, NOUN_YARD, NOUN_STABLE, NOUN_STY, NOUN_COOP, NOUN_KENNEL, NOUN_CORRAL, NOUN_PASTURE],
    adjectives=[ADJ_ABANDONED, ADJ_COLLAPSED, ADJ_OCCUPIED, ADJ_ODOUROUS, ADJ_HOSTILE, ADJ_BURNT_OUT, ADJ_DESERTED, ADJ_CRUMBLING, ADJ_DISORDERLY, ADJ_CLEAN, ADJ_MUDDY, ADJ_WEATHERED, ADJ_STINKING, ADJ_CLUTTERED, ADJ_DILAPIDATED, ADJ_SQUALID, ADJ_FORSAKEN, ADJ_DINGY, ADJ_TIDY, ADJ_FILTHY, ADJ_RUN_DOWN, ADJ_URBAN, ADJ_OVERGROWN, ADJ_FARMYARD, ADJ_PASTORAL, ADJ_SPACIOUS],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST, ENCOUNTER_REST])

# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_APOTHECARY2 = LocationData(
    descriptor="apothecary",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])

# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_ARMORY2 = LocationData(
    descriptor="armory",
    adjectives=[ADJ_EMPTIED, ADJ_SCOURED, ADJ_PARTIALLY_STOCKED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_REST])

# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_AVALANCHE_SITE2 = LocationData(
    descriptor="avalanche site",
    adjectives=[ADJ_FRESH],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BAKERY2 = LocationData(
    descriptor="bakery",
    adjectives=[ADJ_ABANDONED, ADJ_BURNT_OUT],
    encounters=[ENCOUNTER_SOCIAL, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BARN2 = LocationData(
    descriptor="barn",
    adjectives=[ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_OCCUPIED, ADJ_HOSTILE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BARNYARD2 = LocationData(
    descriptor="barnyard",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BARRACKS2 = LocationData(
    descriptor="barracks",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BEACH2 = LocationData(
    descriptor="beach",
    adjectives=[ADJ_SANDY, ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BEACH_LAKESIDE2 = LocationData(
    descriptor="lakeside beach",
    adjectives=[ADJ_SANDY, ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BOAT2 = LocationData(
    descriptor="boat",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BOG2 = LocationData(
    descriptor="bog",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BOGGY_PATCH2 = LocationData(
    descriptor="boggy patch",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BOULDER2 = LocationData(
    descriptor="boulder",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_QUEST, ENCOUNTER_PUZZLE, ENCOUNTER_SKIRMISH])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BRAMBLE2 = LocationData(
    descriptor="bramble",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format, adjectives are a prefix added to the descriptor field
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format, nouns are a suffix added to the descriptor field
LOC_BRANCH2 = LocationData(
    descriptor="branch",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])

LOC_BRIDGE2 = LocationData(
    descriptor="bridge",
    nouns=[NOUN_NATURAL, NOUN_STONE, NOUN_WOOD, NOUN_RIVER, NOUN_CREEK, NOUN_PATH, NOUN_CANYON, NOUN_RAVINE, NOUN_FOREST, NOUN_VALLEY, NOUN_CLIFF, NOUN_WATERFALL, NOUN_GORGE],
    adjectives=[ADJ_ARCHED, ADJ_CRUMBLING, ADJ_RUINED, ADJ_DESTROYED, ADJ_MUDDY, ADJ_WOODEN, ADJ_ROCKY, ADJ_DILAPIDATED, ADJ_RUSTIC, ADJ_PRECARIOUS, ADJ_WINDING, ADJ_SMOOTH, ADJ_LICHEN_COVERED, ADJ_OLD, ADJ_MOSSY, ADJ_ABANDONED, ADJ_STURDY, ADJ_WOODED, ADJ_SHADOWY, ADJ_OVERGROWN, ADJ_PEACEFUL, ADJ_LONG, ADJ_GEOLOGICAL, ADJ_UNDULATING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD])

# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_BROOK2 = LocationData(
    descriptor="brook",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])

# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_BRUSH2 = LocationData(
    descriptor="brush",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_BUNKER2 = LocationData(
    descriptor="bunker",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_BUSH2 = LocationData(
    descriptor="bush",
    nouns=[NOUN_BERRY],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_SOCIAL, ENCOUNTER_REST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_BUSHLAND2 = LocationData(
    descriptor="bushland",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CABIN2 = LocationData(
    descriptor="cabin (fisherman's)",
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CAMP2 = LocationData(
    descriptor="camp",
    nouns=[NOUN_BANDIT],
    adjectives=[ADJ_ABANDONED, ADJ_HASTILY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CANYON2 = LocationData(
    descriptor="canyon",
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])

# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CANYON_FLOOR2 = LocationData(
    descriptor="canyon floor",
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CAVE2 = LocationData(
    descriptor="cave",
    nouns=["hermit", "hillside"],
    adjectives=[ADJ_HIDDEN, ADJ_WIDENING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_REST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CAVERN2 = LocationData(
    descriptor="cavern",
    adjectives=[ADJ_HIDDEN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CAVE_ENTRANCE2 = LocationData(
    descriptor="cave entrance",
    adjectives=[ADJ_HIDDEN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CAVE_MOUTH2 = LocationData(
    descriptor="cave mouth",
    adjectives=[ADJ_HIDDEN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CELLAR2 = LocationData(
    descriptor="cellar",
    adjectives=[ADJ_HIDDEN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CEMETERY2 = LocationData(
    descriptor="cemetery",
    adjectives=[ADJ_HUSHED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CHAMBER2 = LocationData(
    descriptor="chamber",
    adjectives=[ADJ_HUSHED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CHURCH2 = LocationData(
    descriptor="church",
    adjectives=[ADJ_HUSHED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CIRCLE2 = LocationData(
    descriptor="circle",
    nouns=["rock", "mushroom", "fairy"],
    adjectives=[ADJ_OLD],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CIRCLE_FAERIE2 = LocationData(
    descriptor="circle (faerie)",
    adjectives=[ADJ_HUSHED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CIRCLE_MUSHROOM2 = LocationData(
    descriptor="circle (mushroom)",
    adjectives=[ADJ_HUSHED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CIRCLE_STONE2 = LocationData(
    descriptor="circle (stone)",
    adjectives=[ADJ_HUSHED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CLEARING2 = LocationData(
    descriptor="clearing",
    adjectives=[ADJ_DAPPLED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_REST, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CLEARWATER2 = LocationData(
    descriptor="clearwater",
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CLIFF2 = LocationData(
    descriptor="cliff",
    adjectives=[ADJ_JAGGED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format

LOC_CLIFF_EDGE2 = LocationData(
    descriptor="cliff edge",
    adjectives=[ADJ_CRUMBLING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_COLONY_SEABIRD2 = LocationData(
    descriptor="colony (seabird)",
    adjectives=[ADJ_NOISY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_COLONY_SEAL2 = LocationData(
    descriptor="colony (seal)",
    adjectives=[ADJ_NOISY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_COMMUNITY_HALL2 = LocationData(
    descriptor="community hall",
    adjectives=[ADJ_WELCOMING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_COPSE2 = LocationData(
    descriptor="copse",
    adjectives=[ADJ_DAPPLED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_COTTAGE_PEASANT2 = LocationData(
    descriptor="cottage (peasant's)",
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_SOCIAL, ENCOUNTER_REST, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_COVE_HIDDEN2 = LocationData(
    descriptor="cove (hidden)",
    adjectives=[ADJ_SECLUDED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_CREEK_BED2 = LocationData(
    descriptor="creek bed",
    adjectives=[ADJ_DRY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_DELL2 = LocationData(
    descriptor="dell",
    adjectives=[ADJ_DAPPLED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_DEN2 = LocationData(
    descriptor="den",
    adjectives=[ADJ_HIDDEN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_DITCH2 = LocationData(
    descriptor="ditch",
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_DOCK2 = LocationData(
    descriptor="dock",
    adjectives=[ADJ_RICKETY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_DORMITORY2 = LocationData(
    descriptor="dormitory",
    adjectives=[ADJ_NOISY, ADJ_QUIET],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_ECHO_POINT2 = LocationData(
    descriptor="echo point",
    adjectives=[ADJ_SECLUDED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_FARMHOUSE2 = LocationData(
    descriptor="farmhouse",
    adjectives=[ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_OCCUPIED, ADJ_HOSTILE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_FARMLANDS2 = LocationData(
    descriptor="farmlands",
    adjectives=[ADJ_OVERGROWN, ADJ_BARREN, ADJ_FERTILE, ADJ_FLOODED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_FEN2 = LocationData(
    descriptor="fen",
    adjectives=[ADJ_DARK],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_FERNERY2 = LocationData(
    descriptor="fernery",
    adjectives=[ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_FIELD2 = LocationData(
    descriptor="field",
    nouns=["boulder", "flower", "mushroom"],
    adjectives=[ADJ_IDYLLIC],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SPOT_FISHING2 = LocationData(
    descriptor="fishing spot",
    adjectives=[ADJ_IDYLLIC, ADJ_SECLUDED, ADJ_ROUGH],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_FJORD2 = LocationData(
    descriptor="fjord",
    adjectives=[ADJ_DRY, ADJ_SANDY, ADJ_RAPID],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_FOOTHILL2 = LocationData(
    descriptor="foothill",
    adjectives=[ADJ_ROUGH, ADJ_ROCKY, ADJ_DRY, ADJ_BARREN, ADJ_FERTILE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_FORMATIONS2 = LocationData(
    descriptor="formations",
    adjectives=[ADJ_ROUGH, ADJ_ROCKY, ADJ_DRY, ADJ_BARREN, ADJ_FERTILE, ADJ_OVERGROWN, ADJ_FLOODED, ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_SECLUDED, ADJ_IDYLLIC, ADJ_RAPID, ADJ_SANDY, ADJ_OCCUPIED, ADJ_HOSTILE, ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_QUIET, ADJ_NOISY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_FUNGI_COLONY2 = LocationData(
    descriptor="fungi colony",
    adjectives=[ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_SECLUDED, ADJ_IDYLLIC, ADJ_QUIET, ADJ_NOISY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GARDEN_HERBALIST2 = LocationData(
    descriptor="herbalist's garden",
    adjectives=[ADJ_IDYLLIC, ADJ_SECLUDED, ADJ_ROUGH, ADJ_ROCKY, ADJ_DRY, ADJ_BARREN, ADJ_FERTILE, ADJ_OVERGROWN, ADJ_FLOODED, ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_RAPID, ADJ_SANDY, ADJ_OCCUPIED, ADJ_HOSTILE, ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_QUIET, ADJ_NOISY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GARDEN_HIDDEN2 = LocationData(
    descriptor="garden (hidden)",
    adjectives=[ADJ_IDYLLIC, ADJ_SECLUDED, ADJ_ROUGH, ADJ_ROCKY, ADJ_DRY, ADJ_BARREN, ADJ_FERTILE, ADJ_OVERGROWN, ADJ_FLOODED, ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_RAPID, ADJ_SANDY, ADJ_OCCUPIED, ADJ_HOSTILE, ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_QUIET, ADJ_NOISY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GATEHOUSE2 = LocationData(
    descriptor="gatehouse",
    adjectives=[ADJ_OCCUPIED, ADJ_HOSTILE, ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_QUIET, ADJ_NOISY, ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_SECLUDED, ADJ_IDYLLIC, ADJ_RAPID, ADJ_SANDY, ADJ_OVERGROWN, ADJ_FLOODED, ADJ_ROUGH, ADJ_ROCKY, ADJ_DRY, ADJ_BARREN, ADJ_FERTILE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GEODE2 = LocationData(
    descriptor="geode",
    adjectives=[ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_SECLUDED, ADJ_IDYLLIC, ADJ_QUIET, ADJ_NOISY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GLADE2 = LocationData(
    descriptor="glade",
    adjectives=[ADJ_DAPPLED, ADJ_OVERGROWN, ADJ_RESTFUL],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_REST, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GRAIN_MILL2 = LocationData(
    descriptor="grain mill",
    adjectives=[ADJ_OCCUPIED, ADJ_HOSTILE, ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_QUIET, ADJ_NOISY, ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_SECLUDED, ADJ_IDYLLIC, ADJ_RAPID, ADJ_SANDY, ADJ_OVERGROWN, ADJ_FLOODED, ADJ_ROUGH, ADJ_ROCKY, ADJ_DRY, ADJ_BARREN, ADJ_FERTILE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GRAVEYARD2 = LocationData(
    descriptor="graveyard",
    adjectives=[ADJ_OCCUPIED, ADJ_HOSTILE, ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_QUIET, ADJ_NOISY, ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_SECLUDED, ADJ_IDYLLIC, ADJ_RAPID, ADJ_SANDY, ADJ_OVERGROWN, ADJ_FLOODED, ADJ_ROUGH, ADJ_ROCKY, ADJ_DRY, ADJ_BARREN, ADJ_FERTILE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GREEN2 = LocationData(
    descriptor="green",
    adjectives=[ADJ_DAPPLED, ADJ_OVERGROWN, ADJ_RESTFUL],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GROTTO2 = LocationData(
    descriptor="grotto",
    adjectives=[ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_SECLUDED, ADJ_IDYLLIC, ADJ_QUIET, ADJ_NOISY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GROVE2 = LocationData(
    descriptor="grove",
    adjectives=[ADJ_DAPPLED, ADJ_OVERGROWN, ADJ_RESTFUL],
    encounters=[ENCOUNTER_QUEST, ENCOUNTER_SKIRMISH, ENCOUNTER_SOCIAL, ENCOUNTER_REST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GROVE_HIDDEN2 = LocationData(
    descriptor="hidden grove",
    adjectives=[ADJ_SILENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_GULLY2 = LocationData(
    descriptor="gully",
    adjectives=[ADJ_DRY, ADJ_BARREN, ADJ_FERTILE, ADJ_RAPID, ADJ_SANDY, ADJ_OVERGROWN, ADJ_FLOODED, ADJ_ROUGH, ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HALL2 = LocationData(
    descriptor="hall",
    adjectives=[ADJ_OCCUPIED, ADJ_HOSTILE, ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_QUIET, ADJ_NOISY, ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_SECLUDED, ADJ_IDYLLIC, ADJ_RAPID, ADJ_SANDY, ADJ_OVERGROWN, ADJ_FLOODED, ADJ_ROUGH, ADJ_ROCKY, ADJ_DRY, ADJ_BARREN, ADJ_FERTILE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HIDEOUT2 = LocationData(
    descriptor="hideout",
    adjectives=[ADJ_OCCUPIED, ADJ_HOSTILE, ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED, ADJ_QUIET, ADJ_NOISY, ADJ_DARK, ADJ_DAMP, ADJ_HUMID, ADJ_MUDDY, ADJ_SLIPPERY, ADJ_SECLUDED, ADJ_IDYLLIC, ADJ_RAPID, ADJ_SANDY, ADJ_OVERGROWN, ADJ_FLOODED, ADJ_ROUGH, ADJ_ROCKY, ADJ_DRY, ADJ_BARREN, ADJ_FERTILE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HILL2 = LocationData(
    descriptor="hill",
    adjectives=[ADJ_FLOWER_COVERED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HILL_CREST2 = LocationData(
    descriptor="hill crest",
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HOLLOW2 = LocationData(
    descriptor="hollow",
    adjectives=[ADJ_SILENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HOMESTEAD2 = LocationData(
    descriptor="homestead",
    nouns=[],
    adjectives=[ADJ_SILENT, ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HOUSE_MAYOR2 = LocationData(
    descriptor="mayor's house",
    nouns=[],
    adjectives=[ADJ_SILENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HUT_MARSH2 = LocationData(
    descriptor="hut (marsh)",
    nouns=[],
    adjectives=[ADJ_SILENT, ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HUT_SHEPHERDING2 = LocationData(
    descriptor="hut (shepherding)",
    nouns=[],
    adjectives=[ADJ_SILENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_HUT_WITCH2 = LocationData(
    descriptor="hut (witch's)",
    nouns=[],
    adjectives=[ADJ_SILENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_IDOL2 = LocationData(
    descriptor="idol (ancient)",
    nouns=[],
    adjectives=[ADJ_WOODEN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_INFIRMARY2 = LocationData(
    descriptor="infirmary",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_INN2 = LocationData(
    descriptor="inn",
    nouns=[],
    adjectives=[ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED],
    encounters=[ENCOUNTER_REST, ENCOUNTER_SOCIAL, ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_ISLAND2 = LocationData(
    descriptor="island",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE, ENCOUNTER_REST, ENCOUNTER_SOCIAL])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_ISLAND_DUCK2 = LocationData(
    descriptor="island (duck)",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_PUZZLE, ENCOUNTER_REST, ENCOUNTER_SOCIAL])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_ISLAND_REEDY2 = LocationData(
    descriptor="island (reedy)",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_PUZZLE, ENCOUNTER_REST, ENCOUNTER_SOCIAL])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_JETTY2 = LocationData(
    descriptor="jetty",
    nouns=[],
    adjectives=[ADJ_SLIPPERY, ADJ_OLD],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_KITCHEN2 = LocationData(
    descriptor="kitchen",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_KNOLL2 = LocationData(
    descriptor="knoll",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LAIR2 = LocationData(
    descriptor="lair",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LAKE2 = LocationData(
    descriptor="lake",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LANDING2 = LocationData(
    descriptor="landing (longboat)",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LANDSLIDE2 = LocationData(
    descriptor="landslide",
    nouns=[],
    adjectives=[ADJ_OLD, ADJ_FRESH],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LATRINE2 = LocationData(
    descriptor="latrine",
    nouns=[],
    adjectives=[ADJ_ODOUROUS],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LEDGE2 = LocationData(
    descriptor="ledge",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LIGHTS2 = LocationData(
    descriptor="lights (marsh)",
    nouns=[],
    adjectives=[ADJ_UNDULATING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LODGE_HUNTING2 = LocationData(
    descriptor="lodge (hunting)",
    nouns=[],
    adjectives=[ADJ_BURNT_OUT, ADJ_RUINED, ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LOG_FALLEN2 = LocationData(
    descriptor="log (fallen) ",
    nouns=[],
    adjectives=[ADJ_ROTTING, ADJ_FRESHLY, ADJ_LIGHTING_STRUCK, ADJ_MUSHROOM_COVERED, ADJ_LICHEN_COVERED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_LOG_FLOATING2 = LocationData(
    descriptor="log (floating)",
    nouns=[],
    adjectives=[ADJ_ROTTING, ADJ_FRESHLY, ADJ_SMELLY, ADJ_ODOUROUS, ADJ_SLIPPERY, ADJ_MUSHROOM_COVERED, ADJ_LICHEN_COVERED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MARKET2 = LocationData(
    descriptor="market",
    nouns=[],
    adjectives=[ADJ_SILENT, ADJ_FORGOTTEN, ADJ_RUSTIC, ADJ_DESERTED, ADJ_ODOUROUS],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MARKET_FISH2 = LocationData(
    descriptor="market (fish)",
    nouns=[],
    adjectives=[ADJ_SILENT, ADJ_FORGOTTEN, ADJ_RUSTIC, ADJ_DESERTED, ADJ_ODOUROUS],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MARSH2 = LocationData(
    descriptor="marsh",
    nouns=[],
    adjectives=[ADJ_ODOUROUS],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MEADOW2 = LocationData(
    descriptor="meadow",
    nouns=["wildflower"],
    adjectives=[ADJ_IDYLLIC],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_SOCIAL])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MESS_HALL2 = LocationData(
    descriptor="mess hall",
    nouns=[],
    adjectives=[ADJ_DESTROYED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MINE2 = LocationData(
    descriptor="mine",
    nouns=[],
    adjectives=[ADJ_ABANDONED, ADJ_DESERTED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MOAT2 = LocationData(
    descriptor="moat",
    nouns=[],
    adjectives=[ADJ_DRY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MOSSBED2 = LocationData(
    descriptor="mossbed",
    nouns=[],
    adjectives=[ADJ_OVERGROWN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MOUND_BARROW2 = LocationData(
    descriptor="mound (barrow)",
    nouns=[],
    adjectives=[ADJ_COLLAPSED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_MOUNTAIN2 = LocationData(
    descriptor="mountain",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_NAZE2 = LocationData(
    descriptor="naze",
    nouns=[],
    adjectives=[ADJ_PROMINENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_NEST2 = LocationData(
    descriptor="nest",
    nouns=[],
    adjectives=[ADJ_ABANDONED, ADJ_OCCUPIED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_NEST_EAGLE2 = LocationData(
    descriptor="nest (eagle's)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_OFFICE_QUARTERMASER2 = LocationData(
    descriptor="quartermaster's office",
    nouns=[],
    adjectives=[ADJ_SILENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_ORCHARD2 = LocationData(
    descriptor="orchard",
    nouns=[],
    adjectives=[ADJ_OLD],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_OUTCROP2 = LocationData(
    descriptor="outcrop",
    nouns=[],
    adjectives=[ADJ_ROCKY, ADJ_PRECARIOUS, ADJ_CRUMBLING, ADJ_OVERGROWN, ADJ_JAGGED, ADJ_SHARP, ADJ_ERODED, ADJ_RUGGED, ADJ_SCENIC, ADJ_STRIATED, ADJ_EXPOSED, ADJ_CRYSTALLINE, ADJ_ANCIENT, ADJ_VOLCANIC, ADJ_SEDIMENTARY, ADJ_GEOLOGICAL, ADJ_STONY, ADJ_FOSSILIZED, ADJ_PROMINENT, ADJ_BARE, ADJ_TOWERING, ADJ_GRANITIC, ADJ_PRECIPITOUS],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_OUTPOST_OBSERVATION2 = LocationData(
    descriptor="outpost (observation)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])

# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_OUTPOST_TRADING2 = LocationData(
    descriptor="outpost (trading)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PADDOCK2 = LocationData(
    descriptor="paddock",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PASSAGE2 = LocationData(
    descriptor="passage",
    nouns=[],
    adjectives=[ADJ_TWISTING, ADJ_NARROW, ADJ_CRUMBLING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_TRAP, ENCOUNTER_HAZARD])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PATCH2 = LocationData(
    descriptor="patch",
    nouns=[NOUN_WILDFLOWER],
    adjectives=[ADJ_OVERGROWN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PATCH_LICHEN2 = LocationData(
    descriptor="patch (lichen)",
    nouns=[],
    adjectives=[ADJ_FLOODED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PATH2 = LocationData(
    descriptor="path",
    nouns=[],
    adjectives=[ADJ_PINE_CONE_LITTERED, ADJ_LEAF_STREWN, ADJ_NARROW],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PEAK2 = LocationData(
    descriptor="peak",
    nouns=[],
    adjectives=[ADJ_BARREN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PILE_DRIFTWOOD2 = LocationData(
    descriptor="pile (driftwood)",
    nouns=[],
    adjectives=[ADJ_SLIPPERY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PILE_LEAF2 = LocationData(
    descriptor="pile (leaf)",
    nouns=[],
    adjectives=[ADJ_SLIPPERY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PILLAR2 = LocationData(
    descriptor="pillar",
    nouns=[NOUN_STONE],
    adjectives=[ADJ_ANCIENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PIT_SINKING2 = LocationData(
    descriptor="pit (sinking)",
    nouns=[],
    adjectives=[ADJ_FLOWER_COVERED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PLATEAU2 = LocationData(
    descriptor="plateau",
    nouns=[],
    adjectives=[ADJ_FLOWER_COVERED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_POND2 = LocationData(
    descriptor="pond",
    nouns=[],
    adjectives=[ADJ_STAGNANT, ADJ_FETID, ADJ_MUDDY, ADJ_FOUL, ADJ_STINKING, ADJ_FOUL_SMELLING, ADJ_QUIET],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_POOL2 = LocationData(
    descriptor="pool",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_REST, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_POOL_ALLIGATOR2 = LocationData(
    descriptor="pool (alligator)",
    nouns=[],
    adjectives=[ADJ_PEACEFUL],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_POOL_BOG2 = LocationData(
    descriptor="bog pool",
    nouns=[],
    adjectives=[ADJ_ODOUROUS],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_POOL_MARSH2 = LocationData(
    descriptor="marsh pool",
    nouns=[],
    adjectives=[ADJ_SANDY, ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_POOL_UNDERGROUND2 = LocationData(
    descriptor="undergound pool",
    nouns=[],
    adjectives=[ADJ_SANDY, ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PRAIRIE2 = LocationData(
    descriptor="prairie",
    nouns=[],
    adjectives=[ADJ_SANDY, ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_PRECIPICE2 = LocationData(
    descriptor="precipice",
    nouns=[],
    adjectives=[ADJ_SANDY, ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_QUAGMIRE2 = LocationData(
    descriptor="quagmire",
    nouns=[],
    adjectives=[ADJ_ODOUROUS],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_QUARRY2 = LocationData(
    descriptor="quarry",
    nouns=[],
    adjectives=[ADJ_SANDY, ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_QUARTERS_COMMANDER2 = LocationData(
    descriptor="commander's quarter's",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_QUARTERS_OFFICER2 = LocationData(
    descriptor="officer's quarters",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RAPIDS2 = LocationData(
    descriptor="rapids",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RAVINE2 = LocationData(
    descriptor="ravine",
    nouns=[],
    adjectives=[ADJ_SLIPPERY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RIDGE2 = LocationData(
    descriptor="ridge",
    nouns=[],
    adjectives=[ADJ_PRECARIOUS],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RING_FAIRY2 = LocationData(
    descriptor="ring (fairy)",
    nouns=[],
    adjectives=[ADJ_SILENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RIVER2 = LocationData(
    descriptor="river",
    nouns=[],
    adjectives=[ADJ_RAPID],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RIVERBED2 = LocationData(
    descriptor="riverbed",
    nouns=[],
    adjectives=[ADJ_ROCKY, ADJ_MUDDY, ADJ_SANDY, ADJ_DRY, ADJ_FLOODED, ADJ_DAMP, ADJ_OVERGROWN, ADJ_SUN_BAKED, ADJ_LUSH, ADJ_BARREN, ADJ_WINDING, ADJ_DEEP, ADJ_SHALLOW, ADJ_RUGGED, ADJ_SLIPPERY, ADJ_SMOOTH, ADJ_PEBBLY, ADJ_SHADOWY, ADJ_MEANDERING, ADJ_SERENE],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RIVER_BANK2 = LocationData(
    descriptor="river bank",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RIVER_BEND2 = LocationData(
    descriptor="river bend",
    nouns=[],
    adjectives=[ADJ_MEANDERING, ADJ_SERENE, ADJ_PICTURESQUE, ADJ_TWISTING, ADJ_FLOWING, ADJ_TRANQUIL, ADJ_LUSH, ADJ_WINDING, ADJ_SWEEPING, ADJ_MURMURING, ADJ_VERDANT, ADJ_PEACEFUL, ADJ_SHIMMERING, ADJ_GLISTENING, ADJ_INVITING, ADJ_SCENIC, ADJ_UNDULATING, ADJ_QUIET, ADJ_RUSTIC, ADJ_IDYLLIC],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE, ENCOUNTER_HAZARD])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RIVER_UNDERGROUND2 = LocationData(
    descriptor="river (underground)",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_ROOM_STORAGE2 = LocationData(
    descriptor="room (storage)",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_ROOST2 = LocationData(
    descriptor="roost",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_ROOT2 = LocationData(
    descriptor="root",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RUINS2 = LocationData(
    descriptor="ruins",
    nouns=[],
    adjectives=[ADJ_TUMBLEDOWN, ADJ_BURNT_OUT, ADJ_CRUMBLING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_RUINS_HILL_FORT2 = LocationData(
    descriptor="ruins (hill fort)",
    nouns=[],
    adjectives=[ADJ_ABANDONED, ADJ_RUINED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SCHOOLHOUSE2 = LocationData(
    descriptor="schoolhouse",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SCRUB2 = LocationData(
    descriptor="scrub",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SEA_VIEW2 = LocationData(
    descriptor="sea view",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SEWER2 = LocationData(
    descriptor="sewer",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SHALLOWS2 = LocationData(
    descriptor="shallows",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SHELF2 = LocationData(
    descriptor="shelf",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SHOP_COBBLER2 = LocationData(
    descriptor="shop (cobbler's)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SHORE_REEDY2 = LocationData(
    descriptor="shore (reedy)",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SLOPE2 = LocationData(
    descriptor="slope",
    nouns=[],
    adjectives=[ADJ_ROCKY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SLOPE_SCREE2 = LocationData(
    descriptor="slope (scree)",
    nouns=[],
    adjectives=[ADJ_FRESH],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_HAZARD])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SPRING2 = LocationData(
    descriptor="spring",
    nouns=[],
    adjectives=[ADJ_OLD],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SPRING_HOT2 = LocationData(
    descriptor="spring (hot)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SPRING_MOUNTAIN2 = LocationData(
    descriptor="spring (mountain)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SPRING_UNDERGROUND2 = LocationData(
    descriptor="spring (underground)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SQUARE2 = LocationData(
    descriptor="square",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_STABLE2 = LocationData(
    descriptor="stable",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_STAGS_LEAP2 = LocationData(
    descriptor="stag's leap",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_HAZARD, ENCOUNTER_SKIRMISH, ENCOUNTER_SOCIAL])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_STALACTITES2 = LocationData(
    descriptor="stalactites",
    nouns=[],
    adjectives=[ADJ_DRIPPING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_HAZARD, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_STALAGMITES2 = LocationData(
    descriptor="stalagmites",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_STAND2 = LocationData(
    descriptor="stand",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_STOCKAdE2 = LocationData(
    descriptor="stockade",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_STORE_GENERAL2 = LocationData(
    descriptor="general store",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_STREAM2 = LocationData(
    descriptor="stream",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_STREAM_UNDERGROUND2 = LocationData(
    descriptor="stream (underground)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SWAMP2 = LocationData(
    descriptor="swamp",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TAVERN2 = LocationData(
    descriptor="tavern",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_THICKET2 = LocationData(
    descriptor="thicket",
    nouns=[],
    adjectives=[ADJ_BUSHY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TIMBERLAND2 = LocationData(
    descriptor="timberland",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TOWER2 = LocationData(
    descriptor="tower",
    nouns=["guard"],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TRAIL2 = LocationData(
    descriptor="trail",
    nouns=["animal", "cart", "woodland"],
    adjectives=[ADJ_DUSTY, ADJ_OVERGROWN, ADJ_MUDDY, ADJ_ROUGH, ADJ_RUGGED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TRAINING_GROUND2 = LocationData(
    descriptor="training ground",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TREE2 = LocationData(
    descriptor="tree",
    nouns=["archway", "lone", "stump"],
    adjectives=[ADJ_ANCIENT, ADJ_FALLEN, ADJ_HOLLOW, ADJ_LONE, ADJ_STANDING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_REST, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TREE_LINE2 = LocationData(
    descriptor="tree-line",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TREE_TUNNEL2 = LocationData(
    descriptor="tunnel (tree)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TREE_WILLOW2 = LocationData(
    descriptor="  (willow)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TRENCH2 = LocationData(
    descriptor="trench",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TRUNK2 = LocationData(
    descriptor="trunk",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_TUNNEL2 = LocationData(
    descriptor="tunnel",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_UNDERBRUSH2 = LocationData(
    descriptor="underbrush",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_UNDERGROWTH2 = LocationData(
    descriptor="undergrowth",
    nouns=[],
    adjectives=[ADJ_BUSHY],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_UNDERSTORY2 = LocationData(
    descriptor="understory",
    nouns=[],
    adjectives=[ADJ_OVERGROWN],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_VALLEY2 = LocationData(
    descriptor="valley",
    nouns=[],
    adjectives=[ADJ_DEEP],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_VALE = LocationData(
    descriptor="vale",
    nouns=[],
    adjectives=[ADJ_SILENT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_VILLAGE2 = LocationData(
    descriptor="village (fishing)",
    nouns=[],
    adjectives=[ADJ_ABANDONED, ADJ_POPULATED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_VINE2 = LocationData(
    descriptor="vine",
    nouns="tangle",
    adjectives=[ADJ_CREEPING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WAGON_RUTS2 = LocationData(
    descriptor="wagon ruts",
    nouns=[],
    adjectives=[ADJ_DEEP, ADJ_WEATHERED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WALL2 = LocationData(
    descriptor="wall",
    nouns=[],
    adjectives=[ADJ_GLISTENING, ADJ_FOSSIL],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WATCHPOST2 = LocationData(
    descriptor="watch post",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WATCHTOWER2 = LocationData(
    descriptor="watchtower",
    nouns=[],
    adjectives=[ADJ_ABANDONED, ADJ_OLD, ADJ_RUINED, ADJ_HOSTILE, ADJ_BURNT_OUT],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_REST])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WATERFALL2 = LocationData(
    descriptor="waterfall",
    nouns=[],
    adjectives=[ADJ_IDYLLIC, ADJ_WHISPERING],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WATER_WELL2 = LocationData(
    descriptor="water well",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_SPOT_WILL_O_WISP2 = LocationData(
    descriptor="will-o'-the-wisp spot",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WORKSHOP_ARTISAN2 = LocationData(
    descriptor="workshop (artisan's)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WORKSHOP_BLACKSMITH2 = LocationData(
    descriptor="workshop (blacksmith's)",
    nouns=[],
    adjectives=[ADJ_ABANDONED],
    encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WORKSHOP_CARPENTER2 = LocationData("workshop (carpenter's)", nouns=[], adjectives=[ADJ_ABANDONED], encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])
# TODO suggest 20 adjectives for the adjectives field for the following location, using the ADJ_adjective format
# TODO suggest 10 nouns for the nouns field for the following location, using the NOUN_noun format
LOC_WORKSHOP_WEAVER2 = LocationData("workshop (weaver's)", nouns=[], adjectives=[ADJ_ABANDONED], encounters=[ENCOUNTER_SKIRMISH, ENCOUNTER_QUEST, ENCOUNTER_SOCIAL, ENCOUNTER_PUZZLE])

LOCATIONS_DB = [
    LOC_ALCOVE2,
    LOC_ANIMAL_BURROW2,
    LOC_ANIMAL_PENS2,
    LOC_APOTHECARY2,
    LOC_ARMORY2,
    LOC_MARSH2,
    LOC_CANYON2,
    LOC_CANYON_FLOOR2,
    LOC_CAVE2,
    LOC_ISLAND2,
    LOC_ISLAND_DUCK2,
    LOC_AVALANCHE_SITE2,
    LOC_POOL_MARSH2,
    LOC_JETTY2,
    LOC_BAKERY2,
    LOC_BARN2,
    LOC_BARNYARD2,
    LOC_BARRACKS2,
    LOC_BOAT2,
    LOC_WALL2,
    LOC_WATERFALL2,
    LOC_WATCHPOST2,
    LOC_UNDERBRUSH2,
    LOC_UNDERGROWTH2,
    LOC_TRENCH2,
    LOC_TREE2,
    LOC_TRUNK2,
    LOC_THICKET2,
    LOC_TOWER2,
    LOC_VINE2,
    LOC_FJORD2,
    LOC_CAVE_ENTRANCE2,
    LOC_CAVE_MOUTH2,
    LOC_WORKSHOP_ARTISAN2,
    LOC_WORKSHOP_BLACKSMITH2,
    LOC_WORKSHOP_CARPENTER2,
    LOC_WORKSHOP_WEAVER2,
    LOC_SPRING2,
    LOC_TREE_TUNNEL2,
    LOC_RIVER2,
    LOC_RAPIDS2,
    LOC_BRIDGE2,
    LOC_RIVER_BANK2,
    LOC_RIVER_BEND2,
    LOC_MOUNTAIN2,
    LOC_MOUNTAIN_PASS2,
    LOC_SPRING_MOUNTAIN2,
    LOC_LAKE2,
    LOC_MEADOW2,
    LOC_HILL2,
    LOC_SWAMP2,
    LOC_CAVERN2,
    LOC_PATCH2,
    LOC_POOL2,
    LOC_BOG2,
    LOC_BOGGY_PATCH2,
    LOC_POOL_BOG2,
    LOC_OUTPOST_OBSERVATION2,
    LOC_OUTPOST_TRADING2,
    LOC_HILL_CREST2,
    LOC_POOL_UNDERGROUND2,
]
