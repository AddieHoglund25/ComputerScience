# Dictionary is a type of collection like a list
# a list is a collection of items in a sequence
# a dictionary is different
# dictionaries store data in key-value pairs
# you can retreive data quickly by using a unique key
# instead of reteving it by index (position)

# Example
# lists use brackets, dictionaries use braces
addie = {
    "name": "addie", 
    "age" : 17,
    "city": "St. Michael",
    "pets": 1,
    "height": 5.7 
}

# each key must be unique
# retreiving values from a dictionary

print(addie["age"])

# .get allows you to retreive a value without erroring
# when the key doesn't exist
# he second parameter is what is given if value is not found
print(addie.get("height"))
print(addie.get("weight", "Not Found"))

# You can add values to a dictionary
addie["country"] = "USA"

# You can modify values
addie["age"] = 18

print(addie)

# Remove entries
addie.pop("pets")

# iterate through a dictionary using a for loop
for key, value in addie.items:
    print(key + ":" + str(value))

# dictionary functions
print(addie.keys())     # returns all keys
print(addie.values())   # returns all values
print(addie.items())    # returns all pairs
print(addie.clear())    # removes all items from the dictionary
