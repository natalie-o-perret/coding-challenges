#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# Reverse arr and convert integer to string
rarr = map(str, arr[::-1])
print(" ".join(rarr))
