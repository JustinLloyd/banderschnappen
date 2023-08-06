class DeathSaves:
    def __init__(self, successes: int = 0, failures: int = 0):
        self.successes = successes
        self.failures = failures

    def reset(self):
        self.successes = 0
        self.failures = 0
