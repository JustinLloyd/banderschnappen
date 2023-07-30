from difficulty import Difficulty
from gem_generator import GemGenerator
from money_generator import MoneyGenerator
from treasure_vessel_generator import TreasureVesselGenerator


class TreasureGenerator:
    BASE_VALUES = {
        Difficulty.EASY: 100,
        Difficulty.MODERATE: 500,
        Difficulty.CHALLENGING: 1000
    }

    MAX_VESSEL_SIZES = {
        Difficulty.EASY: 'medium',
        Difficulty.MODERATE: 'large',
        Difficulty.CHALLENGING: 'gigantic'
    }

    TRAP_BONUS_MULTIPLIER = 1.5

    @staticmethod
    def generate_vessel(difficulty):
        if difficulty not in TreasureGenerator.MAX_VESSEL_SIZES:
            raise ValueError("Invalid difficulty level. It should be one of 'easy', 'moderate', 'challenging'.")

        max_vessel_size = TreasureGenerator.MAX_VESSEL_SIZES[difficulty]
        vessel = TreasureVesselGenerator.generate_random_vessel(max_size=max_vessel_size)

        return vessel

    # @staticmethod
    # def generate_vessel_treasure(treasure, difficulty):
    #     if difficulty not in TreasureGenerator.BASE_VALUES:
    #         raise ValueError("Invalid difficulty level. It should be one of 'easy', 'moderate', 'challenging'.")
    #
    #     base_value = TreasureGenerator.BASE_VALUES[difficulty]
    #     total_value = base_value * TreasureGenerator.TRAP_BONUS_MULTIPLIER if treasure["is_trapped"] else base_value
    #
    #     # Make sure the treasure value doesn't exceed the vessel's capacity
    #     vessel_value = treasure["value"]
    #     total_value = min(total_value, vessel_value)
    #
    #     coins_value = total_value // 2  # Let's put 50% of total value in coins
    #     coins = MoneyGenerator.generate_random_coins(coins_value)
    #
    #     gems_value = total_value - coins_value  # Remaining value goes to gems
    #     gems = GemGenerator.generate_random_gems_up_to_value(gems_value)
    #
    #     treasure["contents"]["coins"] = coins
    #     treasure["contents"]["gems"] = gems


    @staticmethod
    def generate_vessel_treasure(treasure, difficulty):
        if difficulty not in TreasureGenerator.BASE_VALUES:
            raise ValueError("Invalid difficulty level. It should be one of 'easy', 'moderate', 'challenging'.")

        base_value = TreasureGenerator.BASE_VALUES[difficulty]
        total_value = base_value * TreasureGenerator.TRAP_BONUS_MULTIPLIER if treasure["is_trapped"] else base_value

        # Make sure the treasure value doesn't exceed the vessel's capacity
        vessel_value = treasure['vessel']["value"]
        total_value = min(total_value, vessel_value)

        coins_value = total_value // 2  # Let's put 50% of total value in coins
        coins = MoneyGenerator.generate_random_coins(coins_value)

        gems_value = total_value - coins_value  # Remaining value goes to gems
        gems = GemGenerator.generate_random_gems_up_to_value(gems_value)
        for gem in gems:
            gem['description'] = f"Creatively describe {gem['description']}"

        treasure["contents"]["coins"] = coins
        treasure["contents"]["gems"] = gems
