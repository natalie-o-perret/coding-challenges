# Number of distinguisble handshake between 2 differents person among n individuals
# Please note that (a handshake b) == (b handshake a)
# => considered as only 1 handshake
import math


def combination(n, r):
	result = int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
	return result


t = int(input())
for _ in range(t):
	n = int(input())
	if n >= 2:
		print(combination(n, 2))
	else:
		print(0)
