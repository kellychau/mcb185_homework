
#Kelly Chau Unit2 homework
#Write a function that solves the quadratic formula (ax^2 + bx + c), 
#returning the two X-intercepts. 
#Demonstrate that it works by using the formula multiple times within the program.

import math 
import sys


def quad(a, b, c): #start defining the function
	assert(a != 0) #make sure that the value of a is not 0
	square_root = b**2 - 4*a*c
	if square_root >=0:
		root1 = ((-b + math.sqrt(square_root)) / (2 * a))
		root2 = ((-b - math.sqrt(square_root)) / (2 * a))
	else: 
		sys.exit() #break out of the function
	return root1, root2 
	


#demonstrating that the quadratic function works
root1, root2 = quad(10, 30, 20)
print("root1:", root1,",", "root2:", root2)

root1, root2 = quad(1, 70, 80)
print("root1:", root1,",", "root2:", root2)

root1, root2 = quad(10, 25, 23)
print("root1:", root1,",", "root2:", root2)