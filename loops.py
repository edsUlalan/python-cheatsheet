# simple while loop
current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

# letting the user choose when to quit
message = ''
while message != 'quit':
    message = input("What's your message? ")
    print(message)
