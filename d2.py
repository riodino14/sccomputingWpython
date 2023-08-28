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
