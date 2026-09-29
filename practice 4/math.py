x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)

import math

x = math.sqrt(64)

print(x)

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) 
print(y)

import math

x = math.pi

print(x)

import math 
print (math.e)

import math 
r = 4
pie = math.pi
print(pie * r * r)

import math 
a = 2.3
print ("The ceil of 2.3 is : ", end="") 
print (math.ceil(a)) 
print ("The floor of 2.3 is : ", end="") 
print (math.floor(a))
print ("The value of 3**4 is : ",end="")
print (pow(3,4))

import math 
print(math.sqrt(0)) 
print(math.sqrt(4)) 
print(math.sqrt(3.5))

import math 
a = math.pi/6
print ("The value of sine of pi/6 is : ", end="") 
print (math.sin(a)) 
print ("The value of cosine of pi/6 is : ", end="") 
print (math.cos(a)) 
print ("The value of tangent of pi/6 is : ", end="") 
print (math.tan(a))

import random

print("random:", random.random())

print("randint:", random.randint(1, 10))

fruits = ["apple", "banana", "orange"]
print("choice:", random.choice(fruits))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("shuffle:", numbers)