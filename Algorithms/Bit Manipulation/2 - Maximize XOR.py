#!/usr/bin/python3

import math

def maxxor(left, right):
	# First bit to 1 is where left and right start to differ.
	# e.g. 4 ^ 2 = 100 ^ 010 = 111
	result = left ^ right
	# Let's take the bits representation length associated to the result
	# e.g. = len(111) = 3
	resultBitLength = math.floor(math.log(result, 2) + 1)
	# Then we get the number related number to this 1 bits long representation
	# aka the maxmimum, e.g. 2 ** 3 - 1 = 8 - 1 = 7
	maximum = int(2 ** resultBitLength) - 1;
	return maximum;

if __name__ == '__main__':
	left = int(input())
	right = int(input())
	print(maxxor(left, right))
