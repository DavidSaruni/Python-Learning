""" Python For Loop """
"""
The for loop in Python is used to iterate the statements or a part of the program several times. 
It is frequently used to traverse the data structures like list, tuple, or dictionary.
"""
# iterating through a string
str="Python"
for i in str:
    print(i)
name = "Captain"
for i in name:
    print(i, end='')

# print the multiplication table of a given number
print("\n")
list = [1,2,3,4,5,6,7,8,9,10]
n=6
for i in list:
    table=n*i
    print(table)

# print sum of a given list
list = [10,20,34,92,54,76,89]
sum = 0
for i in list:
    sum = sum+i
    # print("The list total is : ", sum)
print("The list total is : ", sum)

""" For Loop using range() function """
"""
syntax - range(start,stop,step size)
"""
print("")
print(" --- range() --- ")
# print numbers in sequence
for i in range(10):
    print(i, end='')

# print table of a given number
for i in range(1,10):
    c=n*i
    print(n, "*", i,"=",c)

# print even numbers using step size
print("Even numbers")
n=20
for i in range(2,n,2):
    print(i)

# print odd numbers using step size
print("Odd numbers")
n=20
for i in range(1,n,2):
    print(i, end=',')

""" Using the len() function in range() function """
print("")
print(" --- range() with len() --- ")
l = ['Justine', 'Captain', 'Mickey', 'Nick', 'Manuu']
for i in range(len(l)):
    print("Hello ", l[i])


""" Nested For Loop """
print(" --- Nested For Loop --- ")

rows = 5 # user input for rows
for i in range(0,rows+1):   # outer loop prints number of rows
    for j in range(i):
        print("*", end='')
    print()

r=10
for i in range(0,r+1):
    for j in range(i):
        print(i, end='')
    print()

""" For Loop with Else statement """
print(" --- For loop with else statement ")
for i in range(0,5):
    print(i,)
else:
    print("End of loop")

for i in range(0,10):
    print(i)
    break;
else:
    print("For loop exhausted")
    print("The loop is broken because break statement... came out of loop")