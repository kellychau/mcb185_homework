#Kelly Chau
#Write a program the displays a +1/-1 scoring matrix as shown below. 
#The program must have a single variable for the alphabet 
#(don't hard code it multiple times). 
#Hint: use print(end=' ') to terminate print() statements 
#with a space instead of the default newline.

DNA = 'ACGT'
for nt in DNA:
	print(' ', nt, end = '')
print(' ')
for nt1 in DNA:
	for nt2 in DNA:
		if nt1 == nt2 and nt2 == 'A':
			print(nt1, '+1 -1 -1 -1')
		if nt1 == nt2 and nt2 == 'C':
			print(nt1, '-1 +1 -1 -1')
		if nt1 == nt2 and nt2 == 'G':
			print(nt1, '-1 -1 +1 -1')
		if nt1 == nt2 and nt2 == 'T':
			print(nt1, '-1 -1 -1 +1')
	
