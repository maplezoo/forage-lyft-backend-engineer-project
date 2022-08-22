from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wear):
        super().__init__(tire_wear)
        self.service_rate = 0.9

    def needs_service(self):
        for tire in self.tire_wear:
            if tire >= self.service_rate:
                return True
        return False
