def median_core(values, start, stop):
	n = stop - start + 1
	m = start + n // 2
	if (n % 2) == 0:
		return (values[m - 1] + values[m]) / 2
	else:
		return values[m]


def quartiles(values):
	values = sorted(values)
	n = len(values)
	q2 = median_core(values, 0, n - 1)
	m = n // 2
	if (n % 2) == 0:
		q1 = median_core(values, 0, m - 1)
		q3 = median_core(values, m , n - 1)
	else:
		q1 = median_core(values, 0, m - 1)
		q3 = median_core(values, m + 1, n - 1)
	return q1, q2, q3


n = int(input())
x = [int(i) for i in input().split()]
x.sort()
result = map('{:g}'.format, quartiles(x))
print(*result, sep="\n")
