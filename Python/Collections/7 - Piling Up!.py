from collections import deque

T = int(input())
for t in range(T):
	n = int(input())
	lengths = deque(map(int, input().split()))
	