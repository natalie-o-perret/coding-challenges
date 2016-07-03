"""
An array is a type of data structure that stores elements of the same type
in a contiguous block of memory.

In an array, A, of size N, each memory location has some unique index, i (where 0 <= i < N),
that can be referenced as A[i] (you may also see it written as Ai).

Given an array A, of size N, of integers:
print each element in reverse order as a single line of space-separated integers.
"""

N = int(input().strip())
A = input().split(' ')
print(" ".join(A[::-1]))
