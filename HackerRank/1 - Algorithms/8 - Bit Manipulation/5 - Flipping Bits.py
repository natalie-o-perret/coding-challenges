def flip_bits(n):
	return ~n + 2 ** 32


t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	flippedn = flip_bits(n)
	print(flippedn)
