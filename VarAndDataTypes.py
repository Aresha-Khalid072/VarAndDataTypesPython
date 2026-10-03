# Python
# it is simple and easy
# free and open source
# high level language
# portable
# code same rehta like differ os mein run ho skata
# backend mein django


print("Hello World")
# print function ka name hota


# python char set
# letters a to z A-Z ,digits 0-9,- + / *, blank space etc
print(25)
print(25+45)


# variable is  a name given to a memory location in a program
# var=value
# kisi random jagah par value store
# agar value change ki tou variable same rahay ga bs value change

name="Aresha"
age=22
price=25.99

print(name)
print(age)
print(price)


print("my name is: ", name)
print("my age is: ", age)

print(f"I am {name} and my age is {age}")


print(type(name))
print(type(age))
print(type(price))


# = assignment operator
age2=age
print(age2)


# Identifiers
# variables name
# a-z,AtoZ,0-9,_,
# name can not start with digit
# can't use special symbols


# DataTypes
# Integers
# +ve,-ve,,0


# String   "AK"
# string can be written in single,double and triple quotes

name1="Aresh"
name2='Aresha'
name3='''Aresha'''

print(name1)
print(name2)
print(name3)



# float  3.99
# decimal values



# boolean True and False


# None
# a=None
# abhi a ki koi value store nayi ki gayi

old=True
a=None
print(type(old))
print(type(a))



# Keywords are reserved words in python
# and as def elif  return True  while pass None etc

# python is case sensitive language


# Q print sum
a=2
b=5
sum=a+b
diff=a-b
print(sum)
print(diff)
print(type(sum))


# Comments
# """ Mutliline comments """
"""
Helloo gyzzz

"""


# type of operators
# perform some operation bw operands
# a+b a and b are operands , + is operator

# Arithmetic Operators
c=5
d=3
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c%d) #remainder
print(c**d) #5^3



# Relational Operators
# comparison
#  == !=  < > <= >=
# return value in True or False

e=50
f=30
print(e == f)
print(e != f)
print(e >= f)
print(e <= f)


# Assignment Operators
# assign value
num=10
print(num)
num=num+10
num += 20
print(num)
num -=20
print(num)
num *=20
print(num)
num /=20
print(num)
num %=5
print(num)
num **=5
print(num)


# Logical operators
# not and or
print(not False)
print(not True)

a1 = 50
b1 = 30
print(not(a1>b1))


# and op
val1=True
val2=True
print(val1 and val2)

# or
val3=False
val4=True
print(val3 or val4)



# type Conversion
# automatically hoti
# casting manually kartay hm


x=2
y=3.5
print(x+y) #2.0+3.5 bcz float superior hai

# string ko string mein add kar sktay
# string ko float mein add nayi kar sktay

# typecasting
u=int("3")
z=7

print(type(u))
print(u+z)


w=3.14
w=str(w)
print(w)
print(type(w))


# Input from User
name=input("Enter your name: ")
print("Welcome ", name)

# input mein koi bhi value input ki woh string mein change ho gyi
age=int(input("Enter your age: "))
print(f"Youur age is {age}")

marks=float(input("Enter your marks:"))
print(f"Your marks are {marks}")


# Write a program to input 2 numbers and enter their sum
number1=int(input("Enter number 1: "))
number2=int(input("Enter number 2: "))
sum=number1+number2
print(f"Your sum is {sum}")


# Write a program to input side of a square and its area
side=float(input("Enter side of square: "))
Area=side*side
print(f"Area of square is {Area}")


# input 2 float numbers and print their average
f1=float(input("Enter number 1 : "))
f2=float(input("Enter number 2 : "))
f3=(f2+f1)/2
print("Average is ",f3)

# input 2 numbers,a11 and b11
# print true if a is greater than or equal to b or else print false

a11=int(input("Enter number 1: "))
b11=int(input("Enter number 2: "))
print(a11 >= b11)


