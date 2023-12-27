from tire.Tire import ArrayValueException, InvalidValue, Tire

class octoprime_tire(Tire):
    def __init__(self, sensor):
        self.sensor = sensor

    def needs_service(self):
        if len(self.sensor) != 4:
            raise ArrayValueException

        for value in self.sensor:
            if value < 0 or value > 1:
                raise InvalidValue
        return sum(self.sensor) >= 3

