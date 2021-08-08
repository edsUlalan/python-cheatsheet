# simple dictionary
alien = {'color': 'green', 'points': 5}

# accessing a value
skin = alien['color']
print(f"The alien's color is {skin}")

# adding a new key-value pair
alien['x_position'] = 0
print(alien) # {'color': 'green', 'points': 5, 'x_position': 0}

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
