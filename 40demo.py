import random

for i in range(5):
	print(random.random())
	
#random.choice()
for i in range(50):
	print(random.choice('ACGT'), end = '')

#something that wasn't 25% each letter The code generates 70% AT
for i in range(50):
	r = random.random()
	if r < 0.7:
		print(random.choice('AT'), end = '')
	else:
		print(random.choice('CT'), end = '')
print()
		
#random.randint()
for i in range(3):
	print(random.randint(1, 6))

#random.gauss()
for i in range(5):
	print(random.gauss(0.0, 1.0))