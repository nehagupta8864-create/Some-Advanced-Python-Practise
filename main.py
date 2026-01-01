import math

math.floor(5.2368)
result= math.sqrt(3025000)
print(result)
print("Done with the previous program.")

from math import sqrt,pi

result= math.sqrt(900000)
print(result)
print("Done with the previous program")
result= math.sqrt(850124)*pi
print(result)

from math import sqrt as s

result= s(745200)*pi
print(result)
print("Done with the previous program.")

import math as m
result= m.sqrt(12036400)* m.pi
print(result)

import math as math_bulletin_python

result= math_bulletin_python.sqrt(852369)*math_bulletin_python.pi
print(result)
print("Done with the previous program.")

import math

print(dir(math))
print(math.nan, type(math.nan))

x=4
print(x)

def hello():
    print(x)
    print("Hello Harry")

hello()

x= 4
print(x)

def hello():
    x=85
    print("Hello harry")
    print(f"The Local x is {x}")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")

print("Done with the previous program.")

def hello():
    x=896
    y=412
    print(f"The local x is {x}")
    print(f"The local y is {y}")
x=8523
print(f"The global x is {x}")
print("Done with the previous program")
hello()
# print(y) # Throws error as y is a local(inside the hello() function) variable not global

x= 745
print(f"The global variable x is {x}.")

y= 7458
print(f"The global varibale y is {y}")

def my_function():
    x= 85237
    y=96547
    print(f"The local varibale y is {y}")
    print(f"The local variable x is {x}.")

print("How to make a local variable global")

def my_function():
    global x
    global y
    x= 85214
    y=96325
    print(f"The global varibale y is {y}")
    print(f"The global variable x is {x}.")

print("Done with the previous program.")
my_function()
print(f"The global varibale y is {y}")
print(f"The global variable x is {x}.")

with open("file.txt", "r") as f: # Special Program
    print(type(f))
    f.seek(10)

    data= f.read(5)
    print(data)

def double(x):
    return x**2

print(double(85))

def cube(x):
    return x**3

print(cube(963))
print("Done with the previous program.")
