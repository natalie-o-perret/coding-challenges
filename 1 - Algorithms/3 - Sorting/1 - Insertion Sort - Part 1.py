# Given a sorted list with an unsorted number e in the rightmost cell,
# can you write some simple code to insert e into the list so that it remains sorted?

#n = int(input())
a = [int(token) for token in "2 4 6 8 3".split()]
e = a.pop()
a.append(a[-1])

for i in range(len(a) - 1, 0, -1):
	print(*a, sep=" ")
	item = a[i]
	if item < e:
		a[i] = a[i + 1]
	else:
		a[i] = e




