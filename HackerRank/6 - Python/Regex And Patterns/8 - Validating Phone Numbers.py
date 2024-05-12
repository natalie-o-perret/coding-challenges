import re

N = int(input())
r = re.compile("^[789]\d{9}$")

for _ in range(N):
	t = input()
	print("YES" if r.search(t) else "NO")
