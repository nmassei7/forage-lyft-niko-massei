import unittest
from datetime import datetime
from battery.Battery import Battery, NegativeTimeException
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class testNubbinBattery(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        current_date = datetime.datetime(1, 1, 2025)
        last_service_date = datetime.datetime(1, 1, 2018)
        battery_testing = NubbinBattery(current_date, last_service_date)
        self.assertFalse(Battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(1, 1, 2021)
        last_service_date = datetime.datetime(1, 1, 2020)
        battery_testing = NubbinBattery(current_date, last_service_date)
        self.assertTrue(Battery.needs_service())

class testSpindlerBattery(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        current_date = datetime.datetime(1, 1, 2025)
        last_service_date = datetime.datetime(1, 1, 2018)
        battery_testing = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(Battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(1, 1, 2021)
        last_service_date = datetime.datetime(1, 1, 2020)
        battery_testing = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(Battery.needs_service())

if __name__ == '__main__':
    unittest.main()
#ease of access 
