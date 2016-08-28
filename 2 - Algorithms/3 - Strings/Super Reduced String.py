from collections import deque
import re



prev, curr = "", "aaabccddd"

while prev != curr:
	prev, curr = curr, re.sub("(.)\1", "", curr)

print (curr)


def reduce(s):
	d = deque()
	for c in s:
		if d and d[-1] == c:
			d.pop()
		else:
			d.append()
	print(*d if d else "Empty String", sep="")






sa = ["aaabccddd", "abd", "baab"]




