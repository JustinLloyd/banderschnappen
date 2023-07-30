import random

from die_generator import DieGenerator


class TreasureVesselGenerator:
    vessel_designations = ['stashed', 'hidden', 'buried', 'uncovered', 'camouflaged', 'sunken', 'sealed', 'forgotten', 'guarded']
    size_order = ['tiny', 'small', 'medium', 'large', 'massive', 'enormous', 'gigantic']

    vessel_types = {
        'cask': ('10d4', '100d4'),
        'hidden compartment': ('10d4', '100d4'),
        'saddlebag': ('10d4', '100d4'),
        'chest': ('100d4', '1000d4'),
        'pouch': ('10d4', '50d4'),
        'urn': ('2d100', '4d100'),
        'coffer': ('5d100', '15d100'),
        'crate': ('5d100', '20d100'),
        'barrel': ('5d100', '25d100'),
        'pot': ('4d20', '2d100'),
        'cloak bag': ('2d20', '1d100'),
        'bag': ('2d20', '8d20'),
        'backpack': ('3d20', '3d100'),
        'vault': ('5d100', '100d100')
    }

    vessel_sizes = {
        'tiny': 0.25,
        'small': 0.5,
        'medium': 1,
        'large': 2,
        'massive': 3,
        'enormous': 4,
        'gigantic': 5,
    }

    @classmethod
    def generate_random_vessel(cls, max_size='gigantic'):
        valid_sizes = cls.size_order[:cls.size_order.index(max_size) + 1]
        vessel_size = random.choice(valid_sizes)
        vessel_type = random.choice(list(cls.vessel_types.keys()))
        designation = random.choice(cls.vessel_designations)

        min_val, max_val = cls.vessel_types[vessel_type]
        min_val, max_val = DieGenerator.roll_notation_total(min_val), DieGenerator.roll_notation_total(max_val)
        base_value = random.randint(min_val, max_val)

        size_multiplier = cls.vessel_sizes[vessel_size]
        vessel_value = int(base_value * size_multiplier)

        vessel = {
            'type': vessel_type,
            'size': vessel_size,
            'designation': designation,
            'value': vessel_value,
            'text': f"a {vessel_size} {designation} {vessel_type} that can hold up to {vessel_value}gp of items",
            'description': '',
            'noteworthy': ''
        }
        return vessel
