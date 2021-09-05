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
