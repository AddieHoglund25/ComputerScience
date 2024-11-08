# 1
students = {
    "alice": "A",
    "bob": "B",
    "charlie": "C",
    "david": "A",
    "eve": "B",
    "age": 16
}

# 2
for key, value in students.items:
    print(key + ": " + str(value))

# 3
students["alice"] = "A+"

# 4
movies = {
    "dunkirk": 1700,
    "enola holmes 1": 1700,
    "enola holmes 2": 1700
}

movies["despicable me"] = 1700
print(movies) 

#5
fruit = {
    "orange":  20,
    "strawberry": 20,
    "watermelon": 20,
    "apple": 20,
    "pear": 20
}

input = ("What fruit do you want to remove?\n>")
fruit.pop(input)

#6
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
}