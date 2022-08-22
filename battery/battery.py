import datetime


class Battery:
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.cycleDate = 2

    def battery_needs_service(self):
        current_date = datetime.datetime.now()
        seconds_per_year = 365 * 24 * 60 * 60
        return (current_date - self.last_service_date).total_seconds() / seconds_per_year > self.cycleDate

