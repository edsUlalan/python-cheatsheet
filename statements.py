# conditional tests
x = 12
x == 42 # equals => false
x != 42 # not equals => true
x > 24 # greater than => false
x >= 42 # greater or equal => false
x < 42 # less than => true
x <= 42 # less or equal => true

# conditional test with list
bikes = ['one', 'two', 'three']
'one' in bikes # True
'four' not in bikes # True

# checking if a list is empty
players = []

if players:
    for player in players:
        print(f"Player: {player.title()}")
else:
    print("We have no players yet!")

# Assigning boolean values
active = True
online = False

# simple if test
if age >= 18:
    print("You can vote!")

# if-elif-else statements
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15

# more examples on checking equality
car = 'bmx'
car == 'bmx' # True

color = 'red'
color == 'blue' # False

# ignoring case when making comparison
bird = 'Eagle'
bird.lower() == 'eagle' # True

# checking for inequality
topping = 'mushrooms'
topping != 'anchovies' # True

# using and to check multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 # False

age_2 = 23
age_0 >= 21 and age_2 >= 21 # True
