#Kelly Chau
#Unit 2 Homework
#Given values for true positives, false positives, true negatives, 
#and false negatives, write a function that returns the 
#accuracy and F1 score. Demonstrate your function works by using it 
#several times in the program.

import math

def accuracy_and_F1(TP, FP, TN, FN):
	accuracy = (TP + TN) / (TP + FN + TN + FP)
	F1 = (2*(TP / (TP + FP)) * (TP / (TP + FN))) / ((TP / (TP + FP)) + (TP / (TP + FN)))
	return accuracy, F1
	
#Demo

print("Example: TP = 130, FP = 80, TN = 100, FN = 130")
TP = 130
FP = 80
TN = 100
FN = 130
print("Accuracy and F1 score:", accuracy_and_F1(TP, FP, TN, FN))


print("Example: TP = 150, FP = 40, TN = 50, FN = 100")
TP = 150
FP = 40
TN = 50
FN = 100
print("Accuracy and F1 score:", accuracy_and_F1(TP, FP, TN, FN))


print("Example: TP = 70, FP = 50, TN = 50, FN = 140")
TP = 70
FP = 50
TN = 50
FN = 140
print("Accuracy and F1 score:", accuracy_and_F1(TP, FP, TN, FN))