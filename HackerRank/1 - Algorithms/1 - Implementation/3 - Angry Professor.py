t = int(input().strip())
for a0 in range(t):
	n, k = map(int, input().strip().split(' '))
	a = input().strip().split(' ')
	on_time_count = [int(a_temp) for a_temp in a if int(a_temp) <= 0]
	if len(on_time_count) < k:
		print("YES")
	else:
		print("NO")
