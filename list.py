bikes = ['trek', 'redline', 'giant']

# get the first element of bikes
first = bikes[0]

# get the second element of bikes
second = bikes[1]

# get the last element of bikes
last = bikes[-1]

# changing an element
bikes[0] = 'valerie'
bikes[-2] = 'robby'

# loop through a list
for bike in bikes:
    print(bike)

# or
for x in bikes:
    print(f"Hi, this is {x}")

# adding item to bikes
bikes.append('specialize')
print(bikes) # ['trek', 'redline', 'giant', 'specialize']

# deleting an element by its position
del bikes[-1]

# removing an item by its value
bikes.remove('valerie')

# remove any items from the list using pop
users = ['val', 'bob', 'mia']
most_recent_user = users.pop() # pop the last item from the list
print(most_recent_user) # 'mia'

first_user = users.pop(0) # pop the first item from the list
print(first_user) # 'val'

# find the length of the list
num_users = len(users)
print(f"We have {num_users} users.")

# sorting a list permanently
users.sort()

# sorting a list permanently in reverse alphabetical order
users.sort(reverse=True)

# sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse=True))

# reversing the order of a list
users.reverse()

# making numerical list
squares = []
for x in range(1,11):
    squares.append(x ** 2)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cubes = []
for y in range(100):
    cubes.append(y ** 3)
print(cubes)

# list comprehensions
squares = [x**2 for x in range(1,11)]

title = ['one', 'two', 'three']
convert_upper =  [t.upper() for t in title]

# making a list of numbers from 1 to a million
numbers = list(range(1, 1000001))

# using a loop to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)

# slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(first_two) # ['sam', 'bob']

middle_two = finishers[2:3]
print(middle_two) # ['bob', 'ada']

last_three = finishers[-3:]
print(last_three) # ['bea', 'ada', 'bob']

# copy a list of bikes
copy_of_bikes = bikes[:]
print(copy_of_bikes) # ['trek', 'redline', 'giant', 'specialize']

# finding the minimum value in a list
ages = [6, 7, 1, 2, 3, 4, 5]
youngest = min(ages)

# finding the maximum
ages = [6, 7, 1, 2, 3, 4, 5]
oldest = max(ages)

# finding the sum of all values
ages = [6, 7, 1, 2, 3, 4, 5]
total_years = sum(ages)

# tuples - similar to list but can't be modified
dimensions = (1920, 1080)

# looping through a tuple
for dimension in dimensions:
    print(dimension)

# overwriting a tuple
sides = (100, 200)
print(sides)
sides = (200, 120)
