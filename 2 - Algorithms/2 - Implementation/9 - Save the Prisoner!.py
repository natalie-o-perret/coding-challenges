t = int(input())

for _ in range(t):
	n, m, s = map(int, input().split())
	l = (s - 1 + m) % n
	if l == 0:
		l = n
	print(l)
