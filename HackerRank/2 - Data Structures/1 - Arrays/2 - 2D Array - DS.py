"""
Given a 2D Array, A, we define an hourglass in to be a subset of values
with indices falling in this pattern in A's graphical representation:
a b c
  d
e f g
There are hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
"""

A = []
for arr_i in range(6):
	arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	A.append(arr_t)

smax = -9 * 7

for row in range(len(A) - 2):
	for column in range(len(A[row]) - 2):
		tl = A[row][column]
		tc = A[row][column + 1]
		tr = A[row][column + 2]
		mc = A[row + 1][column + 1]
		bl = A[row + 2][column]
		bc = A[row + 2][column + 1]
		br = A[row + 2][column + 2]
		s = tl + tc + tr + mc + bl + bc + br
		smax = max(s, smax)

print(smax)
