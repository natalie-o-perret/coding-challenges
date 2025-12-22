import re

S = input()
k = input()
r = re.compile("(?=(%s))" % k)

if r.search(S):
	print(*[(g.start(1), g.end(1) - 1) for g in r.finditer(S)], sep="\n")
else:
	print((-1, -1))
