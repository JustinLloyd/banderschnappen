from typing import Optional


class Connection:
    def __init__(self, location_a: Optional["Location"] = None, location_b: Optional["Location"] = None, direction: Optional[str] = None, navigation: Optional[str] = None):
        self.location_a = None
        self.location_b = None
        self.direction = None
        self.navigation = None
