def mean(values: list) -> int:
	length = len(values)
	result = 0
	for value in values:
		result += value
	result /= length
	return result


def median(values: list) -> float:
	length = len(values)
	values = sorted(values)
	if length % 2 != 0:
		return values[length // 2]
	else:
		return (values[length // 2] + values[length // 2 - 1]) / 2


def mode(values: list) -> int:
	counters = dict()
	result = None
	for value in values:
		if value in counters:
			counters[value] += 1
		else:
			counters[value] = 1
		if (result is None) or (counters[value] > counters[result]):
			result = value
		elif (counters[value] == counters[result]) and (value < result):
			result = value
	return result


n = int(input())
x = [int(token) for token in input().split()]
print(mean(x))
print(median(x))
print(mode(x))
