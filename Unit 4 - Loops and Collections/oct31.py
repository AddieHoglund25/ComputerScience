# python has 4 types of collectios
# Tuple
# Set
# List
# Dictionary

# Today, we are going to focus on lists
# A list is a way to store more than one value in a single variable
# Those values in the list are called items
# ITEMS can be accessed by their index (position in list)
# INDEX                             0               1               2               3               4

best_elden_ring_weapons = ["Blasphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]

# INDEX         0     1     2     3
best_years = [1776, 1985, 1994, 1957]

#print the index of the value in the list
print(best_years.index(1985))

# Print the best elden ring weapon
print(best_elden_ring_weapons[0])

# print the worst of the best elden ring weapon
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])

# list items can be changed
best_elden_ring_weapons[3] = "Spiked Fist"
print(best_elden_ring_weapons)

#Remove the last item in the list by its position in the list
# the .pop() function removes an item in a list by its position in the list
best_elden_ring_weapons.pop(4)
print(best_elden_ring_weapons)

#Remove an item by its value
best_elden_ring_weapons.remove("Moonveil")
print(best_elden_ring_weapons)

#Add a new item to the end of a list
best_elden_ring_weapons.append("Mohgwyn's Sacred Spear")
print(best_elden_ring_weapons)

import random
numbers = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(numbers)
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)

# strings are lists
# strings are just a list of characters
word = "potato"
print(word[0])



