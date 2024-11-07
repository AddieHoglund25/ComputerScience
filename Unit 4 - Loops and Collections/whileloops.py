# there a couple of types loops
# the For loop lets you iterate a list
# -great for looping a set of number of times
# BUT WHAT IF we need to loop an uncertain number of times???
# ex. Entering your password
# You could get it right the first timr
# it could take you a million tries
# or anything in between

real_pass = "potato45"
entered_pass = ""

# A while loop continues looping until the condition is no longer TRUE
while real_pass != entered_pass:                                # check if the entered password matches the real one
    # Ask for the password
    entered_pass = input("Please enter the password\n>")

    # check if the password is correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print("try again...")

# end password checking
print("Welcome!")


# Try this
# UPDATE this while loop so that it prints how many attempts you are on
#print number of attempts every loop

real_pass = "potato45"
entered_pass = ""
attempts = 0

while real_pass != entered_pass:                             
    entered_pass = input("Please enter the password\n>")
    attempts = attempts + 1

    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print(str(attempts) + " attempts.")
        print("try again...")

print("Welcome!")

# With while loops, you need to be careful for infinite loops
# When you put your computer in rest mode, it has nightmares about infinite loops
# An infinite loop happens when you enter a while loop that can never escaped
# HAS TO BE RESOLVED
# example (do not click run...)

#count = 0
#while True:
#   count += 1
#    print("uh oh")


# REAL WORLD EXAMPLE:
# Type "exit" to quit
    
user_input = ""

while user_input != "exit":
    user_input = input("Enter something (type 'exit' to quit)")
    print ("You entered: " + user_input)

print("All done")