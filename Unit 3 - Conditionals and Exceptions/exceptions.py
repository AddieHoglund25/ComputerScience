# Exception Handling
# Write a program that asks for 2 numbers and adds them

# if = try
# else = except
# elif = except specific error type
def divide_two_numbers():
    try:
        x = int(input ("Whats the first number?\n>"))
        y = int(input ("Whats the second number?\n>"))
        print(x / y)

    except ValueError:
        print("Please enter a number...")
        divide_two_numbers()

    except ZeroDivisionError:
        print("Cannot divide by zero...")
        divide_two_numbers()

divide_two_numbers()

