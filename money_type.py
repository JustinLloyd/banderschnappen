class Money:
    def __init__(self):
        self.gold = 0
        self.silver = 0
        self.copper = 0

    def get_copper_total(self):
        return self.gold * 100 + self.silver * 10 + self.copper

    def set(self, total_gold: int = 0, total_silver: int = 0, total_copper: int = 0):
        self.gold = total_gold
        self.silver = total_silver
        self.copper = total_copper

    @staticmethod
    def to_copper(total_gold: int = 0, total_silver: int = 0, total_copper: int = 0):
        return total_gold * 100 + total_silver * 10 + total_copper

    def reduce(self, total_gold: int = 0, total_silver: int = 0, total_copper: int = 0):
        cp = self.to_copper(total_gold, total_silver, total_copper)
        # convert total copper to gold, silver and copper remainder
        self.gold = cp // 100
        remaining_copper = cp - cp //100
        self.silver = remaining_copper // 10
        remaining_copper = remaining_copper - remaining_copper // 10
        self.copper = remaining_copper
