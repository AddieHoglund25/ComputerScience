#problem 1
sport = input ("What is your favorite sport?\n>")                   #defining an input
like = input ("Why do you like that sport?\n>")                     #defining an input
team = input ("What is your favorite team from that sport?\n>")     #defining an input
print ("Your favorite sport is " + sport + " because " + like + ". My favorite team is " + team + ".")      #putting everything together

#problem 2
x = input ("What is the first integer?\n>")         #define a new function
x = int(x)              #convert from string to input
y = input ("What is the second integer?\n>")
y = int(y)              #convert from string to input
z = input ("What is the third integer?\n>")
z = int(z)
def add_three(x, y, z):
    print (x + y + z)

add_three(x, y, z)


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