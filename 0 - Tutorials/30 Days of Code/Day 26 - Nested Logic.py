from datetime import date


actual = map(int, input().split())
expected = map(int, input().split())

actual = list(actual)
expected = list(expected)

actual = date(day=actual[0], month=actual[1], year=actual[2])
expected = date(day=expected[0], month=expected[1], year=expected[2])

fine = 0

if actual > expected:
	if actual.year == expected.year:
		if actual.month == expected.month:
			fine = 15 * (actual.day - expected.day)
		else:
			fine = 500 * (actual.month - expected.month)
	else:
		fine = 10000

print(fine)
