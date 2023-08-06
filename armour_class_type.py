class ArmourClass:
    def __init__(self, base: int = 0, temporary: int = 0):
        self.base = base
        self.temporary = temporary
        self.actual = base + temporary
        self.derived_from = ''

