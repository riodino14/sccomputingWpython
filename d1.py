name = input("Masukkan nama anda: ")
age = input("Masukkan umur anda: ")
print("----Informasi Pelajar----\nNama: ", name, "\nUmur: ",  int(age) )

# # Conditional structures 
x = int(input("Number Categorized (Must be Number!): "))
if x < 2 : 
    print("Below 2")
elif x < 20 : 
    print("Below 20")
elif x < 10 : 
    print("Below 10")
else: 
    print("Something else")

# #try / except 
rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print("Nice Work")
else :
    print("Not a number")

temp = "5 degrees"
cel = 0
try:
    fahr = float(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
except:
    print(cel)

# several  build in  function in python 
big = max('Helloworld')
print(big)
tiny = min('Helloworld')
print(tiny)
# type()
# str()
# int()
# float()

# What is the purpose of the "def" keyword in Python?
# It indicates the start of a function, and the following indented section of code is to be stored for later.
# function definition (def) (Void function)
def addtwo(a,b):
    result = a + b 
    print(result)
addtwo(1098, 697)

# return values 
# Often a function will take its arguments, do some computation, and return a value to be used as the baluie of the function call in the calling expression. 
# The return keyword is used for this.

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return ('Bonjour')
    else :
        return ('Hello')
print(greet('fr'), 'Mario')

# a "fruitful" function is one that produices a result(or return value)
# the return statement ends the function execution and "sends back" the result of the function

# Void (noon-fruitful) functions 
# - when a function does not return a vlaue, we call it a "void" function 
# - Function the return values are "fruitful" functions 
# - Void functions are "NOT FRUITFUL"
