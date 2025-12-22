# This is a simple challenge to get things started.
# Given a sorted array (a) and a number (v), can you print the index location of V in the array?
def index_of(values, target):
	for i in range(len(values)):
		if a[i] == v:
			return i
	return -1


v = int(input())
n = int(input())
a = [int(token) for token in input().split()]
result = index_of(a, v)
print(result)
