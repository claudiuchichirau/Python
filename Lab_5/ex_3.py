# Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific types of vehicles 
# like Car, Motorcycle, and Truck. Add methods to calculate mileage or towing capacity based on the vehicle type.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def calculate_mileage(self):
        return "Mileage calculation for cars"

class Motorcycle(Vehicle):
    def calculate_mileage(self):
        return "Mileage calculation for motorcycles"

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def display_info(self):
        return f"{super().display_info()} (Towing Capacity: {self.towing_capacity} lbs)"

print("\n")
car = Car(make="Toyota", model="Camry", year=2022)
print(car.display_info())
print(car.calculate_mileage())

print("\n")

motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2022)
print(motorcycle.display_info())
print(motorcycle.calculate_mileage())

print("\n")

truck = Truck(make="Ford", model="F-150", year=2022, towing_capacity=10000)
print(truck.display_info())
