#Guess the number

entered_number = -1
import random 
real_number = random.randint(0,101)

while real_number != entered_number:
    try:
        entered_number = int(input("Please enter in your guess\n>"))
    except:
        print("Hmm... That's not right...")

    if entered_number > real_number:
        print("Too high, try again")
    elif entered_number < real_number:
        print("Too small, try again")
    else:
        print("Bingo! The correct number was " + str(real_number))

print("Congrats on getting it right")



# Count the number of attempts and add that in
attempts = 0
entered_number = -1
import random 
real_number = random.randint(0,101)

while real_number != entered_number:
    attempts = attempts + 1
    try:
        entered_number = int(input("Please enter in your guess\n>"))
    except:
        print("Hmm... That's not right...")

    if entered_number > real_number:
        print("Too high, try again")
    elif entered_number < real_number:
        print("Too small, try again")
    else:
        print("Bingo! The correct number was " + str(real_number))
        print(str(attempts) + " attempts.")

print("Congrats on getting it right")
