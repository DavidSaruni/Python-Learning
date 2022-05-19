""" Python Control Statements """
"""
1. Break Statement
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "cherry":
    break
  print(x)

for i in range(5):
    if i ==3:
        break
    print(i)

subject="python"
for i in subject:
    if i=='h':
        break
    print(i)

""" Break with while loop """
n=0
while n<=10:
    print(n)
    if n==5:
        break
    n+=1


""" Continue Statement """
# continue with for loop
name = "CaptainSDavid"
for i in name:
    if i=='S':
        continue
    print(i, end='')

# continue with while loop
i=0
while i<10:
    i=i+1
    if (i==5):
        continue
    print(i)
print("we jumped 5")

"""
Pass - we use pass where the code will be written somewhere but not yet written in the program file
     - pass is just a placeholder for 'we will add functionality later
"""
print(" --- pass --- ")
values = ['p','y','t','h','o','n']
for value in values:
    pass

for i in range(0,5):
    if i==3:
        pass
        print("This is pass block:",i)
    print(i)

