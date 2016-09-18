def median_core(values: list, start_index: int, stop_index: int) -> float:
	n = stop_index - start_index + 1
	m = start_index + n // 2
	if (n % 2) == 0:
		return (values[m - 1] + values[m]) / 2
	else:
		return values[m]


def quartiles(values: list) -> tuple:
	values = sorted(values)
	length = len(values)
	q2 = median_core(values, 0, length - 1)
	m = length // 2
	if (length % 2) == 0:
		q1 = median_core(values, 0, m - 1)
		q3 = median_core(values, m , length - 1)
	else:
		q1 = median_core(values, 0, m - 1)
		q3 = median_core(values, m + 1, length - 1)
	return q1, q2, q3


n = int(input())
x = [int(i) for i in input().split()]
result = map('{:g}'.format, quartiles(x))
print(*result, sep="\n")
