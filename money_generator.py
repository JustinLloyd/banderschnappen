import random

from die_generator import DieGenerator


class MoneyGenerator:
    @staticmethod
    def generate_random_coins(gp):
        if gp <= 0 or not isinstance(gp, int):
            raise ValueError("Invalid gp value. It must be a positive integer.")

        # Coin types with their corresponding values (in cp) and weights
        coins_info = {
            'gold': {'value': 100, 'weight': 0.5},
            'silver': {'value': 10, 'weight': 0.3},
            'copper': {'value': 1, 'weight': 0.2}
        }

        remaining_cp = gp * 100  # convert gp to cp
        coins = {'gold': 0, 'silver': 0, 'copper': 0}

        while remaining_cp > 0 and coins_info:

            coin = random.choices(list(coins_info.keys()), weights=[coins_info[coin]['weight'] for coin in coins_info.keys()], k=1)[0]
            max_coin = remaining_cp // coins_info[coin]['value']
            if max_coin > 0:
                coin_amount = random.randint(1, max_coin)
                remaining_cp -= coin_amount * coins_info[coin]['value']
                coins[coin] += coin_amount
            else:
                del coins_info[coin]

        return coins

    @staticmethod
    def generate_random_coins_notation(roll_str):
        total_gp = sum(DieGenerator.roll_notation(roll_str))
        return MoneyGenerator.generate_random_coins(total_gp)

    @staticmethod
    def generate_coins_between(min_gp, max_gp):
        total_gp = random.randint(min_gp, max_gp)
        return MoneyGenerator.generate_random_coins(total_gp)
