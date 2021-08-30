class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capcity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")

# creating an object from a class
my_car = Car('audi', 'a4', 2016)

# accessing attribute values
print(my_car.make)
print(my_car.model)
print(my_car.year)

# calling methods
my_car.fill_tank()
my_car.drive()

# creating multiple objects
my_car = Car('audi', 'a4', 2019)
my_old_car = Car('subaru', 'outback', 2015)
my_truck = Car('toyota', 'tacoma', 2012)
