#20demo.py by Kelly Chau
import math

print('hello, again') #greeting

#Math Operators
print(1 + 1)
print(1 / 2)
print(5 % 2)

#Math Functions
abs(-2)
pow(2, 3)

math.ceil(2.3)
math.log10(100)

#Functions
def greeting():
	print('hello yourself')
	
def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c

x = pythagoras(3, 4)
print(x)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(3, 4))
print(pythagoras(1, 1))

#User assert() to ensure function only receives correct values
def pythagoras(a, b):
	assert(a > 0)
	assert(b > 0)
	return math.sqrt(a**2 + b**2)

#print(pythagoras(-1, 1))

#Practice Functions
#write a function that turns negative numbers into positive and vice versa

def flip_sign(a):
	return a * -1
	
print(flip_sign(1))

#Conditionals
a = 2
b = 2
if a == b:
	print('a equals b')
	print(a, b)
	
	


