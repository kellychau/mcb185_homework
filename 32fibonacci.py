#Kelly Chau
#reports the first 10 numbers from the Fibonacci sequence: 
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34. 
#You need to initialize and keep track of 2 previous values.


def fibonacci(n):
	F1 = 0
	F2 = 1
	for i in range(n):
		print(F1)
		storage = F1
		F1 = F2
		F2 = storage + F2
		
fibonacci(10) #prints first 10 numbers


