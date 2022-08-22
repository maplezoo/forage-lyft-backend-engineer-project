

class Car:
    def __init__(self):
        self.engine_type
        self.battery_type

    def needs_service(self):
        return self.engine_type.engine_should_be_serviced() or self.battery_type.battery_needs_service
