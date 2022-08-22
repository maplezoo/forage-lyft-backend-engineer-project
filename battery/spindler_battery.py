from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.cycleDate = 2
