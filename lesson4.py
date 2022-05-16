""" PYTHON KEY WORDS"""
"""
1. True - Represents the boolean true; if the given condition is true, then it returns "True".
    Non-zero values are treated as true
    
2. False - Represents the boolean false; if the given condition is false, then it returns "False".
    Zero value is treated as False
    
3. None - Denotes the null value or void. An empty list or Zero can't be treated as NONE.

4. and - is a ogical operator in Python.
         Used to check multiple conditions.
         Returns true if both conditions are true

5. or - is a logical operator in Python.
        Returns true if one condition is true
        
6. not - is a logical operator in Python.
         Inverts the truth table
"""

""" 7. assert """
"""
assert - Used as a debugging tool in Python.
         It checks the correctness of the code.
         It raises an AssertionError if found any error in the code and also prints the message with an error
"""
print(" -- assert -- ")
a = 10
b = 0
print("a is dividing by zero")
# assert b!=0
# print(a/b) #throws an error

""" 8. def """
"""
def - This key word is used to declare the function in Python
"""
print("")
print(" --- def ---")
def my_func(a,b):
    c = a+b
    print(c)
my_func(30,20)

""" 9. class """
"""
class - Used to represent the class in Python
        The class is the blueprint of the objects
        It is the collection of the variable and methods.
"""
print("")
print(" --- class --- ")
class Myclass:

    def add(a,b):
        a = 40
        b = 60
        c= a+b
        print(c)
    add(a,b)

""" 10. continue """
"""
continue - Used to stop the execution of the current iteration.
"""
print("")
print(" --- continue --- ")
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)

""" 11. break """
"""
break - Used to terminate the loop execution and control transfer to the end of the loop
"""
print("")
print(" -- break -- ")
for i in range(5):
    if(i==3):
        break
    print(i)
print("End of execution")

""" 12. If """
"""
if - Used to represent the conditional statement.
     The execution of a particular block is decided by idf statement
"""
print("")
print(" --- if --- ")
i = 20
if(1<15):
    print("I am less than 20")

""" 13. else """
"""
else - Else statement is used with the if statement.
       When if statement returns false, the else block is executed
"""
print("")
print(" -- else --")
n = 14
if(n%2==0):
    print("Even")
else:
    print("Odd")

""" 14. elif """
"""
elif - Used to check the multiple conditions.
       It's short for else-if
       If previous condition is false, then check until the true condition is found. 
"""
print("")
print(" --- elif --- ")
marks = 30
if(marks>=90):
    print("Excellent")
elif(marks<90 and marks>=75):
    print("very Good")
elif(marks<75 and marks>=60):
    print("Good")
else:
    print("Average")

""" 15. del """
"""
del - used to delete the reference of the object
"""
print("")
print(" --- del --- ")
x=2
y=5
print(x,y)
del x
print(y)
# x nolonger exists
#print(x) # throws an error that x is not defined

""" 16. try, except """
"""
try, except - try-except is used to handle exceptions.
               The exceptions are run-time errors  
"""
print("")
print(" --- try,except --- ")
m=0
try:
    b=2/m
except Exception as e:
    print(e)

""" 17. raise """
"""
raise - is used to throw the exception forcefully
"""
print("")
print(" --- raise --- ")
a=5
# if(a>2):
    # raise Exception('a should not exceed 2')

""" 18. finally """
"""
finally - used to create a block of code thar will always be executed no matter the else block raises an error or not.
"""
print("")
print(" --- finally --- ")
a=0
b=5
try:
    c=b/a
    print(c)
except Exception as e:
    print(e)
finally:
    print("finally was executed")


""" 19. for """
"""
for- used for iterations.
     used to iterate over sequences (list, tuple, dictionary, string)
"""
print("")
print(" --- for ---")
positions = [1,2,3,4,5]
for i in positions:
    print(i)

""" 20. while """
"""
while - Used for iterations
        while loop is executed until the condition returns false
"""
print("")
print(" --- while --- ")
a=0
while(a<5):
    print(a)
    a =a+1

""" 21. import """
"""
import - used to import modules in the current Python script
"""
print("")
print(" --- import --- ")
import math
print(math.sqrt(25))

""" 22. from """
"""
from - used to import the specific function or attributes in the current Python script
"""
print("")
print(" --- from --- ")
from math import sqrt
print(sqrt(36))

""" 23. as """
"""
as - used to create name alias.
     It provides the user-define name while importing a module
"""
import calendar as cal
print(cal.month_name[12])

""" 24. pass """
"""
pass - is used to execute nothing or create a placeholder for future code
        If we declare an empty class or function, it will throw an error,
        so we use the pass key word to declare an empty class or function
"""
print("")
print(" --- pass --- ")
class my_class:
    pass
def my_function():
    pass

""" 25. return """
"""
return - used to return the result value or none to called function
"""
print("")
print(" --- return -- ")
def sum(a,b):
    c = a + b
    return c
print("The sum is:",sum(25,15))

""" 26. is """
"""
is - used to check if the two variables refer to the same object.
     returns true if they refer to the same object otherwise false
"""
print("")
print(" --- is --- ")
x=5
y=5

a=[]
b=[]
print(x is y)
print(a is b)

""" 27. global """
"""
global - used to create a global variable inside the function. Any function can access the global variable
"""
print("")
print(" --- global --- ")
def summation():
    global a
    a = 20
    b = 30
    c = a+b
    print(c)
summation()

def display():
    print(a)
display()

""" 28. nonlocal """
"""
nonlocal - It's similar to the global and used to work with a variable inside
           the nested function ( function inside a function) 
"""
print("")
print(" --- nonlocal --- ")
def outside_function():
    a = 20
    def inside_function():
        nonlocal a
        a = 30
        print("Inner function a : ",a)
    inside_function()
    print("Outer function a : ",a)
outside_function()

""" 29. lambda """
"""
lambda - used to create the anonymous function in Python. 
         It is an inline function without a name
"""
print("")
print(" --- lambda ---")
a = lambda x:x**3
for i in range(1,6):
    print(a(i))

""" 30. yield """
"""
yield - used with the Python generator.
        It stops the function's execution and returns the value to the caller
"""
print("")
print(" --- yield --- ")
def fun_generator():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in fun_generator():
    print(value)

""" 31. with """
"""
with - used in the exception handling.
       Makes code cleaner and more readable
       Advantage of using it is that we don't need to call close(). 
"""
print("")
print(" --- with --- ")
with open('file_path', 'w') as file:
    file.write('Hello World!')

""" 32. None """
"""
none - used to define the null value.
       It's remembered that None does not indicate 0, false, or any empty data-types.
       It is an object of its data-type 
"""
print("")
print(" --- None --- ")
def return_none():
    a = 10
    b = 20
    c = a + b

x = return_none()
print(x)