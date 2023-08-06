from alignment_type import Alignment
from armour_class_type import ArmourClass
from death_saves_type import DeathSaves
from hit_points_type import HitPoints
from saving_throws_type import SavingThrows
# from empty_structures import EmptyStructures


class Player:
    def __init__(self, name: str = None, location: str = None, level: int = None, player_class: str = None):
        self.name = name
        self.location = location
        self.level = level
        self.player_class = player_class
        self.companion = None
        self.alignment = Alignment()
        self.ac = ArmourClass()
        self.hp = HitPoints()
        self.death_saves = DeathSaves()
        self.saving_throws = SavingThrows(self)
