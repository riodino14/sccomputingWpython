# strings 
# A string is a sequence of characters
# A string literal uses quotes 'Hello' or "Hello"
# For string ->  +  means "concatenate"
str1 = "Helo"
str2 = ' there'
print(str1 + str2)

# when a string contains numbers, it is still a string 
# We can convert numbers in a string into a number using int()
str3 = '123'
print(int(str3) + 1)

# Looking inside string 
# we can get at any single charcter in a string using an index specified in square brackets 
fruit = 'Banana' #->  index value for B is 0  
letter = fruit[1] #The index value must be an integer and starts at zero
# we can get a python error if the index beyond the end of a string 
x = 3 
w = fruit[x-1]
print(letter, w)  
# Strings have Length. lenght of String for banana is 6, so it is counted from 1.
print(len(fruit)) #The built-in function len gives us the length of a string 

# Looping through Strings 
fruit = 'Banana'
index = 0 
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

# a definite loop using for statemnet is much more elegant 
# The iteration variable is completely taken care of by the for loop 
fruit = 'Banana'
for letter in fruit:
    print(letter)
# Simple loop to encounter the 'a' charcter 
word = 'Banana'
count = 0 
for letter in word :
    if letter == 'a':
        count += 1 
print(count)

# Slicing Strings 
s = 'Monty Python'
print(s[0:4]) #The second number is one beyond the end of the slice - "up to but not including" (output: mont)
print(s[6:20]) #If the second number is beyond the end of the string, it stops at the end (output: Python)
print(s[:2])
print(s[8:])
print(s[:])

# String Concatenation 
a = 'Hello'
b = a + ' ' + 'There'
print(b)

# Using in as a logical Operator 
fruit = 'Banana'
print('n' in fruit) 
print('m' in fruit)
print('nan' in fruit)

