#problem 3
def data_three():   
    word = input ("Give me a random word\n>")
    x = input ("Give me a whole number\n>")
    x = int(x)
    y = input ("Give me a float number\n>")
    y = float(y)
    sum = input(x + y)
    print (sum + " combined with " + word + " equals " + str(sum + word))

data_three()