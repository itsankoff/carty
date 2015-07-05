class CartyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.repr(self.value)


class BadArgumentError(CartyError):
    pass
