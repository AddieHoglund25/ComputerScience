def start_adventure():                                                                                   # starting function
    print("You and your immeadiate family want to see other relatives, where do you want to go?")        # asking user where they want to go
    print("1. Washington, on the west coast")                                                            # option to go to Washington
    print("2. Maine, on the east coast")                                                                 # option to go to Maine

    choice = input("> ")

    if choice == "1":
        go_to_washington()
    elif choice == "2":
        go_to_maine()
    else:
        print("Invalid choice, try again.")
        start_adventure()

def go_to_washington():                                                             # start of the Washington function
    print("You have decided to go to Washington, how do you want to get there?")    # asking how you want to travel
    print("1. Walk")                                                                # option 1 (walk)
    print("2. Take a horse and wagon")                                              # option 2 (take a horse and wagon)

    choice = input ("> ")

    if choice == "1":
        walk_to_washington()
    elif choice == "2":
        wagon_to_washington()
    else:
        print("invalid choice, try again.")
        start_adventure()

def go_to_maine():                                                                  # start of the Maine function
    print("You have decided to go to Maine, how do you want to get there?")         # asking how you want to travel
    print("1. Walk")                                                                # option 1 (walk)
    print("2. Take a horse and wagon")                                              # option 2 (take a horse and wagon)

    choice = input("> ")

    if choice == "1":
        walk_to_maine()
    elif choice == "2":
        wagon_to_maine()
    else:
        print("invalid choice, try again.")
        start_adventure()

# USER DECIDED WHERE THEY WANTED TO GO AND HOW TO GET THERE. BELOW IS FUNCTIONS FOR AFTER THE USER DECIDED HOW TO GET THERE


def walk_to_washington():                                                                                                           # walking to washington function
    print("You are walking to Washington. How do you plan on getting to the other side of the Rocky Mountains?")                    # asking user how to get over rocky mountains
    print("1. Go over the mountain. This is faster but the forecast shows there will possibly be a snowstorm")                      # option 1 (go over the mountain to get there)
    print("2. Go around the mountains. This is longer and you will miss that possible snowstorm")                                   # option 2 (go around the mountain)

    choice = input("> ")

    if choice == "1":
        over_rocky_mountains()
    elif choice == "2":
        around_rocky_mountains()
    else:
        print("invalid choice, start over")
        start_adventure()


def wagon_to_washington():                                                                                               # wagon and horse to washington
    print("You have decided to take a wagon and horse to Washington. When do you want to leave?")                        # asking user when they want to leave
    print("1. Tomorrow")                                                                                                 # option 1 (you would leave tomorrow morning)
    print("2. Friday")                                                                                                   # option 2 (you would leave friday morning)

    choice = input("> ")

    if choice == "1":
        leave_tomorrow()
    elif choice == "2":
        leave_friday()
    else:
        print("invalid choice, start over")
        start_adventure()


def walk_to_maine():                                                                                                                # walking to maine function
    print("You have decided to walk to Maine. How do you plan on getting to the other side of the Appalachian Mountains?")
    print("1. Go over the mountains. This would be quicker, but there is a possibility you would run into some hillbillies")        # option 1 (go over the mountains)
    print("2. Go around the mountains. This would take longer, but it is safer and you could run out of food")                      # option 2 (go around the mountains)

    choice = input("> ")

    if choice == "1":
        over_appalachian_mountains()
    elif choice == "2":
        around_appalachian_mountains()
    else:
        print("invalid choice, start over")
        start_adventure()


def wagon_to_maine():
    print("You have decided to take a wagon and horse to Maine, this is the longest journey, what do you want to bring?")                   # wagon and horse to maine funcion
    print("1. Lots of food and water, a spare wheel, a bow, arrows, a knife, tent, and a jacket")                                           # option 1 (lots of food)
    print("2. Little food and water, lots of blankets, a knife, fire equipment, tent, and medicine")                                        # option 2 (little food)

    choice = input("> ")

    if choice =="1":
        lots_of_food()
    elif choice == "2":
        little_food()
    else:
        print("invalid choice, start over")
        start_adventure()


#  FUNCTIONS OF MORE CHOICES LIKE GOING OVER OR AROUND MOUNTAINS, WHEN THE USER WANTS TO LEAVE, AND WHAT THEY WANT TO BRING


def over_rocky_mountains():
    print("You have picked to go over the rocky mountains. When you are on top of the mountains a blizzard decides to come on top of the mountain. What do you want to do?")
    print("1. Stay on top of the mountain and wait for the blizzard to pass by")
    print("2. Keep walking to the other side of the mountain through the blizzard")

    choice = input("> ")

    if choice == "1":

    elif choice == "2":

    else:
        print("invalid choice, try again")
        start_adventure()


def around_rocky_mountains():
    print("You decided to go around the rocky mountains, which is the longer route. You are starting to run out of food, what do you want to do?")
    print("1. Turn around and go home")
    print("2. Keep going and go hunting for food")


def leave_tomorrow():
    print("You have decided to leave tomorrow morning")
    print("1. ")
    print("2. ")


def leave_friday():
    print("You have chose to leave Friday morning")
    print("1. ")
    print("2. ")

def over_appalachian_mountains():
    print("You have decided to go over the appalachian mountains")
    print("1. ")
    print("2. ")

def around_appalachian_mountains():
    print("You have picked to go around the appalachian mountains")
    print("1. ")
    print("2. ")

def lots_of_food():
    print("You have pickedd to bring a lot of food")
    print("1. ")
    print("2. ")

def little_food():
    print("You have picked to bring a little amount of food")
    print("1. ")
    print("2. ")








start_adventure()