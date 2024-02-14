#unit 4
#Kelly Chau

import random

for sequence in range(1, 4):
	print(f'\n>seq-{sequence}')
	length = random.randint(50, 61)
	for nt in range(length):
		print(random.choice('ACGT'), end = '')