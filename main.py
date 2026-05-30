name = input("Enter your name: ")
print(f"hello, {name}! ")

""""
string helper functions :
- len() - return the length of a string
- upper() - converts a string to uppercase
- lower() - converts a string to lowercase
- title() - converts a the first character of each word to uppercase
- strip() - removes leading and trailing whitespace from a string
- replace() - replace occurrences of a substring with another substring
- split() - splits a string into a list of substrings based on a delimiter
- join() - joins a list of strings into a  single string with a specified delimiter
"""
# Example usage of string helper functions 
greeting = " Hello, World! "
print (greeting.strip()) # output : "Hello,World"
print (greeting.upper()) # output : "hello,world"
print (greeting.lower()) # output : hello,world "
print (greeting.title()) # outpot : hello,world "
print(greeting.replace( " World", "Python")) # output : Hello,python! "
print(greeting.split()) # output ;['Hello,','World!']
words = ["Hello", "World"]
print(" ".join(words)) # output : "Hello World"

print("hello, Collins")
"""
write a program that accept two numbers and display the sum
"""
"""
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter a second number: "))
result = num1 + num2 
print(f" the sum of {num1} and {num2} is;{result}")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 / num2
print(f"{num1} divided {num2} is: {result}")

num1 = float(input("Enter a number: "))
num2 = float(input(Enter another number: "))
result= num1 - num2
print(f"{num1} substracted by {num2} is: {result}")
"""


"""
write a program that accept the first name and the last name,then display your fullname in uppercase 
"""
first_name = input("Enter  yourfirst name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"

print(f"Your full name is: {full_name.upper()}")
#Accept another name and use replace method to change the last name
other_name = input ("Enter another name: ")

new_name = full_name.replace(last_name, other_name)
print(f"Your new full name is: {new_name.upper()}")

