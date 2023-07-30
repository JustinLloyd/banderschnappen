import random

from die_generator import DieGenerator


class GemGenerator:
    gem_types = {
        'Ruby': '20d20',
        'Emerald': '20d20',
        'Sapphire': '30d20',
        'Diamond': '50d100',
        'Amethyst': '4d100',
        'Citrine': '20d20',
        'Onyx': '8d20',
        'Opal': '20d100',
        'Turquoise': '2d20',
        'Moonstone': '8d20',
        'Jade': '4d100',
        'Amber': '4d100',
        'Garnet': '4d100',
        'Aquamarine': '10d100',
        'Pearl': '4d100',
        'Peridot': '8d20',
        'Topaz': '20d100',
        'Tourmaline': '4d100',
        'Alexandrite': '16d100',
        'Agate': '2d20',
        'Coral': '4d100',
        'Jasper': '12d20',
        'Lapis Lazuli': '4d20',
        'Malachite': '2d20',
        'Obsidian': '1d10',
        'Quartz': '2d20',
        'Rhodonite': '2d20',
        'Sunstone': '4d20',
        'Tanzanite': '25d100',
        'Zircon': '8d20'
    }

    designations = {
        'Flawed': 0.5,
        'Cracked': 0.3,
        'Chipped': 0.6,
        'Unpolished': 0.8,
        'Polished': 1.2,
        'Flawless': 2.0,
        'Pulsating': 3.0,
        'Shimmering': 3.5,
        'Glowing': 4.0
    }

    sizes = {
        'Small': 0.5,
        'Medium': 1.0,
        'Large': 2.0,
        'Massive': 4.0
    }

    @staticmethod
    def generate_random_gem():
        """Generate a random gem with a random value."""

        gem_type, dice = random.choice(list(GemGenerator.gem_types.items()))
        gem_size, size_multiplier = random.choice(list(GemGenerator.sizes.items()))
        gem_designation, designation_multiplier = random.choice(list(GemGenerator.designations.items()))

        base_value = sum(DieGenerator.roll_notation(dice))
        gem_value = round(base_value * size_multiplier * designation_multiplier)

        gem = {
            'type': gem_type,
            'size': gem_size,
            'designation': gem_designation,
            'GP': gem_value,
            'description': f'a {gem_size.lower()} {gem_designation.lower()} {gem_type} worth {gem_value}gp'
        }

        return gem

    @staticmethod
    def generate_random_gem_up_to_value(max_value):
        """Generate a random gem with a random value up to a maximum."""
        for _ in range(5):
            gem = GemGenerator.generate_random_gem()
            if gem['GP'] <= max_value:
                remaining_value = max_value - gem['GP']
                return gem, remaining_value

        # If the function hasn't returned after 5 attempts, force an exit with a small, flawed gem
        gem_type = random.choice(list(GemGenerator.gem_types.keys()))
        gem = {
            'type': gem_type,
            'size': 'Small',
            'designation': 'Flawed',
            'GP': max_value,
            'description': f'a small flawed {gem_type} worth {max_value}gp'
        }
        return gem, 0

    @staticmethod
    def generate_random_gems_up_to_value(max_value):
        """Generate a list of random gems with a total value up to a maximum."""
        gems = []
        remaining_value = max_value

        while remaining_value > 0:
            gem, remaining_value = GemGenerator.generate_random_gem_up_to_value(remaining_value)
            gems.append(gem)

        random.shuffle(gems)
        return gems
