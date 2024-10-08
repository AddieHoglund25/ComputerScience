# string functions 
# A group of like-functions that manipulate strings
# they modify strings
# SUPER easy and convenient to use
# Python would really not be fun without them

# .lower()
# converts a string to all lowercase
# no matter what the input casing is, is is converted to lowerrcase
# and the answer is lowercase
input_answer = "Lord of The Rings"
input_answer = input_answer.lower()     #converts to "lord of the rings"
real_answer = "lord of the rings"
print(input_answer == real_answer)

# .upper()
# converts a string to uppercase
x = "hello world".upper()
print(x)            # prints HELLO WORLD

# .capitalize()
# converts to lowercase, thencapitalizes the first letter
y = "heLlO wOrLd".capitalize()
print(y)            # prints Hello world

# .title()
#converts a string to titlecase
z = "HeLlO wOrLd".title()
print(z)            #prints Hello World

# .swapcase()
# it inverts the casing of each character
q = "Hello World!".swapcase()
print(q)            #prints hELLO wORLD!