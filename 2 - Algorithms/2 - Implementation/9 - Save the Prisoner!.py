t = 1# int(input())

for _ in range(t):
	n, m, s = map(int, input().split())
	l = 1 + ((s - 1 + m) % n)
	print(l)
