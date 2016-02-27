#!/bin/python3

import sys
import math

def digits(n):
	return int(math.log10(n)) + 1

p = 1 #int(input().strip()) #lower bound
q = 99 #int(input().strip()) #upper bound

count = 0

for n in range(p, q + 1):
	n2 = n**2
	ndig = digits(n)
	powdig = pow(10, ndig)
	proof = (n2 % powdig) + (n2 // powdig)
	#print (proof)
	if (proof == n):
		print(n)
		count = count + 1

print(count)