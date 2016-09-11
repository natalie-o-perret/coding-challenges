import math


def digits(n):
	return int(math.log10(n)) + 1


# lower bound
p = int(input().strip())
# upper bound
q = int(input().strip())

count = 0

for n in range(p, q + 1):
	n2 = n ** 2
	powdig = pow(10, digits(n))
	l = (n2 % powdig)
	r = (n2 // powdig)
	if (l + r) == n:
		print(n, end=" ")
		count += 1
if count == 0:
	print("INVALID RANGE")
