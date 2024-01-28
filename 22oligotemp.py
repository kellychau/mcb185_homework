#Kelly Chau Unit2 Homework

#Write a program that returns the oligo melting temperature 
#given the number of As, Cs, Gs, and Ts in the oligo. 
#Use these two methods.

#For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
#For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)

#Demonstrate that your program works by computing the Tm of 
#several oligos of different sizes.


def melting_temp(A, C, G, T): 
	count = A + C + G + T
	if count <= 13: 
		Tm = (A+T)*2 + (G+C)*4
		
	else:
		Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)
		
	return Tm

#Demo
Tm1 = melting_temp(1, 2, 3, 4)
Tm2 = melting_temp(2, 3, 6, 8)
Tm3 = melting_temp(2, 1, 1, 2)

print("The oligo melting temp of Tm1 is:", Tm1)
print("The oligo melting temp of Tm2 is:", Tm2)
print("The oligo melting temp of Tm3 is:", Tm3)