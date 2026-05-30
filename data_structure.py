""""
Data Structures in Python
Data structures are a way of organizing and storing data in a computer so that it can
be accessed and modified efficiently.
Python provides several built-in data structures , including lists, tuples, sets, and dictionaries.

1. Lists
A list is an ordered collection of items that can be of any type.
List are mutable , meaning that you can change their contents after they have been created.
You can create a list using square breakets '[]' and separate the item with commas.

2. Tuples
A tuple is similar to a list , but it is immutable, meaning that you cannot change
its contents after it has been created.
You can create a tuple using parentheses '()' and separate the items with commas.

3. Sets
A set is an unordred collection of unique items.
sets are mutable, meaning that you can change their contents after they have been created .
You can create a set uding curly '{}' and separate the items with commas.

4. Dictionaries
A dictionary is an unordered collection of key-value pairs.
Dictionaries are mutable , meaning that you can change their contents after they have been created.
You can create a dictionary using curl braces '{}' and separate the key-value pairs with commas.
"""

# Example of a list
my_list = ["apple","banana","cherry",10]
print(my_list[0]) # output : apple
print(my_list[3]) # output : 10
my_list.append("orange")
print(my_list)
my_list.insert(0, " grape")
print(my_list)

""""
List  heloer methods:
- append () : Adds an item to the end of the list.
- insert () : Insert an item at a specified position.
- remove() : Removes the first occurrence of a specified item.
- Pop () : Removes and returns the item at a specified position.
- Sort() : Sort the item of the list in place.
reverse() : Reverses the order of the item in the list.
- Clear() : Removes all the items from the list.
- Count() : Retrns the number of occurrences of a specified item in the list.
"""
"""
tuple - an ordered, imutable collection of items. Tuples are defined by enclosing
the items in parentheses () and separating them with commas, They can contain
elements of different data types, including other tuples.
Tuples are imutable, meaning that once they are created , their elements cannot be 
changed.

tuple helper functions
count() - return the number of items a specified value occurs in a tuple
index() - searches the tuple for a specified value and return the position of 
where it was found 
len() - returns the number of items in a tuple
max() - returns the number largest item in a tuple
sum() - returns the sum of all the items in a tuple
sorted() - returns a sorted list of the specified iterable's items

slicing - allows you to access a range of items in a tuple by specifying a Start 
index, an end index, and an optional step. The syntax for slicing is 
tuple[start:end:step].
The start index is inclusive, while the end index is exclusive.
if the step is not specified, it defaults to 1.
"""
# creating a tuple
my_tuple = (1,2,3,4,5, "hello", True, 5.5)
print(my_tuple)

# count 
print(f"number of occurrences of 3: {my_tuple.count(3)}")

# index
print(f"Index of 'hello': {my_tuple.index('hello')}")

# length of the tuple
print(f"Length of the tuple: {len(my_tuple)}")

# accessing the tuple elements
# print(my_tuple[0])
# slicing a tuple
# print(my_tuple[1:4]) # output: (2, 3, 4)






