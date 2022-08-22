from battery.nubbin_battery import NubbinBattery
from engine.willoughby_engine import WilloughbyEngine
from model.car import Car


class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        self.engine_type = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery_type = NubbinBattery(last_service_date)
