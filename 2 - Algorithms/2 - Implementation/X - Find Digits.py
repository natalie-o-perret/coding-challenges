#!/bin/python3

import sys


def finddigits(n):
	c = 0
	for sd in list(str(n)):
		d = int(sd)
		if (d != 0) and ((n % d) == 0):
			c += 1
	return c


t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	c = finddigits(n)
	print(c)
