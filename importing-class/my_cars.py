# importing individual classes from a module

from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
my_beetle.fill_tank()
my_beetle.drive()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.charge()
my_tesla.drive()

# importing an entire module

# import car
#
# my_bettle = car.Car('volkswagen', 'beetle', 2019)
# my_beetle.fill_tank()
# my_beetle.drive()
#
# my_tesla = car.ElectricCar('tesla', 'model s', 2019)
# my_tesla.charge()
# my_tesla.drive()

# importing all classes from a module

# from car import *
#
# my_beetle = Car('volkswagen', 'beetle', 2016)

# Storing objects in a list

# make lists to hold a fleet of cars.
gas_fleet = []
electric_fleet = []

# make 500 gas cars and 250 electric cars.
for _ in range(500):
    car = Car('ford', 'escape', 2019)
    gas_fleet.append(car)
for _ in range(250):
    ecar = ElectricCar('nissan', 'leaf', 2019)
    electric_fleet.append(ecar)

# Fill the gas cars, and charge electric cars.
for car in gas_fleet:
    car.fill_tank()
for ecar in electric_fleet:
    ecar.charge()

print(f"Gas cars: {len(gas_fleet)}")
print(f"Electric cars: {len(electric_fleet)}")
