#Kelly Chau

#Write a program that finds all Pythagorean triples for triangles 
#with sides a and b less than 100. 
#For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. 
#Hint: all sides, including the hypotenuse, must be an integer. 
#There are 62 unique triples (half-matrix minus the major diagonal).

import math

for a in range(1, 100):
	for b in range(a, 100):
		c = (a**2 + b**2) ** 0.50
		if c == c // 1:
			print(a, b, c)
