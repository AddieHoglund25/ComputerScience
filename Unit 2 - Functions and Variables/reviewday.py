#2 functions
print("Hello, World!")             #"Hello, World!" is the parameter
input("Please enter your username\>")       # \n is called an escape character
# \n starts a new line (linebreak)
# input is never required - only use when told or want to use

#variables
# syntax (grammar)
# <name> = <value>
x = 5

#Snake naming convention - all lowercase, underscore for spaces
# CONCISE: short and desriptive
username = "hoglund"        # define string ("string of characters")
fav_animal  = "penguin"     # define string ("string" of characters)
total_poptarts = 12         # define integer (whole number)
percent_complete = 23.52    # define float (decimal number)
is_cool = True              # define boolean (True/False)
first_letter = 'c'          # define character (single symbol)
total_poptarts = 8          # reassign (if original value changes)

# Arithmetic Operators
# + - * / **(exponent) %(modulus) //(floor division)
print(4 + 4)             #> 8
print("4" +  "4")       #> 44
print("cat" + "dog")    #> catdog
print("cat" * 3)        #> catcatcat
print("cat" + 3)        #> ERROR: Cannot use + for string and int

# Make some working programs
#1. add two numbers using input
x = input("What is x?\n>")      # input() always returns a string
x = int(x)                      # convert  from string to a int
y = input("What is y?\n>")      # even if you type in a number
y = int(y)                      # convert from string to a int
print(x + y)

#2. Converts celcius to farenheight using input
temp_celcius = input("What is the temperature in Celcius?\n>")
temp_celcius = int(temp_celcius)            #convert to integer
temp_farenheight = (temp_celcius * 1.8) + 32
print(temp_celcius + " degrees C equals " + temp_farenheight + "degrees F")

#some conversion functions
str()
int()
float()
bin()
bool()

#the stuff that goes the parenthesis are called PARAMETERS (green words)
#parameters are the values that the function needs in order to run

#Function
#Functions are a lot like variables
#They have names
#They can be recalled from memory by calling their name
#Store information
#variables store values, functions store code

def potato():       #def keyword + name + () + :
    print("potato") #lines indented underneath are "inside" the functions

#functions are not ran when they are defined
#they must be called by their name to run
potato()    #every function call needs open and closed parentheis
            #even if it has no parameters

#function with parameters
def jump(how_high):
    print("You jumped " + str(how_high) + " inches!")

jump(14)

#function with a lot of parameters
def make_a_word(a, b, c, d, e, f, g, h, i, j, k):
    print(a + b + c + d + e + f + g + h + i + k)
            
#functions can have many many lines
def top_ten_games():
    print ("1. Elden Ring")
    print ("2. Shadow of the Colussus")
    print ("3. Minecraft")
    print ("4. Diablo 3")
    print ("5. Gran Turismo 7")
    print ("6. Overwatch")
    print ("7. Rachet & Clank: Up Your Arsenal")
    print ("8. World of Warcraft")
    print ("9. Path of Exile")
    print ("10. Enter the Gungeon")

#Scope: Global and Local Variables
#Scope refers to the context in which the variable was defined
#GLOBAL - defined at no indentation level
#LOCAL - defined inside a function
    
#Global variables can be used anywhere
todd = "cool guy"           #Global variable - no indentation level

#local variables only exist in the scope they were defined
def my_function():
    smith = "not cool guy"  #Local variable - define in a function
    todd = "strange guy"    #local variavle even though it has the same name
    print(todd)             #prints "strange guy" - local variable
    #When you call a variable in a function
    # it searches for local variable first, then global variables

# if you want to reassign a global variable inside of a function
todd = "cool guy"
def my_function2():
    global todd                 #In this function, whenever I call todd
                                # I mean the global todd, not the local
    todd = "strange guy"        # Reassign Todd - global
    print(todd)                 # print todd - global

#Return functions
#functions can also return values
# the value that is returned is sent back to where the function was called
# this is very similar to how a variable works
#the function does its work and returns an anwser back
def add2 (x, y):
    return x + y        #returns the sum of x and y to where the function was called

add2 (2, 10)            #never prints anything
