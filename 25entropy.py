#Kelly Chau
#Unit 2
#Write a function that returns the Shannon entropy 
#for nucleotide counts a, c, g, t. 
#Demonstrate it works using multiple calls, including those where one of the counts is zero.

import math
import sys

def Shannon_entropy(a, c, g, t):
	count = a + c + g + t
	assert(count > 0)
	prob_a = a / count
	prob_c = c / count
	prob_g = g / count
	prob_t = t / count
	
	if prob_a <= 0: 
		sys.exit('Error: probability must be greater than 0')
	else:
		a_event = prob_a * math.log2(prob_a)
		
	if prob_c <= 0:
		sys.exit('Error: probablity must be greater than 0')
	else: 
		c_event = prob_c * math.log2(prob_c)
		
	if prob_g <= 0:
		sys.exit('Error: probablity must be greater than 0')
	else: 
		g_event = prob_g * math.log2(prob_g)
		
	if prob_t <= 0:
		sys.exit('Error: probablity must be greater than 0')
	else: 
		t_event = prob_t * math.log2(prob_t)
		
	Shannon_entropy = -(a_event + c_event + g_event + t_event)
	return Shannon_entropy
	
	
#Demo
print(Shannon_entropy(3, 5, 7, 2))
print(Shannon_entropy(3, 2, 4, 2))
print(Shannon_entropy(5, 5, 5, 5))