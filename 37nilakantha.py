#Kelly Chau
#Estimate pi using the Nilakantha series. 
#Hint: you must figure out how to get the +/- to flip-flop with each iteration.

#Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...

pi = 3
number = 3
sign = 1

for i in range(100):
	pi = pi + (sign * (4 / ((number - 1) * number * (number + 1))))
	number = number + 2
	sign = -sign
print(pi)