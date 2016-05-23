from collections import deque

d = deque()
N = int(input())
for _ in range(N):
	cmd, *args = input().split()
	getattr(d, cmd)(*args)
print (*[item for item in d], sep = " ")
