import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
#Import individul classes from engine modules

class testCapuletEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 60100
        last_service_mileage = 25200
        engine_testing = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine_testing.needs_service())

    def test_engine_shouldnt_be_serviced(self):
        current_mileage = 40100
        last_service_mileage = 25300
        engine_testing = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine_testing.needs_service())

class testSternmanEngine(unittest.TestCase):

    def test_warning_light_is_on(self):
        engine_testing = SternmanEngine(True)
        self.assertTrue(engine_testing.needs_service())

    def test_warning_light_is_off(self):
        engine_testing = SternmanEngine(False)
        self.assertFasle(engine_testing.needs_service())
    
class testWilloughbyEngine(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 90100
        last_service_mileage = 25000
        engine_testing = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine_testing.needs_service())

    def test_engine_shouldnt_be_serviced(self):
        current_mileage = 45100
        last_service_mileage = 25300
        engine_testing = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine_testing.needs_service())

#End of Engine Testing Code

if __name__ == '__main__':
    unittest.main()
#ease of access 