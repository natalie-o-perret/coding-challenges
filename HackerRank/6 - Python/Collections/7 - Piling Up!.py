from collections import deque

T = int(input())
for t in range(T):
	n = int(input())
	lengths = deque(map(int, input().split()))
	top = max(lengths)
	while len(lengths) > 0:
		left = lengths[0]
		right = lengths[-1]
		if (right >= left) and (right <= top):
			top = right
			lengths.pop()
		elif (left >= right) and (left <= top):
			top = left
			lengths.popleft()
		else:
			break
	if len(lengths) == 0:
		print("YES")
	else:
		print("NO")
