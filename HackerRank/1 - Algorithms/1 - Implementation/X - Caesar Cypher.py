#!/bin/python3

import sys


def is_between(value, min, max):
	if (min <= value) and (value <= max):
		return True
	else:
		return False


def shift(value, offset, min, max):
	return ((value + offset - min) % (max - min + 1)) + min


n = int(input().strip())
s = input().strip()
k = int(input().strip())

barr = bytearray(s, "ascii")

for i in range(0, len(barr)):
	b = barr[i]
	print(i, barr[i], end=" ")
	if is_between(b, 97, 122):
		barr[i] = shift(b, k, 97, 122)
	elif is_between(b, 65, 90):
		barr[i] = shift(b, k, 65, 90)

print(str(barr, "ascii"))
