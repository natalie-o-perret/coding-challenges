def mean(values):
	sum = 0
	count = 0
	for value in values:
		sum += value
		count += 1
	result = sum / count
	return result


def median(values):
	values = sorted(values)
	n = len(values)
	if n % 2 != 0:
		return values[n // 2]
	else:
		return (values[n // 2] + values[n // 2 - 1]) / 2


def mode(values):
	counters = dict()
	mode = None
	for value in values:
		if value in counters:
			counters[value] += 1
		else:
			counters[value] = 1
		if (mode is None) or (counters[value] > counters[mode]):
			mode = value
		elif (counters[value] == counters[mode]) and (value < mode):
			mode = value
	return mode


n = int(input())
x = list(map(int, input().split()))
print(mean(x))
print(median(x))
print(mode(x))
