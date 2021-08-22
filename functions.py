# a simple function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# passing an argument
def greet_user(username):
    """Display a personalized greeting."""
    print(f"Hello, {username}!")

greet_user('jesse')

# default values for parameters
def make_pizza(topping='bacon'):
    """Make a single-topping pizza."""
    print(f"Have a {topping} pizza!")

make_pizza()
make_pizza('pepperoni')

# using None to make an argument optional
def describe_pet(animal, name=None):
    """Display information about a pet."""
    print(f"\nI have a {animal}.")
    if name:
        print(f"Its name is {name}.")

describe_pet('hamster', 'harry')
describe_pet('snake')

# returning a value
def add_numbers(x, y):
    """Add two numbers and return the sum."""
    return x + y

sum = add_numbers(3, 5)
print(sum)

# returning a dictionary
def build_person(first, last):
    """Return a dictionary of information about a person."""
    person = {'first': first, 'last': last}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# returning a dictionary with optional values
def build_person(first, last, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first, 'last':last}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

musician = build_person('janis', 'joplin')
print(musician)

# using positional arguments
def describe_pet(animal, name):
    """Display information about a pet."""
    print(f"\nI have a {animal}.")
    print(f"Its name is {name}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# using keyword arguments
describe_pet(animal='monkey', name="kiwew")
describe_pet(name='chow', animal='cat')

# allowing a function to modify a list
def print_models(unprinted, printed):
    """3d print a set of models."""
    while unprinted:
        current_model = unprinted.pop()
        print(f"Printing {current_model}")
        printed.append(current_model)

unprinted = ['phone case', 'pendant', 'ring']
printed = []
print_models(unprinted, printed)

print(f"\nUnprinted: {unprinted}")
print(f"Printed: {printed}")

# preventing a function from modifying a list
def print_models(unprinted, printed):
    """3d print a set of models."""
    while unprinted:
        current_model = unprinted.pop()
        print(f"Printing {current_model}")
        printed.append(current_model)

original = ['phone case', 'pendant', 'ring']
printed = []

print_models(original[:], printed)
print(f"\nOriginal: {original}")
print(f"Printed: {printed}")

# collecting an arbitary number of arguments
def make_pizza(size, *toppings):
    """Make a pizza."""
    print(f"\Making a {size} pizza.")
    print("Toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers', 'onions', 'extra cheese')

#collecting an arbritrary number of keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary for a user."""
    user_info['first'] = first
    user_info['last'] = last

    return user_info

user_0 = build_profile('albert', 'einstein', location='princeton')
user_1 = build_profile('marie', 'curie', location='paris', field='chemistry')

print(user_0)
print(user_1)
