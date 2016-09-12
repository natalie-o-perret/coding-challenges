def biggest_decent_number(n):
	if not (n % 3) != 0:
		return n * "5"
	else:
		if n % 3:
			pass

	
t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	print(biggest_decent_number(n))
