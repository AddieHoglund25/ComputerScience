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
    print("1. Walk")                                                                # option 1 
    print("2. Take a horse and wagon")                                              # option 2

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
    print("1. Walk")                                                                # option 1
    print("2. Take a horse and wagon")                                              # option 2

    choice = input("> ")

    if choice == "1":
        walk_to_maine()
    elif choice == "2":
        wagon_to_maine()
    else:
        print("invalid choice, try again.")
        start_adventure()


def walk_to_washington():
    print("You are walking to Washington")
    print("1. ")
    print("2. ")

def wagon_to_washington():
    print("You have decided to take a wagon and horse to Washington.")
    print("1. ")
    print("2. ")

def walk_to_maine():
    print("You have decided to walk to Maine.")
    print("1. ")
    print("2. ")

def wagon_to_maine():
    print("You have decided to take a wagon and horse to Maine")
    print("1. ")
    print("2. ")
















start_adventure()