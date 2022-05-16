# Python Data Types
a = 10
b = "Hi Captain Python"
c = 20.1
print(type(a))
print(type(b))
print(type(c))

# STANDARD DATA TYPES
"""
1. Numbers
2. Sequence Type
3. Boolean
4. Set
5. Dictionary
"""

""" Numbers """
x = 8
print("The type of x is ", type(x))

y = 12.24
print("The type of y is", type(y))

z = 2 + 6j
print("The type of z is ", type(z))
print("z is a complex number", isinstance(2 + 6j,complex))

""" Sequence Type """
# STRING - SEQUENCE OF CHARACTERS REPRESENTED IN THE QUOTATION MARK
print("")
print(" --- Python Strings --- ")
str = "String using double quotes"
print(str)
s=""" A multiple 
lines
string"""
print(s)

str1 = 'Hello PythonDev Captain' # string str1
str2 = " How are you" #string str2
print(str1[0:2])  # printing first two characters using slice operator
print(str1[0:5])  # printing first five
print(str1[4])  # printing the fifth character of the string
print(str1*2)  # printing the string twice
print(str1 + str2)  # printing the concatenation of st1 and str2

"""List"""
"""
Python lists are Similar to arrays in C.
Contains data of different types
Items in the list are seperated by commas(,) and enclosed within square brackets[].
We can use slice [:] operator to access the data of the list
"""
print(" --- Python List ---")
list1 = [1,"hi", "Python", 3]
print(type(list1))  # Checking given type of list
print(list1)    # Printing the list1
print(list1[3:])    # List slicing
print(list1[0:2])   # List slicing
print(list1 + list1)    # List concatenation using + operator
print(list1 * 3)    # List repetition using * operator

"""Tuple"""
"""
A tuple is similar to the list in many ways.
Items of the tuple are seperated by commas (,) and enclosed in parenthesis().
A tuple is a read-only data structure as we can't modify the size and
value of the items of a tuple. 
"""
print(" --- Python Tuple ---")
tup = ("hi","Python",3)
print(type(tup))    # Checking the type of tup
print(tup)  # printing the tuple
# Tuple slicing
print(tup[1:])
print(tup[0:2])

# Tuple Concatenation using + operator
print(tup + tup)

# tuple repetition using * operator
print(tup * 4)

# Adding values to tup throws an error
#tup[2] = "hi"


"""Dictionary"""
"""
Dictionary is an unordered set of a key-value pair of items.
It is like an associative array or a hash table where each key stores a specific value.
Key can hold any primitive data type, whereas value is an arbitrary Python object
Items are seperated with the comma(,) and enclosed in the curly braces {}
"""
print(" --- Python Dictionary --- ")
d = {1:'Captain Python', 2:'Dr Java', 3: 'Pastor Nick', 4: 'Economists Pulei'}
print(d)    # Printing the dictionary

# Accessing values using keys
print("1st peson is "+d[1])
print("2nd name is "+d[4])

print(d.keys())
print(d.values())

"""Boolean"""
"""
Boolean provides two built-in values, True or False.
These values are used to determine the given statement true or false.
True - can be represented by non-zero values or 'T'
False - can be represented by 0 or 'F'
"""
print(' --- Python Boolean Type --- ')
print(type(True))
print(type(False))
#print(false) #throws error; not defined

"""Set"""
"""
Python Set is the unordered collection of the data type. 
It is iterable, mutable(can modify after creation), and has unique elements.
Created using a built-in function set(), or a sequence of elements is passed in 
curly braces and seperated by the comma.
It can contain various types of values
Order of elements is undefined; it may return the changed sequence of the elements
"""

print(' --- Python Set ---')
set1 = set()    # creating an empty set
set2 = {'Captain', 2, 3, "Python"}
print(set2)

set2.add(20)    # Adding elements to the set
print(set2)

set2.remove(2)  # Removing elements from the set
print(set2)

