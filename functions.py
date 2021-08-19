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
