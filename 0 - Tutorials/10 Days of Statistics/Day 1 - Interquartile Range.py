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


def interquatile_range(values, frequencies):
	n = len(values)
	s = []
	for i in range(n):
		value = values[i]
		frequency = frequencies[i]
		for j in range(frequency):
			s.append(value)
	s.sort()
	qs = quartiles(s)
	result = float(qs[2] - qs[0])
	return result


#n = int(input())
x = [int(i) for i in "10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10 20 10 40 30 50 20 10 40 30 50".split()]
f = [int(i) for i in "1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20".split()]
print(interquatile_range(x, f))
