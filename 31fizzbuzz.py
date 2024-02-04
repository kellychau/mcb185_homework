#Unit3 homework Fizzbuzz
#Kelly Chau

#Make a program that writes out the numbers from 1 to 100. 
#If the number is divisible by 3, write Fizz instead. 
#If the number is divisible by 5, write Buzz instead. 
#If the number is divisible by both 3 and 5, write FizzBuzz.

for number in range(1, 101):
	if number % 15 == 0:
		print('FizzBuzz')
	elif number % 3 == 0:
		print('Fizz')
	elif number % 5 == 0:
		print('Buzz')
	else:
		print(number)
	