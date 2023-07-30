import random

from treasure_vessel_generator import TreasureVesselGenerator


class TreasureTrapGenerator:
    traps = {
        'Poison Dart': {'size_factor': 1, 'value_factor': 1, 'vessel_factor': ['chest', 'cask', 'crate', 'vault']},
        'Animated Attacking Objects': {'size_factor': 3, 'value_factor': 1, 'vessel_factor': ['hidden compartment', 'chest', 'crate', 'vault']},
        'Gas Release': {'size_factor': 2, 'value_factor': 1, 'vessel_factor': ['cask', 'chest', 'barrel', 'vault']},
        'Explosive Runes': {'size_factor': 4, 'value_factor': 2, 'vessel_factor': ['hidden compartment', 'chest', 'crate', 'vault']},
        'Illusory Treasure': {'size_factor': 1, 'value_factor': 1, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Acid Spray': {'size_factor': 2, 'value_factor': 1, 'vessel_factor': ['cask', 'chest', 'crate', 'vault']},
        'Alarm Spell': {'size_factor': 1, 'value_factor': 1, 'vessel_factor': ['hidden compartment', 'chest', 'crate', 'vault']},
        'Teleportation Glyph': {'size_factor': 4, 'value_factor': 2, 'vessel_factor': ['hidden compartment', 'chest', 'crate', 'vault']},
        'Summoning Trap': {'size_factor': 5, 'value_factor': 3, 'vessel_factor': ['chest', 'vault']},
        'Blade Trap': {'size_factor': 3, 'value_factor': 2, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Poison Needle': {'size_factor': 3, 'value_factor': 2, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Magical Lock': {'size_factor': 3, 'value_factor': 3, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Weighted Trap': {'size_factor': 3, 'value_factor': 6, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Cursed Gold': {'size_factor': 3, 'value_factor': 6, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Fire Trap': {'size_factor': 3, 'value_factor': 4, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Summoning Glyph': {'size_factor': 3, 'value_factor': 8, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Fear Gas': {'size_factor': 2, 'value_factor': 4, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Dimensional Shifter': {'size_factor': 2, 'value_factor': 8, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Crossbow Bolt': {'size_factor': 3, 'value_factor': 2, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Magic Mouth': {'size_factor': 3, 'value_factor': 8, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Arcane Lock': {'size_factor': 3, 'value_factor': 7, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Flame Trap': {'size_factor': 3, 'value_factor': 5, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Glyph of Warding': {'size_factor': 3, 'value_factor': 5, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Cursed Treasure': {'size_factor': 4, 'value_factor': 5, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Dissolving Trap': {'size_factor': 4, 'value_factor': 10, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Chain Lightning Trap': {'size_factor': 4, 'value_factor': 10, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Disintegration Trap': {'size_factor': 4, 'value_factor': 15, 'vessel_factor': ['chest', 'crate', 'vault']},
        'False Bottom': {'size_factor': 3, 'value_factor': 2, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Lock of Paralysis': {'size_factor': 3, 'value_factor': 4, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Fire Glyph': {'size_factor': 3, 'value_factor': 3, 'vessel_factor': ['chest', 'crate', 'vault']},
        'False Bottom Pit': {'size_factor': 3, 'value_factor': 5, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Trap of Rusting': {'size_factor': 3, 'value_factor': 5, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Swarm Cage': {'size_factor': 3, 'value_factor': 6, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Illusionary Chest': {'size_factor': 3, 'value_factor': 5, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Blade Swing': {'size_factor': 3, 'value_factor': 5, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Possession Curse': {'size_factor': 3, 'value_factor': 5, 'vessel_factor': ['chest', 'crate', 'vault']},
        'Magic Dampening Field': {'size_factor': 3, 'value_factor': 8, 'vessel_factor': ['chest', 'crate', 'vault']}
    }

    @classmethod
    def generate_random_trap(cls, vessel):
        suitable_traps = [trap for trap, trap_info in cls.traps.items() if vessel['type'] in trap_info['vessel_factor'] and vessel['value'] > trap_info['value_factor'] * 100 and TreasureVesselGenerator.vessel_sizes[vessel['size']] >= trap_info['size_factor']]

        if suitable_traps:
            return random.choice(suitable_traps)
        else:
            return None
