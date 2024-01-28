#Kelly Chau
#Unit2 Homework

#Write a function that returns the Kyte-Doolittle 
#hydrophobicity value for an amino acid letter. 

#Demonstrate that the function works by calling it 
#multiple times with different letters, one of which 
#should be outside the amino acid alphabet.

import sys

def hydrophobicity(aa):
	if aa == 'I':
		return 4.5
	elif aa == 'V':
		return 4.2
	elif aa == 'L':
		return 3.8
	elif aa == 'F':
		return 2.8
	elif aa == 'C':
		return 2.5
	elif aa == 'M':
		return 1.9
	elif aa == 'A':
		return 1.8
	elif aa == 'G':
		return -0.4
	elif aa == 'T:':
		return	-0.7
	elif aa == 'W':
		return -0.9
	elif aa == 'S':
		return -0.8
	elif aa == 'Y':
		return -1.3
	elif aa == 'P':
		return -1.6
	elif aa == 'H':
		return -3.2
	elif aa == 'E':
		return -3.5
	elif aa == 'Q':
		return -3.5
	elif aa == 'D':
		return -3.5
	elif aa == 'N':
		return -3.5
	elif aa == 'K':
		return -3.9
	elif aa == 'R':
		return -4.5
	sys.exit('Error: Must be an Amino Acid')
	
	
#Demo
print("Example: I")
print(hydrophobicity('I'), "is the hydrophobicity value")

print("Example: A")
print(hydrophobicity('A'), "is the hydrophobicity value")

print("Example: N")
print(hydrophobicity('N'), "is the hydrophobicity value")
	
	