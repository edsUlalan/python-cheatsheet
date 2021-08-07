bikes = ['trek', 'redline', 'giant']

# get the first element of bikes
first = bikes[0]

# get the last element of bikes
last = bikes[-1]

# loop through a list
for bike in bikes:
    print(bike)

# or
for x in bikes:
    print(bike)

# adding item to bikes
bikes.append('specialize')
print(bikes) # ['trek', 'redline', 'giant', 'specialize']

# making numerical list
squares = []
for x in range(1,11):
    squares.append(x ** 2)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list comprehensions
squares = [x**2 for x in range(1,11)]

# slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(first_two) # ['sam', 'bob']

# copy a list of bikes
copy_of_bikes = bikes[:]
print(copy_of_bikes) # ['trek', 'redline', 'giant', 'specialize']

# tuples - similar to list but can't be modified
dimensions = (1920, 1080)
