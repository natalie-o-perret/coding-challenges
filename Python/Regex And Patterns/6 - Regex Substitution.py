import re

r = re.compile("(?<= )(&&|\|\|)(?= )")
N = int(input())
for _ in range(N):
	t = input()
