# Complete your Converting Data Types activity here

# Successfully convert all of the following variables to another type and print the result
# If the conversion prints without errors, you did the conversion correctly

a = 115         #int -> string
b = 3.14        #float -> string
c = "68"        #string -> int
d = "True"      #string -> boolean
e = True        #boolean -> string
f = False       #boolean -> string
g = '10110111'  #byte -> int
h = "2.54"      #string -> float
i = 100         #int -> float
j = 10.0        #float -> int
k = 254         #int -> byte

a = str(a)
num_str = str(115)
print(a)

num_float = 3.14
float_str = str(num_float)
print (b)

c = str(c)
num_str = "68"
num = int(num_str)
print(c)

d = bool(d)
bool_str = "True"
bool_val = bool(bool_str)
print(d)

e = bool(e)
bool_val = True
bool_str = str(bool_val)
print (e)

f = bool(f)
bool_val = False
bool_str = str (bool_val)
print(f)

g = int(g)
bin_val = '10110111'
bin_val = int(bin_val)
print (g)

h = str(h)
float_str = "2.54"
num = float(float_str)
print (h)

i = int(i)
num = 100
num_float = float(num)
print (i)

j = float(j)
num_float = 10.0
num = int(num_float)
print (j)

k = int(k)
int = 254
int_bin = bin(int)
print(k)
