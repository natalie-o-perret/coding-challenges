def minimum_reductions(s):
	count = 0
	previous = s[0]
	for current in s[1::]:
		if previous == current:
			count += 1
		else:
			previous = current
	return count


T = int(input())
for _ in range(T):
	s = input()
	print(minimum_reductions(s))
