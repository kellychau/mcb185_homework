#Unit 4
#You have probably heard before that 1 z-score corresponds to 
#approximately 2/3 of the data, and 2 z-scores corresponds to 95% 
#(e.g. the typical threshold for statistical significance). 
#Write a program that generates numbers drawn from a normal distribution 
#and calculate how many of those are 1, 2, or 3 z-scores above the mean. 
#Use random.gauss().

import random

z1 = 0
z2 = 0
z3 = 0
limit = 100000
for i in range(limit):
	r = random.gauss(0.0, 1.0)
	if r > 1:
		z1 += 1
	if r > 2: 
		z2 += 1
	if r > 3:
		z3 += 1
print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)
