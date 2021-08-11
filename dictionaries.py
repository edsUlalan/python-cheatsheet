# simple dictionary
alien = {'color': 'green', 'points': 5}

# accessing a value
skin = alien['color']
print(f"The alien's color is {skin}")

# getting the value with get
dog = {'color': 'red'}

dog_color = dog.get('color')
dog_points = dog.get('points', 0)

print(dog_color)
print(dog_points)

# adding a new key-value pair
alien['x_position'] = 0
print(alien) # {'color': 'green', 'points': 5, 'x_position': 0}

# adding to and empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

# modifying values in a dictionary
color = {'red': 1, 'blue': 2}
print(color)

color['red'] = 3
color['blue'] = 4
print(color)

# deleting a key-value pair
del color['blue']
print(color)

# looping through all key-value pairs
fave_numbers = {'eric': 17, 'ever': 4}
for name, number in fave_numbers.items():
    print(f"{name} loves {number}")

# looping through all keys
for name in fave_numbers.keys():
    print(f"{name} loves a number")

# looping through all values
for number in fave_numbers.values():
    print(f"{number} is a favorite")

# looping through all the keys in reverse order
for name in sorted(fave_numbers.keys(), reverse=True):
    print(f"Hi, {name}!")

# finding dictionary length
num_persons = len(fave_numbers)
print(num_persons)
