class Car:
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")


# inherit from class Car
class ElectricCar(Car):
    """A simple model of an electric car."""

    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)

        # Attributes specific to electric cars.
        # Battery capacity in kwh.
        self.battery_size = 75
        # Charge level in %.
        self.charge_level = 0

# adding new methods to the child class
class ElectricCar(Car):
    --snip--
    def charge(self):
        """Fully charge the vehicle."""
        self.charge_level = 100
        print("The vehicle is fully charged.")

# using child methods and parent methods
my_ecar = ElectricCar('tesla', 'model s', 2019)

my_ecar.charge()
my_ecar.drive()

# overriding parent methods
class ElectricCar(Car):
    --snip--
    def fill_tank(self):
        """Display an erro message."""
        print("This car has no fuel tank!")

# instances as attributes
class Battery:
    """A battery for an electric car."""

    def __init__(self, size=75):
        """Initialize battery attributes."""
        # Capacity in kWh, charge level in %.
        self.size = size
        self.charge_level = 0

    def get_range(self):
        """Return the battery's range."""
        if self.size == 75:
            return 260
        elif self.size == 100:
            return 315
