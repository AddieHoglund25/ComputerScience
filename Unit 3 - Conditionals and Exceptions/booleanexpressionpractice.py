# Boolean Expression
# kind of like a mathematical formula 
# can only evaluate to true or false
# Are my shoes tied? = True
# is 5 > 7 = False
print(5 > 7)

# Comparison operators == > < >= <=
# kind of like arithmetic operators + - / * ** % //
x = 5               # SET x equal to 5, tell it what to be
print (x == 5)      # GET x equals 5, ask a question
#The difference is that we are using one or two equal signs
#This is a PERFECT test question

print (4 >= 2)                  #True
print (1993 == 1993)            #True
print(-90 < -99)                #False
print(10 != 10)                #False, "bash" "not"

#Boolean Expression quiz assignment
answer_one = input ("Give me a integer that is negative")
answer_one = int(answer_one)
print(answer_one < 0)

answer_two = input("Write the number 5\n>")
#answer_two = int(answer_two) THis is unnecessary
print(answer_two == "5")

print("Walrus" == "Walrus")           # == is totally valid for 2 strings
