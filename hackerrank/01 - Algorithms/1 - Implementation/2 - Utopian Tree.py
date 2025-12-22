#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	h = 1
	e = (n // 2) + 1
	s = 1
	if (n % 2) == 1:
		s = 2
		e += 1
	h = 2**e - s
	print(h)