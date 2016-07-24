#!/bin/python3

import sys

poscount = 0
zercount = 0
negcount = 0

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for num in arr:
	if num > 0:
		poscount = poscount + 1
	elif num == 0:
		zercount = zercount + 1
	else:
		negcount = negcount + 1

print(poscount / n)
print(negcount / n)
print(zercount / n)
