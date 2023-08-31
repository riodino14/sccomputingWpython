# Iterations 
# Breaking out of the a loop 
# - the break statement ends the current loop and jumps to the statement immediuately following the loop 
# - it is like a loop test that can happen anywhere in the body of the loop 
#  the continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration 

# While Loops 
while True:
    line = input("> ")
    if line[0] == "#" :
        continue 
    if line == "done":
        break
    print(line)
print("Done!")

# Terminal output result 
# > hello there
# hello there
# > # don't print this
# > print this!
# print this!
# > done
# Done!

# Indefinites loops 
# while loops are calles "indefinite loops" because they keep going until a logical condition becomes False 
# The loops we have seen so far are pretty easy to examine to see if they will terminate or if they will be "Infinite loops"
# Sometimes it is a little harder to be sure if a loop will terminate

# definite loops 
# These loops are called "Definite loops" because they exceute an exact number of times.
# we say that "definite loops iterate through the members of a set"
for i in [5,4,3,2,1]:
    print(i)
print('blastoff!')
# Definite loops (for loops) have explicit iteration varuables that changes eact time through a loop. These iteration variables move through the sequence or set 
friedns = ['Rio', 'Glen', 'Bisma']
for friend in friedns :
    print('Happy Graduation: ', friend)
print('You guys are awesome!')

# Loops Idioms: What we do in loops 
smallest = None
print(type(smallest))
print("Before:", smallest)
for itervar in [3, 41, 1, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

for i in range(1,11): # Menyetak angka dari 1 sampai 10 secara menurun 
    print(i) 

# Finding the average in a loop 
count = 0 
sum = 0 
print('before', count, sum)
for value in [9,41,12,3,74,15]:
    count += 1 
    sum = sum + value 
    print(count, sum, value)
print('after', count, sum, '\nAverage:', sum/count)


# seacrh using a boolean variable
# if we just want to search and know if a value was found, 
# we use a variables that starts at False and is set to True as soon as we find what we are looking for.
found = False 
print('Before', found)
for value in [9,41,12,3,74,15] : 
    if value == 3 :
        found = True 
    print(found, value)
print('After', found)

# Finding the smallest value 
smallest = None 
print('Before', smallest)
for value in [9,41,12,3,74,15]:
    if smallest is None :
        smallest = value
    elif value < smallest :   # change < to > if we want to find the largest value and change the var smallest to largest to make it clearer 
        smallest = value 
    print(smallest, value)
print('After', smallest)

# The 'is' and 'is not' operators. Is -> the type and value must be equal 
# ex: 0 == 0.00 (True) | 0 is 0.00 (False) 
# - can be used in logical expressions 
# - imples "is the same as"
# - similiar tio, but stronger than == 
