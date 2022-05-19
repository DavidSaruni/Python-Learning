""" Python While Loop """
# print 1 to 10
i=1
while (i<=10):
    print(i)
    i=i+1
    #print(i) # the peint after increment value exceeds the loop by 1

# print a table for a given number
print(" --- table using while --- ")
i=1
number = 5
while i<=10:
    print("%dX%d=%d\n"%(number,i,number*i))
    i=i+1

""" Loop Control Statements """
"""
While loop sequence can be altered using control statements
"""
print(" -- Loop control Statements -- ")
print(" --- continue --- ")
"""
continue - when continue is encountered the control is transfered to the beginning of the loop
"""
# program to print all letters except 'a' and 'n'
i=0
name = "Captain"
while i<len(name):
    if name[i]=='a' or name[i]=='n':
        i=i+1
        continue
    print("Current letter",name[i])
    i=i+1

"""
break - when break is encountered, it brings control out of the loop.
"""
print(" --- break  ---- ")
i = 0
name = "Python"
while i<len(name):
    if name[i]=='t':
        i=i+1
        break
    print(name[i])
    i = i+1

"""
pass - pass statement is used to declare an empty loop
       it is also used to define empty class, function and control statement
"""

name = "Python"
i=0

while i <len(name):
    i+=1
    pass
print("Value of i: ",i)