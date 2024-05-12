n, k, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range (q):
	m = int(input())
	i = (m - k) % n
	print(a[i])
