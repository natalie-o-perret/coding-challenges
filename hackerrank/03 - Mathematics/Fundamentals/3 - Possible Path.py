def gcd(u, v):
	while v > 0:
		tmp = v
		v = u % v
		u = tmp
	return u


t = int(input())
for _ in range(t):
	a, b, x, y = map(int, input().split())
	# gcd definitions says:
	# gcd (a + m * b, b) = gcd(a, b)
	# such as m being an integer
	# hence:
	# gcd (a + b, b)
	# gcd (a - b, b)
	# gcd (a, a + b)
	# gcd (a, a - b)
	# must all be equal to gcd(a, b)
	# thus it means it's possible to
	# move from (a,b) point to (x, y) point
	# iff gcd(a, b) == gcd(x, y)
	if gcd(a, b) == gcd(x, y):
		print("YES")
	else:
		print("NO")
