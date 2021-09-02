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
