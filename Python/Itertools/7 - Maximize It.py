import itertools

K, M = map(int, input().split())
l = []
for i in range(K):
	ts = input().split()[1 : ]
	xs = [int(x) ** 2 for x in ts]
	l.append(xs)
ps = map(sum, itertools.product(*l))
mps = max(map(lambda p: p % M, ps))
print(mps)
