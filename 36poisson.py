#Kelly Chau
#Create a function that computes the Poisson probability of k events 
#occuring with an expectation of n (n^k e^-n / k!) and 
#demonstrate it works by calling it with several values of n and k. Use math.e.

import math

def Poisson(k, n):
	return ((n**k) * (math.e**-n)) / (math.factorial(k))

print(Poisson(20, 46))
print(Poisson(22, 44))