n = int(input())

max_one_count = 0
one_count = 0

while n != 0:
	factor = n // 2
	remainder = n - 2 * factor
	n = factor
	if remainder == 1:
		one_count += 1
		max_one_count = max(max_one_count, one_count)
	else:
		one_count = 0

print(max_one_count)
