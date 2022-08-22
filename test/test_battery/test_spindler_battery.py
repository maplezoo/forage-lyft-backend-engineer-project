import datetime
import unittest

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime.datetime(2019, 8, 22)
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.battery_needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime.datetime(2020, 8, 23)
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.battery_needs_service())

