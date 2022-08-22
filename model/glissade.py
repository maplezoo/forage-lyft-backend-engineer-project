from datetime import datetime

from battery.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine
from model.car import Car


class Glissade(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        self.engine_type = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery_type = SpindlerBattery(last_service_date)

