class Vehicle:
    def __init__(self, speed=0, passengers=1, fuel_type=""):
        self.speed = speed
        self.passengers = passengers
        self.fuel_type = fuel_type

    def go(self):
        pass

    def stop(self):
        pass

    def change_direction(self):
        pass


class Car(Vehicle):
    def __init__(
        self, model_type="", doors=1, auto_maker="", speed=0, passengers=1, fuel_type=""
    ):
        super().__init__(speed, passengers, fuel_type)
        self.model_type = model_type
        self.doors = doors
        self.auto_maker = auto_maker

    def radio(self):
        print("nobody touches my radio")

    def wind_shield_wiper(self):
        pass

    def change_direction(self):
        pass
