"""
Objective
Today, we're learning about the Array data structure.

Task
Given an array, A, of N integers, print A's elements in reverse order
as a single line of space-separated numbers.
"""


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# Reverse arr and convert integer to string
rarr = map(str, arr[::-1])
print(" ".join(rarr))
