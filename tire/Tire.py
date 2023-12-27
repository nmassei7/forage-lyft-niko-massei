from abc import ABC, abstractmethod

ArrayValueException = Exception("Sensor value must be an array of exactly four numbers")
InvalidValue = Exception("Sensor values must be between 0 and 1")

class Tire(ABC):
  @abstractmethod
  def needs_service():
    pass