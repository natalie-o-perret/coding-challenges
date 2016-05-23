import itertools

line = input().split()
S = ''.join(sorted(line[0]))
k = int(line[1])
for i in range(1, k + 1):
	print(*[''.join(p) for p in itertools.combinations(S, i)], sep = "\n")
