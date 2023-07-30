import random
import re


class DieGenerator:
    MAX_ROLLS = 1000
    MAX_MODIFIER = 1000
    MAX_LENGTH = 200
    DIE_FACES = [2, 3, 4, 6, 8, 10, 12, 20, 100]

    @staticmethod
    def roll(faces, num=1):
        if faces not in DieGenerator.DIE_FACES:
            raise ValueError(f"Invalid number of faces: d{faces}")
        if num > DieGenerator.MAX_ROLLS:
            raise ValueError(f"Too many dice. Maximum is {DieGenerator.MAX_ROLLS}.")
        if num <= 0:
            raise ValueError(f"Cannot roll a negative or zero number of dice.")
        return [random.randint(1, faces) for _ in range(num)]

    @staticmethod
    def roll_total(faces, num=1, modifier=0):
        if abs(modifier) > DieGenerator.MAX_MODIFIER:
            raise ValueError(f"Modifier is too large. Maximum is {DieGenerator.MAX_MODIFIER}.")
        return sum(DieGenerator.roll(faces, num)) + modifier

    @staticmethod
    def roll_d2(num=1):
        return DieGenerator.roll(2, num)

    @staticmethod
    def roll_d2_total(num=1, modifier=0):
        return sum(DieGenerator.roll_d2(num)) + modifier

    @staticmethod
    def roll_d3(num=1):
        return DieGenerator.roll(3, num)

    @staticmethod
    def roll_d3_total(num=1, modifier=0):
        return sum(DieGenerator.roll_d3(num)) + modifier

    @staticmethod
    def roll_d4(num=1):
        return DieGenerator.roll(4, num)

    @staticmethod
    def roll_d4_total(num=1, modifier=0):
        return sum(DieGenerator.roll_d4(num)) + modifier

    @staticmethod
    def roll_d6(num=1):
        return DieGenerator.roll(6, num)

    @staticmethod
    def roll_d6_total(num=1, modifier=0):
        return sum(DieGenerator.roll_d6(num)) + modifier

    @staticmethod
    def roll_d8(num=1):
        return DieGenerator.roll(8, num)

    @staticmethod
    def roll_d8_total(num=1, modifier=0):
        return sum(DieGenerator.roll_d8(num)) + modifier

    @staticmethod
    def roll_d10(num=1):
        return DieGenerator.roll(10, num)

    @staticmethod
    def roll_d10_total(num=1, modifier=0):
        return sum(DieGenerator.roll_d10(num)) + modifier

    @staticmethod
    def roll_d12(num=1):
        return DieGenerator.roll(12, num)

    @staticmethod
    def roll_d12_total(num=1, modifier=0):
        return sum(DieGenerator.roll_d12(num)) + modifier

    @staticmethod
    def roll_d20(num=1):
        return DieGenerator.roll(20, num)

    @staticmethod
    def roll_d20_total(num=1, modifier=0):
        return sum(DieGenerator.roll_d20(num)) + modifier

    @staticmethod
    def roll_d100(num=1):
        return DieGenerator.roll(100, num)

    @staticmethod
    def roll_d100_total(num=1, modifier=0):
        return sum(DieGenerator.roll_d100(num)) + modifier

    @staticmethod
    def decompose_roll_notation(roll_str):
        """Decompose roll notation into a list of dictionaries."""
        if not roll_str:
            raise ValueError("The roll notation string cannot be empty.")
        if len(roll_str) > DieGenerator.MAX_LENGTH:
            raise ValueError(f"The roll notation string is too long. Maximum length is {DieGenerator.MAX_LENGTH}.")

        roll_dicts = []
        roll_parts = re.findall(r'(\d*)d(\d+)([+-]\d+)?', roll_str)
        for roll_part in roll_parts:
            dice, sides, modifier = roll_part
            roll_dicts.append({
                "dice": int(dice) if dice else 1,
                "sides": int(sides),
                "modifier": int(modifier) if modifier else 0
            })

        # Validate each dictionary
        for roll_part in roll_dicts:
            if roll_part['dice'] < 1:
                raise ValueError(f"Cannot roll less than 1 die: {roll_part['dice']}")
            if roll_part['dice'] > DieGenerator.MAX_ROLLS:
                raise ValueError(f"Too many dice. Maximum is {DieGenerator.MAX_ROLLS}.")
            if roll_part['sides'] not in DieGenerator.DIE_FACES:
                raise ValueError(f"Invalid number of faces: d{roll_part['sides']}")
            if abs(roll_part['modifier']) > DieGenerator.MAX_MODIFIER:
                raise ValueError(f"Modifier is too large. Maximum is {DieGenerator.MAX_MODIFIER}.")

        return roll_dicts

    @staticmethod
    def roll_notation(roll_str):
        """Roll the dice as per the roll notation and return the list of results."""
        roll_dicts = DieGenerator.decompose_roll_notation(roll_str)
        results = []
        for roll_dict in roll_dicts:
            rolls = DieGenerator.roll(roll_dict["sides"], roll_dict["dice"], )
            rolls.append(roll_dict["modifier"])  # Add modifier as a separate entry
            results.extend(rolls)
        return results

    @staticmethod
    def roll_notation_total(roll_str):
        """Roll the dice as per the roll notation and return the total."""
        return sum(DieGenerator.roll_notation(roll_str))

    @staticmethod
    def roll_keep_highest(sides, num=1, keep=1):
        rolls = DieGenerator.roll(sides, num)
        rolls.sort(reverse=True)
        return rolls[:keep]

    @staticmethod
    def roll_keep_highest_total(sides, num=1, keep=1, modifier=0):
        rolls = DieGenerator.roll_keep_highest(sides, num, keep)
        return sum(rolls[:keep]) + modifier

    @staticmethod
    def roll_drop_highest(sides, num=1, drop=1):
        rolls = DieGenerator.roll(sides, num, )
        rolls.sort(reverse=True)
        return rolls[drop:]

    @staticmethod
    def roll_drop_highest_total(sides, num=1, drop=1, modifier=0):
        rolls = DieGenerator.roll_drop_highest(sides, num, drop)
        return sum(rolls[drop:]) + modifier

    @staticmethod
    def roll_keep_lowest(sides, num=1, keep=1):
        rolls = DieGenerator.roll(sides, num)
        rolls.sort()
        return rolls[:keep]

    @staticmethod
    def roll_keep_lowest_total(sides, num=1, keep=1, modifier=0):
        rolls = DieGenerator.roll_keep_lowest(sides, num)
        return sum(rolls[:keep]) + modifier

    @staticmethod
    def roll_drop_lowest(sides, num=1, drop=1):
        rolls = DieGenerator.roll(sides, num)
        rolls.sort()
        return rolls[drop:]

    @staticmethod
    def roll_drop_lowest_total(sides, num=1, drop=1, modifier=0):
        rolls = DieGenerator.roll_drop_lowest(sides, num)
        return sum(rolls[drop:]) + modifier
