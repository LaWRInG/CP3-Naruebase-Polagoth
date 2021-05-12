class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Pickup(Vehicle):
    pass;

class Car(Vehicle):
    pass;

class Van(Vehicle):
    pass;

pickup01 = Pickup()
pickup01.turnOnAirConditioner()

car01 = Car()
car01.turnOnAirConditioner()

van01 = Van()
van01.turnOnAirConditioner()