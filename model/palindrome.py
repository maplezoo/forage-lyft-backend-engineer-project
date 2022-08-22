from datetime import datetime

from battery.spindler_battery import SpindlerBattery
from engine.sternman_engine import SternmanEngine


class Palindrome(Car):
    def __init__(self, warning_light_is_on, last_service_date):
        self.engine_type = SternmanEngine(warning_light_is_on)
        self.battery_type = SpindlerBattery(last_service_date)
