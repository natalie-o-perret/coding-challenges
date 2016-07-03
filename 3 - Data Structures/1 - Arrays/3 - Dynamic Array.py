"""
Create a list, seqList, of N empty sequences, where each sequence is indexed from 0 to N-1.
The elements within each of the N sequences also use 0-indexing.
Create an integer, lastAns, and initialize it to 0.
The types of queries that can be performed on your list of sequences (seqList) are described below:
1] Query: 1 . y
	1] Find the sequence, seq, at index ((x xor lastAns) % N) in seqList.
	2] Append integer y to sequence seq
2] Query: 2 . y
	1] Find the sequence, seq, at index ((x xor lastAns) % N) in seqList.
	2] Find the value of element y % size in seq (where size is the size of seq) and assign it to lastAns.
	3] Print the new value of lastAns on a new line
"""

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
