from item_types import ItemData

ABILITY_STRENGTH_KEY = "strength"
ABILITY_DEXTERITY_KEY = "dexterity"
ABILITY_CONSTITUTION_KEY = "constitution"
ABILITY_INTELLIGENCE_KEY = "intelligence"
ABILITY_WISDOM_KEY = "wisdom"
ABILITY_CHARISMA_KEY = "charisma"

ABILITIES_DB = [
    ABILITY_STRENGTH_KEY,
    ABILITY_DEXTERITY_KEY,
    ABILITY_CONSTITUTION_KEY,
    ABILITY_INTELLIGENCE_KEY,
    ABILITY_WISDOM_KEY,
    ABILITY_CHARISMA_KEY
]

RACE_HUMAN_KEY = "human"
RACE_ORC_KEY = "orc"
RACE_GOBLIN_KEY = "goblin"
RACE_HOBGOBLIN_KEY = "hobgoblin"
RACE_HALFLING_KEY = "halfling"
RACE_ELF_KEY = "elf"
RACE_DWARF_KEY = "dwarf"
RACE_HALF_ELF_KEY = "half-elf"
RACE_HALF_ORC_KEY = "half-orc"
RACE_TIEFLING_KEY = "tiefling"
RACE_DRAGONBORN_KEY = "dragonborn"
RACE_GNOME_KEY = "gnome"

PLAYABLE_RACES_DB = [
    RACE_HUMAN_KEY,
    RACE_HALFLING_KEY,
    RACE_ELF_KEY,
    RACE_DWARF_KEY,
    RACE_HALF_ELF_KEY,
    RACE_HALF_ORC_KEY,
    RACE_TIEFLING_KEY,
    RACE_DRAGONBORN_KEY,
    RACE_GNOME_KEY
]

CLASS_BARBARIAN_KEY = "barbarian"
CLASS_BARD_KEY = "bard"
CLASS_CLERIC_KEY = "cleric"
CLASS_DRUID_KEY = "druid"
CLASS_FIGHTER_KEY = "fighter"
CLASS_MONK_KEY = "monk"
CLASS_PALADIN_KEY = "paladin"
CLASS_RANGER_KEY = "ranger"
CLASS_ROGUE_KEY = "rogue"
CLASS_SORCERER_KEY = "sorcerer"
CLASS_WARLOCK_KEY = "warlock"
CLASS_WIZARD_KEY = "wizard"

PLAYABLE_CLASSES_DB = [
    CLASS_BARBARIAN_KEY,
    CLASS_BARD_KEY,
    CLASS_CLERIC_KEY,
    CLASS_DRUID_KEY,
    CLASS_FIGHTER_KEY,
    CLASS_MONK_KEY,
    CLASS_PALADIN_KEY,
    CLASS_RANGER_KEY,
    CLASS_ROGUE_KEY,
    CLASS_SORCERER_KEY,
    CLASS_WARLOCK_KEY,
    CLASS_WIZARD_KEY
]

# A simple mapping of classes to their primary and secondary abilities.
CLASS_ABILITIES = {
    CLASS_BARBARIAN_KEY: [ABILITY_STRENGTH_KEY, ABILITY_CONSTITUTION_KEY],
    CLASS_BARD_KEY: [ABILITY_CHARISMA_KEY, ABILITY_DEXTERITY_KEY],
    CLASS_CLERIC_KEY: [ABILITY_WISDOM_KEY, ABILITY_CONSTITUTION_KEY],
    CLASS_DRUID_KEY: [ABILITY_WISDOM_KEY, ABILITY_CONSTITUTION_KEY],
    CLASS_FIGHTER_KEY: [ABILITY_STRENGTH_KEY, ABILITY_CONSTITUTION_KEY],
    CLASS_MONK_KEY: [ABILITY_DEXTERITY_KEY, ABILITY_WISDOM_KEY],
    CLASS_PALADIN_KEY: [ABILITY_STRENGTH_KEY, ABILITY_CHARISMA_KEY],
    CLASS_RANGER_KEY: [ABILITY_DEXTERITY_KEY, ABILITY_WISDOM_KEY],
    CLASS_ROGUE_KEY: [ABILITY_DEXTERITY_KEY, ABILITY_INTELLIGENCE_KEY],
    CLASS_SORCERER_KEY: [ABILITY_CHARISMA_KEY, ABILITY_CONSTITUTION_KEY],
    CLASS_WARLOCK_KEY: [ABILITY_CHARISMA_KEY, ABILITY_CONSTITUTION_KEY],
    CLASS_WIZARD_KEY: [ABILITY_INTELLIGENCE_KEY, ABILITY_CONSTITUTION_KEY]
}

RACE_ABILITY_BONUSES_DB = {
    RACE_DWARF_KEY: {ABILITY_CONSTITUTION_KEY: 2},
    RACE_ELF_KEY: {ABILITY_DEXTERITY_KEY: 2},
    RACE_HALFLING_KEY: {ABILITY_DEXTERITY_KEY: 2},
    RACE_HUMAN_KEY: {ABILITY_STRENGTH_KEY: 1, ABILITY_DEXTERITY_KEY: 1, ABILITY_CONSTITUTION_KEY: 1, ABILITY_INTELLIGENCE_KEY: 1, ABILITY_WISDOM_KEY: 1, ABILITY_CHARISMA_KEY: 1},
    RACE_DRAGONBORN_KEY: {ABILITY_STRENGTH_KEY: 2, ABILITY_CHARISMA_KEY: 1},
    RACE_GNOME_KEY: {ABILITY_INTELLIGENCE_KEY: 2},
    RACE_HALF_ELF_KEY: {ABILITY_STRENGTH_KEY: 1, ABILITY_DEXTERITY_KEY: 1, ABILITY_CONSTITUTION_KEY: 1, ABILITY_INTELLIGENCE_KEY: 1, ABILITY_WISDOM_KEY: 1, ABILITY_CHARISMA_KEY: 2},
    RACE_HALF_ORC_KEY: {ABILITY_STRENGTH_KEY: 2, ABILITY_CONSTITUTION_KEY: 1},
    RACE_TIEFLING_KEY: {ABILITY_INTELLIGENCE_KEY: 1, ABILITY_CHARISMA_KEY: 2},
}
HIT_DICE_BY_CLASS_DB = {
    CLASS_BARBARIAN_KEY: 12,
    CLASS_BARD_KEY: 8,
    CLASS_CLERIC_KEY: 8,
    CLASS_DRUID_KEY: 8,
    CLASS_FIGHTER_KEY: 10,
    CLASS_MONK_KEY: 8,
    CLASS_PALADIN_KEY: 10,
    CLASS_RANGER_KEY: 10,
    CLASS_ROGUE_KEY: 8,
    CLASS_SORCERER_KEY: 6,
    CLASS_WARLOCK_KEY: 8,
    CLASS_WIZARD_KEY: 6
}

XP_LEVEL_THRESHOLDS = [
    0,  # Level 1
    300,  # Level 2
    900,  # Level 3
    2700,  # Level 4
    6500,  # Level 5
    14000,  # Level 6
    23000,  # Level 7
    34000,  # Level 8
    48000,  # Level 9
    64000,  # Level 10
    85000,  # Level 11
    100000,  # Level 12
    120000,  # Level 13
    140000,  # Level 14
    165000,  # Level 15
    195000,  # Level 16
    225000,  # Level 17
    265000,  # Level 18
    305000,  # Level 19
    355000  # Level 20
]

STARTER_PACKAGES_DB = {
    CLASS_BARBARIAN_KEY: ['GreatAxe', 'Two Handaxes', 'Explorer\'s Pack', 'Four Javelins'],
    CLASS_BARD_KEY: ['Rapier', 'Diplomat\'s Pack', 'Lute', 'Leather Armor', 'Dagger'],
    CLASS_CLERIC_KEY: ['Mace', 'Scale Mail', 'Light Crossbow and 20 Bolts', 'Priest\'s Pack', 'Shield', 'Holy Symbol'],
    CLASS_DRUID_KEY: ['Wooden Staff', 'Leather Armor', 'Explorer\'s Pack', 'Druidic Focus'],
    CLASS_FIGHTER_KEY: ['Longsword', 'Chain Mail', 'Light Crossbow and 20 Bolts', 'Dungeoneer\'s Pack', 'Shield', 'Two Handaxes'],
    CLASS_MONK_KEY: ['Shortsword', 'Dungeoneer\'s Pack', '10 Darts'],
    CLASS_PALADIN_KEY: ['Longsword', 'Chain Mail', 'Shield', 'Holy Symbol', 'Priest\'s Pack', '5 Javelins'],
    CLASS_RANGER_KEY: ['Longsword', 'Leather Armor', 'Longbow and 20 Arrows', 'Explorer\'s Pack'],
    CLASS_ROGUE_KEY: ['Rapier', 'Shortbow and 20 Arrows', 'Burglar\'s Pack', 'Leather Armor', 'Two Daggers'],
    CLASS_SORCERER_KEY: ['Quarterstaff', 'Component Pouch', 'Scholar\'s Pack', 'Two Daggers'],
    CLASS_WARLOCK_KEY: ['Quarterstaff', 'Leather Armor', 'Scholar\'s Pack', 'Dagger', 'Component Pouch'],
    CLASS_WIZARD_KEY: ['Quarterstaff', 'Component Pouch', 'Scholar\'s Pack', 'Spellbook', 'Dagger'],
}




ITEMS_DB = [
    ItemData('Abacus', 200, 2, 'Adventuring gear', "A standard tool used to make calculations.", ['Utility'], 1),
    ItemData('Acid (vial)', 2500, 1, 'Adventuring gear', "A vial of acid can be thrown at a creature or object up to 20 feet away. As an action, you can splash the contents of this vial onto a creature within 5 feet of you or throw the vial up to 20 feet, shattering it on impact, treating the acid as an improvised weapon. On a hit, the target takes 2d6 acid damage.", ['Combat', 'Consumable', 'Damage', 'Utility'], 1),
    ItemData('Alchemist\'s Fire (flask)', 5000, 1, 'Adventuring gear', "This sticky, adhesive fluid ignites when exposed to air. As an action, you can throw this flask up to 20 feet, shattering it on impact. Make a ranged attack against a creature or object, treating the alchemist\'s fire as an improvised weapon. On a hit, the target takes 1d4 fire damage at the start of each of its turns. A creature can end this damage by using its action to make a DC 10 Dexterity check to extinguish the flames.", ['Combat', 'Consumable', 'Damage', 'Utility'], 1),
    ItemData('Amulet', 500, 1, 'Holy Symbol', "A trinket worn around the neck.  holy symbol is a representation of a god or pantheon. A cleric or paladin can use a holy symbol as a spell casting focus. To use the symbol in this way, the caster must hold it in hand, wear it visibly, or bear it on a shield.", ['Trinket', 'Utility'], 1),
    ItemData('Alms box', 200, 1, 'Adventuring gear', "A small box for holding a substantial amount of coins. Usually found in a priest's or cleric's pack.", ['Utility'], 1),
    ItemData('Antitoxin (vial)', 5000, 0, 'Adventuring gear', "A creature that drinks this vial of liquid gains advantage on saving throws against poison for 1 hour. It confers no benefit to undead or constructs.", ['Consumable', 'Healing', 'Utility'], 1),
    ItemData('Arcane focus', 500, 1, 'Arcane focus', "A crystal or glass cone, rod, or wand. An arcane focus is a special item designed to channel the power of arcane spells. A sorcerer, warlock, or wizard can use such an item as a spell casting focus.", ['Utility'], 1),
    ItemData('Arrow', 100, 1, 'Ammunition', "Arrows are used with a weapon that has the ammunition property to make a ranged attack. Each time you attack with the weapon, you expend one piece of ammunition. Drawing the ammunition from a quiver, case, or other container is part of the attack (you need a free hand to load a one-handed weapon). At the end of the battle, you can recover half your expended ammunition by taking a minute to search the battlefield.", ['Ammunition', 'Combat'], 1),
    ItemData("Assassin's Blood", 15000, 0,
         'Poison', "A creature subjected to this poison must make a DC 10 Constitution saving throw. On a failed save, it takes 6 (1d12) poison damage and is poisoned for 24 hours. On a successful save, the creature takes half damage and isn't poisoned. Ingested. A creature must swallow an entire dose of ingested poison to suffer its effects. The dose can be delivered in food or a liquid. You may decide that a partial dose has a reduced effect, such as allowing advantage on the saving throw or dealing only half damage on a failed save.", ['Consumable', 'Damage', 'Poison'], 1),
    ItemData('Backpack', 200, 5, 'Adventuring gear', "A backpack can hold one cubic foot or 30 pounds of gear. You can also strap items, such as a bedroll or a coil of rope, to the outside of a backpack.", ['Container'], 1),
    ItemData('Bagpipes', 3000, 6, 'Musical instrument', "A musical instrument consisting of a leather bag and pipes. A bagpipe requires two hands to play. If you have proficiency with this instrument, you can add your proficiency bonus to any ability checks to play music with the instrument. A bard can use bagpipes as a spell casting focus.", ['Musical instrument'], 1),
    ItemData('Blowgun needle', 100, 0, 'Ammunition', "A blowgun needle is used as ammunition for a blowgun or similar ranged weapon.", ['Ammunition', 'Combat'], 1),
    ItemData('Battleaxe', 1000, 4, 'Weapon', "A battleaxe is a weapon with a long handle and a heavy head, used for slashing and chopping.", ['Weapon', 'Martial', 'Combat', 'Damage'], 1),
    ItemData('Bedroll', 100, 7, 'Adventuring gear', "A bedroll consists of bedding and a blanket thin enough to be rolled up and tied. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Bell', 100, 0, 'Adventuring gear', "A small bell without a clapper. Usually found in a priest's or cleric's pack.", ['Utility'], 1),
    ItemData('Blanket', 50, 3, 'Adventuring gear', "A blanket is a large piece of woven cloth, used as a covering for warmth. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Block and tackle', 100, 5, 'Adventuring gear', "A block and tackle is a set of pulleys with a rope threaded through them, usually used to lift or pull heavy loads. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Blowgun', 1000, 1, 'Weapon', "A blowgun is a simple tube for firing light projectiles, or darts. It is a one-handed ranged weapon.", ['Weapon', 'Martial', 'Combat', 'Damage'], 1),
    ItemData('Book', 2500, 5, 'Adventuring gear', "A book is a stack of paper or parchment, bound together along one edge. Usually found in a scholar's pack.", ['Utility'], 1),
    ItemData('Bottle, glass', 200, 2, 'Adventuring gear', "A glass bottle with a cork stopper. Usually found in an alchemist's pack.", ['Utility'], 1),
    ItemData('Bucket', 50, 2, 'Adventuring gear', "A bucket is a cylindrical container with a handle. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Caltrops', 100, 2, 'Adventuring gear', "A caltrop is a four-pronged metal spike crafted so that one prong faces up no matter how the caltrop comes to rest. When you scatter a handful of caltrops on the ground, they make a difficult terrain for creatures smaller than 1 inch in diameter. The caltrops remain where they are until removed. Any creature that enters the area must succeed on a DC 15 Dexterity saving throw or stop moving this turn and take 1 piercing damage. Taking this damage reduces the creature's walking speed by 10 feet until the creature regains at least 1 hit point. A creature moving through the area at half speed doesn't need to make the save.", ['Utility'], 1),
    ItemData('Candle', 10, 0, 'Adventuring gear', "A candle is a stick of wax with a string (the wick) running down the middle. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Case, crossbow bolt', 100, 1, 'Adventuring gear', "A case for holding crossbow bolts. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Case, map or scroll', 100, 1, 'Adventuring gear', "A cylindrical leather case for holding maps and scrolls. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Chain (10 feet)', 500, 10, 'Adventuring gear', "A chain is a series of connected metal links. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Chalk (1 piece)', 1, 0, 'Adventuring gear', "Chalk is a soft, white, porous sedimentary carbonate rock, a form of limestone composed of the mineral calcite. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Chest', 500, 25, 'Adventuring gear', "A chest is a large, heavy, box with a hinged lid used for storage. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Climber\'s kit', 2500, 12, 'Adventuring gear', "A climber's kit includes special pitons, boot tips, gloves, and a harness. You can use the climber's kit as an action to anchor yourself; when you do, you can't fall more than 25 feet from the point where you anchored yourself, and you can't climb more than 25 feet away from that point without undoing the anchor.", ['Utility'], 1),
    ItemData('Clothes, common', 50, 3, 'Adventuring gear', "Common clothes include a shirt, pants, undergarments, and a belt. Usually found in a dungeoneer's pack.", ['Utility'], 1),
    ItemData('Clothes, costume', 500, 4, 'Adventuring gear', "Costume clothes include fancy, ornate clothes, suitable for masquerades and parties. Usually found in a dungeoneer's pack.", ['Utility'], 1),
    ItemData('Clothes, fine', 1500, 6, 'Adventuring gear', "Fine clothes include a set of high-quality, well-made clothes. Usually found in a dungeoneer's pack.", ['Utility'], 1),
    ItemData('Clothes, traveler\'s', 200, 4, 'Adventuring gear', "Traveler's clothes include a shirt, pants, undergarments, and a belt. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Component pouch', 2500, 2, 'Adventuring gear', "A component pouch is a small, watertight leather belt pouch that has compartments to hold all the material components and other special items you need to cast your spells, except for those components that have a specific cost (as indicated in a spell's description).", ['Utility'], 1),
    ItemData('Crowbar', 200, 5, 'Adventuring gear', "A crowbar is a small, straight metal bar, often with a flattened end. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Druidic focus', 1000, 1, 'Adventuring gear', "A druidic focus might be a sprig of mistletoe or holly, a wand or scepter made of yew or another special wood, a staff drawn whole out of a living tree, or a totem object incorporating feathers, fur, bones, and teeth from sacred animals. A druid can use such an object as a spellcasting focus.", ['Utility'], 1),
    ItemData('Fishing tackle', 100, 4, 'Adventuring gear', "Fishing tackle includes a wooden rod, silken line, corkwood bobbers, steel hooks, lead sinkers, velvet lures, and narrow netting. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Flask or tankard', 20, 1, 'Adventuring gear', "A flask or tankard is a small container for holding liquid. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Grappling hook', 200, 4, 'Adventuring gear', "A grappling hook is a metal hook attached to a rope, designed to be thrown and snagged on a target. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Hammer', 100, 3, 'Adventuring gear', "A hammer is a tool with a heavy metal head mounted at right angles at the end of a handle, used for jobs such as breaking things and driving in nails. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Hammer, sledge', 200, 10, 'Adventuring gear', "A sledge hammer is a large hammer with a two-handed grip. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Healer\'s kit', 500, 3, 'Adventuring gear', "A healer's kit is a leather pouch containing bandages, salves, and splints. The kit has ten uses. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check.", ['Utility'], 1),
    ItemData('Holy symbol', 500, 1, 'Adventuring gear', "A holy symbol is a representation of a god or pantheon. A cleric or paladin can use a holy symbol as a spellcasting focus.", ['Utility'], 1),
    ItemData('Holy water (flask)', 2500, 1, 'Adventuring gear', "Holy water is water that has been blessed by a cleric or paladin. It has 3 uses. As an action, you can splash the contents of this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. In either case, make a ranged attack against a target creature, treating the holy water as an improvised weapon. If the target is a fiend or undead, it takes 2d6 radiant damage. A cleric or paladin may create holy water by performing a special ritual. The ritual takes 1 hour to perform, uses 25 gp worth of powdered silver, and requires the caster to expend a 1st-level spell slot.", ['Utility'], 1),
    ItemData('Hourglass', 2500, 1, 'Adventuring gear', "An hourglass is a device used to measure the passage of time. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Hunting trap', 500, 25, 'Adventuring gear', "A hunting trap is a metal device that snaps shut when a creature steps on a pressure plate in the center. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Ink (1 ounce bottle)', 1000, 0, 'Adventuring gear', "Ink is a liquid used for writing, drawing, and printing. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Ink pen', 20, 0, 'Adventuring gear', "An ink pen is a small tool used to write or draw with ink. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Jug or pitcher', 20, 4, 'Adventuring gear', "A jug or pitcher is a container for holding liquid. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Ladder (10-foot)', 10, 25, 'Adventuring gear', "A ladder is a set of steps or rungs that are used to climb up or down. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Lamp', 50, 1, 'Adventuring gear', "A lamp casts bright light in a 15-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Lantern, bullseye', 1000, 2, 'Adventuring gear', "A bullseye lantern casts bright light in a 60-foot cone and dim light for an additional 60 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Lantern, hooded', 500, 2, 'Adventuring gear', "A hooded lantern casts bright light in a 30-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Lock', 1000, 1, 'Adventuring gear', "A lock is a mechanical device that is used to restrict access to something. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Magnifying glass', 10000, 0, 'Adventuring gear', "A magnifying glass is a convex lens that is used to produce a magnified image of an object. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Manacles', 200, 6, 'Adventuring gear', "Manacles are metal restraints that can bind a Small or Medium creature. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Mess kit', 20, 1, 'Adventuring gear', "A mess kit is a collection of silverware and cookware used for eating meals. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Mirror, steel', 500, 0.5, 'Adventuring gear', "A steel mirror is a highly polished piece of metal that reflects light. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Oil (flask)', 10, 1, 'Adventuring gear', "Oil is a flammable liquid that can be used to fuel a lantern. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Paper (one sheet)', 20, 0, 'Adventuring gear', "Paper is a thin material produced by pressing together moist fibers of cellulose pulp derived from wood, rags or grasses, and drying them into flexible sheets. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Parchment (one sheet)', 10, 0, 'Adventuring gear', "Parchment is a thin material produced from calfskin, sheepskin or goatskin, often split. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Perfume (vial)', 500, 0, 'Adventuring gear', "Perfume is a fragrant liquid typically made from essential oils extracted from flowers and spices. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Pick, miner\'s', 200, 10, 'Adventuring gear', "A miner's pick is a tool used to break up rock and mineral deposits. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Piton', 5, 0.25, 'Adventuring gear', "A piton is a metal spike that is hammered into rock to support a climber's weight. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Poison, basic (vial)', 10000, 0, 'Adventuring gear', "Basic poison is a substance that causes death or injury when ingested, inhaled, or absorbed into the body. Usually found in an explorer's pack.", ['Utility'], 1),
    ItemData('Pole (10-foot)', 5, 7, 'Adventuring gear', "A pole is a long, slender, rounded piece of wood or metal, typically used with one end placed in the ground as a support for something. Usually found in an explorer's pack.", ['Utility'], 1),



]

RACE_AGE_DB = {
    RACE_HUMAN_KEY: {'base_age': 15, 'age_variation': 20},
    RACE_ELF_KEY: {'base_age': 100, 'age_variation': 100},
    RACE_DWARF_KEY: {'base_age': 50, 'age_variation': 50},
    RACE_HALFLING_KEY: {'base_age': 20, 'age_variation': 30},
    RACE_GNOME_KEY: {'base_age': 40, 'age_variation': 70},
    RACE_DRAGONBORN_KEY: {'base_age': 15, 'age_variation': 10},
    RACE_ORC_KEY: {'base_age': 12, 'age_variation': 10},
    RACE_GOBLIN_KEY: {'base_age': 8, 'age_variation': 10},
    RACE_HOBGOBLIN_KEY: {'base_age': 15, 'age_variation': 10},
    RACE_HALF_ORC_KEY: {'base_age': 14, 'age_variation': 30},
    RACE_HALF_ELF_KEY: {'base_age': 20, 'age_variation': 80},
    RACE_TIEFLING_KEY: {'base_age': 15, 'age_variation': 30},
}

STARTER_GOLD_DB = {
    "Barbarian", "2d4×10",
    "Bard", "5d4×10",
    "Cleric", "5d4×10",
    "Druid", "2d4×10",
    "Fighter", "5d4×10",
    "Monk", "5d4×10",
    "Paladin", "5d4×10",
    "Ranger", "5d4×10",
    "Rogue", "4d4×10",
    "Sorcerer", "3d4×10",
    "Warlock", "4d4×10",
    "Wizard", "4d4×10",
}


ALIGNMENT_LAWFUL_GOOD = "lawful good"
ALIGNMENT_NEUTRAL_GOOD = "neutral good"
ALIGNMENT_CHAOTIC_GOOD = "chaotic good"
ALIGNMENT_LAWFUL_NEUTRAL = "lawful neutral"
ALIGNMENT_NEUTRAL = "neutral"
ALIGNMENT_CHAOTIC_NEUTRAL = "chaotic neutral"
ALIGNMENT_LAWFUL_EVIL = "lawful evil"
ALIGNMENT_NEUTRAL_EVIL = "neutral evil"
ALIGNMENT_CHAOTIC_EVIL = "chaotic evil"

ALIGNMENT_DB = [
    ALIGNMENT_LAWFUL_GOOD,
    ALIGNMENT_NEUTRAL_GOOD,
    ALIGNMENT_CHAOTIC_GOOD,
    ALIGNMENT_LAWFUL_NEUTRAL,
    ALIGNMENT_NEUTRAL,
    ALIGNMENT_CHAOTIC_NEUTRAL,
    ALIGNMENT_LAWFUL_EVIL,
    ALIGNMENT_NEUTRAL_EVIL,
    ALIGNMENT_CHAOTIC_EVIL
]
