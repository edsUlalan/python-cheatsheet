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
'one' in bikes # true
'four' not in bikes # true

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
