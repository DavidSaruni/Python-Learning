# This lesson covers python Variables

# Python Identifiers

number = 10
print(number)

a = 'Senior Developer'
print(a)

_a = "Captain"
print(_a)

x_y = 'Numerical Python'
print(x_y)

print("john")

print(type("john"))


# Object Identity
a = 50
b = a
print(id(a))
print(id(b))

# Reasigne variable a
a = 500
print(id(a))

# Variable Names
name = "Andela LC"
age = 12
worth = 85.55
print(name)
print(age)
print(worth)

# Multiple Assignment
a=b=c=100
print(a)
print(b)
print(c)

d,e,f = 20,30,40
print(d)
print(e)
print(f)

# Local Variables
# Declaring a function
def product():
    # Declaring local variables. They have scope only within the function
   j = 30
   k = 40
   l = j*k
   print('The product is ',l)

# Function Calling
product()

# Accesing variable out of function will bring an error at our console
# print(l)

# GLOBAL VARIABLES
# Declare a variable and initialize it
m = 200
# Global Variable function
def myglobalvariable():
    # Printing the global variable
    global m
    print(m)
    # We try to modify the global variable
    m = 'Welcome to Nepapa Technologies'
    print(m)


myglobalvariable()
print(m)

# Printing Multiple variables
print("---Print Multiple Variables---")
p='Justine'
q=20
r=3.0


print(p,q,r)

# Print Variable Types
print(type(p))
print(type(q))
print(type(r))
