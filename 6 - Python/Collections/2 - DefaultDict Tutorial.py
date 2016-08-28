from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)
for i in range(1, n + 1):
	A[input()].append(i)
for _ in range(m):
	key = input()
	if key in A:
		print(*A[key], sep=" ")
	else:
		print(-1)
