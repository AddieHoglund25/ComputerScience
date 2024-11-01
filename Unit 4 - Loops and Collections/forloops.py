# For loops
# This is a BIG deal
# For loops allow the programmer to REPEAT, or what we call LOOP
# i is the index for the list

# Write a program that prints the numbers one through ten

# for <temp var> in <list>

# Range is a list like -> range(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0,10):           # 0 is the START value, 10 is the STOP value
    print(i)

top_foods = ["Eggs Benedict", "Fried Chicken", "Mac n Cheese"]
# "Go through every food in top foods"
# Repeats everything in the for loop for each item in the list
# Where food equals the current item
for food in top_foods:
    print(food)

# PRACTICE: Create a list of groceries - 
# Contains: milk, eggs, bread, butter, apples
# Ask for user input on an iteem they purchased
# if the item was on the list, print ("<item> crossed off the list!")
# Remove that item from the list
# You will need to use a for loop to search for that item
# You will need an if statement in the for loop to check  

grocery_list = ["milk", "eggs", "bread", "butter", "apples"]

purchased_item = input("What item did you buy?\n>")

for grocery in grocery_list:
    if grocery == purchased_item.lower():
        print(grocery + " checked off the list!")
        grocery_list.remove(grocery)

print(grocery_list)

# Create a list of five random numbers from 0-100
# use a for loop to find the sum of those numbers










