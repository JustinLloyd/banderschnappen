from die_generator import DieGenerator


class Ability:
    def __init__(self, name=None):
        self.name = name
        self.short = name[0:3]
        self.modifier = 0
        self.actual = 0
        self.base = 0

    def roll(self, for_player: bool = False):
        if for_player:
            self.actual = DieGenerator.roll_drop_lowest(4, 6)
        else:
            self.actual = DieGenerator.roll(3, 6)
