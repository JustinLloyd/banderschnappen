from location_data import *
from zone_types import ZoneData

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_WOODLAND2 = ZoneData(name="woodland", minimum_locations_to_use=4, maximum_locations_to_use=8, locations=[LOC_WATCHPOST2, LOC_WATERFALL2, LOC_UNDERGROWTH2, LOC_UNDERBRUSH2, LOC_TRENCH2, LOC_TREE2, LOC_VINE2, LOC_TRUNK2, LOC_THICKET2, LOC_TOWER2, LOC_SPRING2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_FOREST2 = ZoneData(name="forest", minimum_locations_to_use=2, maximum_locations_to_use=3, locations=[LOC_WATERFALL2, LOC_TREE2, LOC_TREE_TUNNEL2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_RIVER2 = ZoneData(name="river", minimum_locations_to_use=4, maximum_locations_to_use=6, locations=[LOC_RIVER2, LOC_BRIDGE2, LOC_RIVER_BANK2, LOC_RIVER_BEND2, LOC_FJORD2, LOC_RAPIDS2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_MOUNTAIN2 = ZoneData(name="mountain", minimum_locations_to_use=2, maximum_locations_to_use=3, locations=[LOC_MOUNTAIN2, LOC_SPRING_MOUNTAIN2, LOC_MOUNTAIN_PASS2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_LAKE2 = ZoneData(name="lake", minimum_locations_to_use=2, maximum_locations_to_use=2, locations=[LOC_LAKE2, LOC_JETTY2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_MARSH2 = ZoneData(name="marsh", minimum_locations_to_use=2, maximum_locations_to_use=4, locations=[LOC_MARSH2, LOC_POOL_MARSH2, LOC_ISLAND2, LOC_ISLAND_DUCK2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_CANYON2 = ZoneData(name="canyon", minimum_locations_to_use=2, maximum_locations_to_use=2, locations=[LOC_CANYON2, LOC_CANYON_FLOOR2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_CAVE2 = ZoneData(name="cave", minimum_locations_to_use=2, maximum_locations_to_use=4, locations=[LOC_CAVE2, LOC_CAVE_ENTRANCE2, LOC_CAVE_MOUTH2, LOC_POOL_UNDERGROUND2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_HILL2 = ZoneData(name="hill", minimum_locations_to_use=2, maximum_locations_to_use=2, locations=[LOC_HILL2, LOC_HILL_CREST2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_MEADOW2 = ZoneData(name="meadow", minimum_locations_to_use=1, maximum_locations_to_use=1, locations=[LOC_MEADOW2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_CAVERN2 = ZoneData(name="cavern", minimum_locations_to_use=1, maximum_locations_to_use=1, locations=[LOC_CAVERN2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_SWAMP2 = ZoneData(name="swamp", minimum_locations_to_use=2, maximum_locations_to_use=5, locations=[LOC_SWAMP2, LOC_BOAT2, LOC_PATCH2, LOC_BRIDGE2, LOC_POOL2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_BOG2 = ZoneData(name="bog", minimum_locations_to_use=2, maximum_locations_to_use=3, locations=[LOC_BOG2, LOC_BOGGY_PATCH2, LOC_POOL_BOG2, LOC_BOAT2, LOC_TREE2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_OUTPOST2 = ZoneData(name="outpost", adjectives=[ADJ_ABANDONED,ADJ_POPULATED], minimum_locations_to_use=1, maximum_locations_to_use=1, locations=[LOC_OUTPOST_OBSERVATION2, LOC_OUTPOST_TRADING2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_WATCHTOWER2 = ZoneData(name="watchtower", adjectives=[ADJ_ABANDONED,ADJ_POPULATED], minimum_locations_to_use=2, maximum_locations_to_use=4, locations=[LOC_WATCHTOWER2, LOC_TRENCH2, LOC_MOAT2, LOC_WATCHPOST2, LOC_GATEHOUSE2, LOC_ALCOVE2, LOC_ARMORY2, LOC_MESS_HALL2, LOC_BRIDGE2])

# TODO add in more locations to the locations field that would be relevant to the zone type
ZONE_VILLAGE2 = ZoneData(name="village", adjectives=[ADJ_ABANDONED,ADJ_POPULATED], minimum_locations_to_use=3, maximum_locations_to_use=5, locations=[LOC_BRIDGE2, LOC_BAKERY2, LOC_MARKET2, LOC_MARKET_FISH2, LOC_WORKSHOP_BLACKSMITH2, LOC_WORKSHOP_CARPENTER2, LOC_WORKSHOP_WEAVER2])

ZONE_DB = [
    ZONE_WOODLAND2,
    ZONE_FOREST2,
    ZONE_RIVER2,
    ZONE_MOUNTAIN2,
    ZONE_LAKE2,
    ZONE_MARSH2,
    ZONE_CANYON2,
    ZONE_CAVE2,
    ZONE_HILL2,
    ZONE_MEADOW2,
    ZONE_CAVERN2,
    ZONE_SWAMP2,
    ZONE_BOG2,
    ZONE_OUTPOST2,
]
