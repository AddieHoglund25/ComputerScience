# if statements evaluate boolean expressions
# make decisions about which code to run next

# Take a temperature
# print "<temperature> is hot" if the temperature is >= 80
# otherwise, print "<temperature> is not hot"
temperature = input("What is the temperature?\n>")
temperature = int(temperature)
# If, boolean expression, :
# sort of like a function, no parenthesis
if temperature >= 80:           #if the bool evaluates to True, go inside
    print("The temperature is " + str(temperature) + " degrees.")
    print(str(temperature) + " degrees is hot outside")
else:                 # Else takes NO condition, runs when if above is false
    #Otherwise...
    print("The temperature is " + str(temperature) + " degrees.")
    print(str(temperature) + " degrees is not hot")

# Complete the activity
# Create a program that asks for a password
# Print "ACCESS GRANTED" if the password is correct
# Print "ACCESS DENIED" if the password is wrong
    
password = input("What is the password?\n>")
if password == "skibidi68":
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

real_password = "skibidi68"
input_password = input ("Please enter the password\n?")
if input_password == real_password:
    print ("ACCESS GRANTED")
else:
    print("ACCESS DENIED")


# Activity 2, electric boogaloo
# create a five question quiz that prints your score at the end
# choose any 5 questions

best_color = input ("What is the best color?\n>")
if best_color == "blue":
    print("Correct")
else:
    print("Wrong")

best_animal = input("What is the best animal?\n>")
if best_animal == "dog":
    print("Correct")
else:
    print("Wrong")

best_movie = input ("What is the best movie?\n>")
if best_movie == "Dunkirk":
    print("Correct")
else:
    print("Wrong")

worst_color = input ("What is the worst color?\n>")
if worst_color == "yellow":
    print("correct")
else:
    print("Wrong")

best_food = input ("What is the best food?\n>")
if best_food == "pasta":
    print("Correct")
else:
    print ("Wrong")