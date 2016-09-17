t = int(input())

for _ in range(t):
	n, m, s = map(int, input().split())
	l = (s - 1 + m) % n
	# Cannot be 0, this is 1-base
	# Could go with another modulo difference
	if l == 0:
		l = n
	print(l)
