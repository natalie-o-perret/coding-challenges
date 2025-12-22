# Given a sorted list with an unsorted number e in the rightmost cell,
# can you write some simple code to insert e into the list so that it remains sorted?
def last_insertion_sort(sorted_array, value):
	item = a[-1]
	i = n - 1
	while (item >= value) and (i > 0):
		i -= 1
		item = a[i]
		if item < value:
			a[i + 1] = value
		else:
			a[i + 1] = a[i]
		print(*a, sep=" ")
	if item >= value:
		a[0] = value
		print(*a, sep=" ")


n = int(input())
a = [int(token) for token in input().split()]
e = a.pop()
a.append(a[-1])
last_insertion_sort(a, e)
