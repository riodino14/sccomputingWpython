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
