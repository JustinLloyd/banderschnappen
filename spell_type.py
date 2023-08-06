class Spell:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description


SPELL_MAGIC_MISSILE = Spell(
    name='Magic Missile',
    description='A missile of magical energy darts forth from your fingertip and strikes its target, dealing 1d4+1 points of force damage.')
