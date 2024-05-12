import math


def sqrt_count(a, b):
	sqrt_a = math.sqrt(a)
	sqrt_b = math.sqrt(b)
	return math.floor(sqrt_b) - math.ceil(sqrt_a) + 1


t = int(input().strip())
for a0 in range(t):
	a, b = map(int, input().split())
	c = sqrt_count(a, b)
	print(c)
