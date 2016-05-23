N, Q = map(int, input().split())
lastAns = 0
seqList = [[] for _ in range(N)]

for __ in range(Q):
	q, x, y = map(int, input().split())
	index = (x ^ lastAns) % N
	seq = seqList[index]
	if q == 1:
		seq.append(y)
	elif q == 2:
		size = len(seq)
		lastAns = seq[y % size]
		print(lastAns)
	else:
		raise ValueError()
