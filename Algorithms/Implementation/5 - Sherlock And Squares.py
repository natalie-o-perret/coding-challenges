#!/bin/python3

import sys
import math

def sqrtcount(a, b):
	sqrta = math.sqrt(a)
	sqrtb = math.sqrt(b)
	return math.floor(sqrtb) - math.ceil(sqrta) + 1

t = int(input().strip())
for a0 in range(t):
	a, b = map(int, input().split())
	c = sqrtcount(a, b)
	print(c)
