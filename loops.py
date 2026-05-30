"""
Loop - a programing structure that repeats a sequence of instructions until a 
specific condition is met
Types of Loops:
1. For loop - used to iterate over a sequence (like a list, tuple, or string)
or other iterable objects.
2. while loop - repeates executes a block of code as long as a specified condition is true.

syntax of for loop:
for variable in sequence:
    # code is execute

 syntax of while loop:
    while condition:
    # code to execute   
    
parts of a loop:
1. variable - a temporary name that represent the current item in the sequence.
2. sequence - the collection of item that the loop will iterate over.

general parts of a loop 
1. initialiazation - setting up any necessary variable before the loop starts.
2. condition - the expression that is evaluated before each iteration of the loop.
3. increment/decrement - updating the loop variable to eventually meet the exit condition.

example using the range() function:
0 - starting point, 5 - ending point (exclusive), 1- step (increment)
for i in range(0, 5, 1):
    print(i)
for i in range(5): # this will interate from 0 to 4
    print(i)


syntax of while loop:
    while condition:
        #code to execute 
"""
# for loop example 
for i in range(5):
       print(i)