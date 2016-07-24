"""
There are N strings.
Each string's length is no more than 20 characters.
There are also Q queries.
For each query, you are given a string.
You need to find out how many times this string occurred previously.
"""


def count(target, source):
	counter = 0
	for item in source:
		if item == target:
			counter += 1
	return counter


N = int(input())
strings = []
for _ in range(N):
	string = input()
	strings.append(string)

Q = int(input())
for __ in range(Q):
	query = input()
	occurrences = count(query, strings)
	print(occurrences)
