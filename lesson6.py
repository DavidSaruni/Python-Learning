""" Python If-Else Statements"""
""" The If Staetement """
print(" --- if statement --- ")
# num = int(input("Enter a number: "))
num = 6
if num%2==0:
    print("Number is even")

""" Program to print the largest number """
# a = int(input("Enter a? "));
# b = int(input("Enter b? "));
# c = int(input("Enter c? "));
a=4
b=10
c=1
if a>b and a>c:
    print(" a is the largest ")
if b>a and b>c:
    print("b is the largest")
if c>a and c>b:
    print("c is the largest")


""" The If-Else Statement"""
print(" --- if - else --- ")
age=10
# age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

number = 7
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")


""" The elif statement """
# marks = int(input("Enter Your marks: "))
marks = 90
if marks>=90 and marks<=100:
    print(" You scored an A")
elif marks>=80 and marks<90:
    print("You scored a B")
elif marks>=70 and marks<=79:
    print("You scored a C")
elif marks>=60 and marks<=69:
    print("You scored a D")
elif marks>=50 and marks<=59:
    print("You scored an E")
elif marks>=40 and marks<=49:
    print("You failed")
elif marks>=0 and marks<=39:
    print("You will have a retake")
else:
    print("You score is invalid invalid")
