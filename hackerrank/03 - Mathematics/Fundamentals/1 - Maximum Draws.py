# Maximum (worst case) sock draws to get a first pair of socks (i.e. same colors)

t = int(input())
for _ in range(t):
	n = int(input())
	# e.g. a1, b1, c1, a2, b2, c2
	# In the worst case scenario:
	# => a1, b1, c1, a2 => (a1, a2) is a pair after 4 draws
	# Comes from: 2 * n // 2 + 1 = n + 1
	print(n + 1)
