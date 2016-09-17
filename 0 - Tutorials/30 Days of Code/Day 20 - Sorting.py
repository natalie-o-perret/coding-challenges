#!/bin/python3

import sys

def swap(a, x, y):
	tmp = a[x]
	a[x] = a[y]
	a[y] = tmp

def bubblesort(a):
	n = len(a)
	allSwapCount = 0
	for i in range(0, n):
		swapCount = 0
		for j in range(0, n - 1):
			if a[j] > a[j + 1]:
				swap(a, j, j + 1)
				swapCount += 1
		if swapCount == 0:
			break
		else:
			allSwapCount += swapCount
	return (a[0], a[n - 1], allSwapCount)

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
first, last, swaps = bubblesort(a)
print("Array is sorted in", swaps, "swaps.")
print("First Element:", first)
print("Last Element:", last)
