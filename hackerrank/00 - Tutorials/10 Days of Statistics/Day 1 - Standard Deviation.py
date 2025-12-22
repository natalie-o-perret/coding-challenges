def standard_deviation(values: list) -> float:
	length = len(values)
	mean = sum(values) / length
	result = 0
	for value in values:
		result += (value - mean)**2
	result = (result / length)**0.5
	return result


n = int(input())
x = [int(token) for token in input().split()]
print(round(standard_deviation(x), 1))
