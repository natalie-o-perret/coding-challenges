import random


T = random.randrange(5, 20, 1)
print(T)
for t in range(T):
	N = 3 + t
	K = 3
	if (t % 2) == 0:
		a = [-1] + [0] + [1] * (N - 2)
	else:
		a = [-1] + [0] * 2 + [1] * (N - 3)
	print(N, K)
	print(*a, sep=" ")
