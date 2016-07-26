def minimum_reductions(s):
	n = len(s)
	count = 0
	for i in range(n // 2):
		left = ord(s[i])
		right = ord(s[(n - 1) - i])
		if left != right:
			if left > right:
				count += left - right
			else:
				count += right - left
	return count


T = int(input())
for _ in range(T):
	s = input()
	print(minimum_reductions(s))

