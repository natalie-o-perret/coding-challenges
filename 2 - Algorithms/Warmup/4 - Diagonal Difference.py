#!/bin/python3

import sys

sumdiag1 = 0
sumdiag2 = 0
n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   sumdiag1 += a_t[a_i]
   sumdiag2 += a_t[(n - 1) - a_i]
   # a.append(a_t) # not really useful

res = abs(sumdiag1 - sumdiag2)
print (res)