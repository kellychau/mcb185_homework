#Kelly Chau
#Create a function that solves "n choose k": n! / k!(n - k)! 
#and demonstrate that it works by calling it multiple times 
#with several values of n and k. 
#It's more fun to reuse your factorial function than math.factorial().

import math

def factorial(n):
	factor = 1
	for i in range(1, n + 1):
		factor = factor * i
	return factor

def binomial(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))
	

print(binomial(10, 15))
print(binomial(23, 45))

