import random

class Car:
    def __init__(self, model, color, economy):
        self.mileage = 0
        self.fuel = 100
        self.economy = economy
        self.color = color
        self.model = model

    def drive(self, distance):
        fuel_needed = (distance * self.economy) / 100
        if fuel_needed > self.fuel:
            print(f"Error: Not enough fuel to drive {distance} km.")
        else:
            self.fuel -= fuel_needed
            self.mileage += distance

    def distance_left(self):
        return (self.fuel / self.economy) * 100

    def fuel_up(self):
        self.fuel += 20
        if self.fuel > 100:
            self.fuel = 100

    def __str__(self):
        return f"{self.model} ({self.color}), Mileage: {self.mileage}, Fuel: {self.fuel}, Economy: {self.economy} l/100km"

# Create a list of cars
cars = []
models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]


for _ in range(10):
    model = random.choice(models)
    color = random.choice(["Red", "Blue", "Green", "Black", "White"])
    economy = random.uniform(5.0, 15.0)  # Generate a random fuel economy between 5.0 and 15.0 l/100km
    car = Car(model, color, economy)
    cars.append(car)


for car in cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)

most_fuel_car = max(cars, key=lambda x: x.fuel)

print("Car with the most fuel left:")
print(most_fuel_car)
