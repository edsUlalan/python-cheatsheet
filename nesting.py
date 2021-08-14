# storing dictionaries in a list
users = []

new_user = {
  'last': 'fermi',
  'first': 'enrico',
  'username': 'efermi'
}

users.append(new_user)

new_user = {
  'last': 'curie',
  'first': 'marie',
  'username': 'mcurie'
}

users.append(new_user)

for user in users:
    for k, v in user_dict.items():
        print(f"{k}: {v}")
    print("\n")


persons = [
  {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi'
  },
  {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie'
  }
]

for user_dict in persons:
    for k, v in user_dict.items():
        print(f"{k}: {v}")
    print("\n")

# storing list in a dictionary
fav_languages = {
  'jen': ['python', 'ruby'],
  'sarah': ['c'],
  'edward': ['ruby', 'go'],
  'phil': ['python', 'haskell']
}

for name, langs in fav_languages.items():
    print(f"{name}: ")
    for lang in langs:
        print(f"- {lang}")

# storing dictionaries in a dictionary
users = {
  'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton'
  },
  'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris'
  }
}

for username, user_dict in users.items():
    print("\nUsername: " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']

    print(f"\tFullname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# using loop to make a dictionary
squares = {}
for x in range(5):
    squares[x] = x**2

# using a dictionary comprehension
squares = {x:x**2 for x in range(5)}

# using zip() to make a dictionary
group_1 = ['kai', 'abe', 'ada', 'gus', 'zoe']
group_2 = ['jen', 'eva', 'dan', 'isa', 'meg']

pairings = {name:name_2
    for name, name_2 in zip(group_1, group_2)}

# generating a million dictionaries
aliens = []

for alien_num in range(1000000):
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['points'] = 5
    new_alien['x'] = 20 * alien_num
    new_alien['y'] = 0
    aliens.append(new_alien)

num_aliens = len(aliens)

print("Number of aliens created:")
print(num_aliens)
