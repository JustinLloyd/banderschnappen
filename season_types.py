class SeasonData:
    def __init__(self, name: str = None, description: str = None, minimum_temperature: int = -40, maximum_temperature: int = 130):
        self.name = name
        self.description = description
        self.minimum_temperature = minimum_temperature
        self.maximum_temperature = maximum_temperature

    def validate(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Each season must have a name, it must be a string, and it cannot be empty.")

        if not self.description or not isinstance(self.description, str):
            raise ValueError("Each season must have a description, it must be a string, and it cannot be empty.")

        if self.minimum_temperature is None or not isinstance(self.minimum_temperature, int):
            raise ValueError("Each season must have a minimum temperature, it must be an integer, and it cannot be empty.")

        if self.maximum_temperature is None or not isinstance(self.maximum_temperature, int):
            raise ValueError("Each season must have a maximum temperature, it must be an integer, and it cannot be empty.")


class Season:
    def __init__(self, data: SeasonData = None):
        self.name = data.name
        self.description = data.description
        self.minimum_temperature = data.minimum_temperature
        self.maximum_temperature = data.maximum_temperature
