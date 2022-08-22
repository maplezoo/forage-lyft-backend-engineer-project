import unittest
import datetime

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime.datetime(2018, 8, 22)
        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.battery_needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime.datetime(2019, 8, 22)
        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.battery_needs_service())
