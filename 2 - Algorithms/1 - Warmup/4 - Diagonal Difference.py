sum_diag1 = 0
sum_diag2 = 0
n = int(input().strip())
a = []
for a_i in range(n):
	a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
	sum_diag1 += a_t[a_i]
	sum_diag2 += a_t[(n - 1) - a_i]
	# a.append(a_t)
	# not really useful...
res = abs(sum_diag1 - sum_diag2)
print(res)
