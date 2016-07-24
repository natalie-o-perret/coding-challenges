"""
Given an array of size N and a number d, rotate the array to the left by d
i.e. shift the array elements to the left by d.
Ex: The array [1, 2, 3, 4, 5] after rotating by 2 gives [3, 4, 5, 1, 2].
"""

N, d = map(int, input().split())
a = list(input().split())
r = a[d % N : N] + a[0 : d % N]
print(*r, sep=" ")
