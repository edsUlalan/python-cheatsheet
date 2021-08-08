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

# returning a value
def add_numbers(x, y):
    """Add two numbers and return the sum."""
    return x + y

sum = add_numbers(3, 5)
print(sum)
