""" Python Operators """
""" Arithmetic Operators """
print(" --- Arithmetic Operators --- ")
x=11
y=2
print(x+y)  # Addition
print(x-y)  # Subtraction
print(x*y)  # Multiplication
print(x/y)  # Division
print(x%2)  # Modulus
print(x**y) # Exponentiation
print(x//y) # Floor division

""" Assignment Operators """
print(" --- Assignment Operators --- ")
a = 5
print(a)
a+=3
print(a)
a = 6
a-=3
print(a)
a = 5
a*=3
print(a)
a = 7
a/=2
print(a)
a=11
a%=2
print(a)
a=90
a//=3
print(a)
a=2
a**=4
print(a)
a=5
a&=3
print(a)

a=4
a|=3
print(a)

a=2
a^=3
print(a)

a=20
a>>=2
print(a)

a=15
a<<=2
print(a)

""" Comparison Operators """
print(" --- Comparison Operators --- ")

x=3
y=5
print(x==y) # Equal
print(x!=y) # Not Equal
print(x>y)  # Greater than
print(x<y)  # Less than
print(x>=y) # Greater than or Equal to
print(x<=y)  # Less than or Equal to

""" Python Logical Operators """
print(" --- Python Logical Operators --- ")
x=5
print(x>3 and x<10) # and - returns true because both conditions are true
print(x>3 or x<4)   # or - returns true because one of the conditions is true
print(not(x>3 and x<10))  # not - returns False because not is used to reverse the result


""" Python Identity Operators """
print(" --- Python Identity Operators --- ")
x = ['apple', 'banana']
y = ['apple', 'banana']
z=x

print(" --- is --- ")
print(x is z)   # returns True because z is the same object ads x
print(x is y)   # returns False because x is not the same object as y, even if they have the same content
print(x==y)   # to demonstrate the difference between 'is' and '=='. This comparison returns True because x is equal to y

print(" --- is not --- ")
print(x is not z)   # returns False because z is the same object as x
print(x is not y)   # returns True because x is not the same object as y, even if they have the same content
print(x != y)   # to demonstrate the difference between 'is not' and '!='. This comparison returns False because x is equal to y


""" Python Membership Operators """
print(" --- Python Membership Operators --- ")
x=["pineapple", "Banana", "Orange"]
print("pineapple" in x) # returns true because a sequence with the value "pineapple is in the list.
print("Mango" in x) # returns False because a sequence with the value "Mango" is not in the list
