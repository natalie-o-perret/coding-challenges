
def flipbits(n):
	return ~n + 2**32

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	flippedn = flipbits(n)
	print(flippedn)
