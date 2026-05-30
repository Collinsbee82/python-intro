"""
condition - is a statement that can be evaluaated as true or false.
it is used in programming to control the flow of execution based on certain
criteria.
Conditions are often used in if statements, loops, and other control structures to 
determine which code block should be executed.

syntax:
if condition:
       # code to execute if te condition is true
elif another_condition:
    # code  to execute if the another_condition is true 
else:
       # code to execute if all conditions are false
"""

# Example of using conditions in Python
# age = 18
# if age >= 18:
#     print("you are an adult,")
# else:
#     print("Your are a minor,")

# Example of using multiple conditions
# score = 85
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: c")
# elif score >=60:
#     print("Grade: D")
# else:
#     print("Grade: F")
    
""""
write a program that accept a user's age and determines if they are an adult,
and a minor if below 18
"""
# age = int(input("Enter your age:"))
# if age >=18:
#     print(" Your are an adult")
# else:
#     print("your are a minor")

"""
Error handling - is the process to end managing errors that occurs 
 during the execution of a program.
 it involves anticipating potential errors, catching them when they occur,
and providing appropriate responses to ensure that the program continues to 
run smoothly or fails gracefully.
Error handling is crucial for creating robust and user-friendly applications,
as it helps prevent crashes and allows developers to provide meaningful 
feedback to users when something goes wrong.

    syntax:
    try:
         # code that may raise an error
         # code that may raise an error
except SomeError:
         # code to handle the error
except AnotherError:
         # code to handle another error
else:
         # code to execute if no errors were raised 
finally:
         # code to execute regardless of whether an error was raised or not
"""

# examples of using error handling in Python
try:
    user_age = int(input("Enter your age:"))
    if user_age < 0:
          print("Age cannot be negative.")
    else:
        print("Your are minor.")
except ValueError:
    print("Invalid input: please enter a valid age")
""""
write a program that accepts a user's '
'gender and displays "You are a male " if the input is "male ' and 
"You are a female" if the input is female ,if the input is either 
"male" nor "female", display "Invalid input: Please enter 'male' or 'female'".
"""
user_gender = input("Enter your gender(male/female):")
if user_gender == "male":
    print("You are a male")
elif user_gender == "female":
    print("You are a female")
else :
    print("Invalide input: Please enter 'male' or 'female'")
    """"
    write a program that takes a number and displays the corresponding 
    day of the week ( 1 for Monday, 2 for Tuesday, etc).
    if the input is not a valid number between 1 and 7, display "Invalid input:
    """
try:
    day_number = int(input("Enter a number (1-7):"))
    if day_number == 1:
        print("Today is Monday")
    elif day_number == 2:
        print("Today is Tuesday")
    elif day_number == 3:
        print("Today is Wednesday")
    elif day_number == 4:
        print("Today is Thursday")
    elif day_number == 5:
        print("Today is Friday")
    elif day_number == 6:
        print("Today is Saturday")
    elif day_number == 7:
        print("Today is sunday")
    else:
        print("Invalid input: Please enter a number between 1 and 7")
except ValueError:
    print("Invalid input: Please enter a valid number between 1 and 7") 
    
        
        
