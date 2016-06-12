#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
	n, c, m = input().strip().split(' ')
	n, c, m = [int(n), int(c), int(m)]
	nc = n // c
	w = nc
	while (w >= m):
		nc = nc + w // m
		w = w % m + w // m
	print(nc)