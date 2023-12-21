from abc import ABC, abstractmethod

NegativeMileageException = Exception("The mileage on this car cannot be less than the last service mileage.")

class Engine(ABC):
  @abstractmethod
  def needs_service():
    pass