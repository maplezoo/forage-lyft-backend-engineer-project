from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from model.car import Car


class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        self.engine_type = CapuletEngine(current_mileage, last_service_mileage)
        self.battery_type = SpindlerBattery(last_service_date)
