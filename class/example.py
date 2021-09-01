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

# modifying an attribute directly
my_new_car = Car('audi', 'a4', 2019)
my_new_car.fuel_level = 5

# writing a method to update an attribute's value
def update_fuel_level(self, new_level):
    """Update the fuel level."""
    if new_level <= self.fuel_capacity:
        self.fuel_level = new_level
    else:
        print("The tank can't hold that much!")

# writing a method to increment an attribute's value
def add_fuel(self, amount):
    """Add fuel to the tank."""
    if self.fuel_level + amount <= self.fuel_capacity:
        self.fuel_level += amount
        print("Added fuel.")
    else:
        print("The tank won't hold that much.")
