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
