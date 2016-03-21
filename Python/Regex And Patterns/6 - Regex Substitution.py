import re

r = re.compile("(?<= )(&&|\|\|)(?= )")
N = int(input())
for _ in range(N):
	t = input()
	t = r.sub(lambda x: "and" if x.group() == "&&" else "or", t)
	print (t)
