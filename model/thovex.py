from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from model.car import Car


class Thovex(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        self.engine_type = CapuletEngine(current_mileage, last_service_mileage)
        self.battery_type = NubbinBattery(last_service_date)

