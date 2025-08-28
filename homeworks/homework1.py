#.venv/
#venv/
#__pycache__/


class Car:
    # инициализатор
    def __init__(self, max_speed, color, model):
        self.max_speed = max_speed
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")

class Bus(Car):
    def __init__(self, max_speed, color, model, number_of_seats):
        super().__init__(max_speed, color, model)
        self.number_of_seats = number_of_seats

    def test(self):
        print(f"Bus test, bus has {self.number_of_seats} seats.")

    def drive_to_location(self, location):
        print(f"Bus {self.model} is driving to {location}")

class Truck(Car):
    def drive_to_location(self, location):
        print(f"Truck {self.model} is driving to {location}")

bus = Bus(100, "green", "Mercedes", 40)
bus.drive_to_location("Bishkek") # Driving ..
bus.test()
truck_man = Truck(200, "grey", "MAN")
truck_man.drive_to_location("Karakol")

print(type(1000))
print(type("hello"))
print(type(bus))
print(isinstance(bus, Bus))
print(isinstance(bus, Car))
print(issubclass(Bus, Car))
print(issubclass(Bus, Truck))

car_honda = Car(160, "silver", "Honda Fit")

vehicles = [car_honda, bus, truck_man]
for vehicle in vehicles:
    vehicle.drive_to_location("Karakol")

# adolf hitler