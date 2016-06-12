import re

N = int(input())
r = re.compile("(?<!^)(#(?:[\da-f]{3}){1,2})", re.I)

for _ in range(N):
	t = input()
	m = r.findall(t)
	if m:
		print(*m, sep="\n")
