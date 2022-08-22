from battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.cycleDate = 4
