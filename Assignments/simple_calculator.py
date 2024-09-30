
def add():              #defining a new function
    print("Add two numbers:") 
    x = input("What is the first number?\n>")       #ask for input for x
    x = int(x)                      #convert x to int
    y = input("What is the second number?\n>")      #ask for input for y
    y = int(y)                      #convert y to int
    print(str(x) + " + " + str(y) + " = " + str(x + y))
add()

def subtract():
    print("Subtract two numbers:")
    x = input ("What is the first number?\n>")
    x = int(x)
    y = input ("What is the second number?\n>")
    y = int(y)
    print(str(x) + " - " + str(y) + " = " + str(x - y))
subtract()

def multiply():
    print("Multiply two numbers:")
    x = input ("What is the first number?\n>")
    x = int(x)
    y = input ("What is the second number?\n>")
    y = int(y)
    print(str(x) + " * " + str(y) + " = " + str(x * y))
multiply()

def divide():
    print("Divide two numbers:")
    x = input ("What is the first number?\n>")
    x = int(x)
    y = input ("What is the second number?\n>")
    y = int(y)
    print (str(x) + " / " + str(y) + " = " + str (x / y))
divide()