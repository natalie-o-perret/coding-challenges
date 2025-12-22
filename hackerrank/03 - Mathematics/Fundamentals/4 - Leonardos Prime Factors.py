import math


def is_prime(x):
	if x < 2:
		return False
	if x == 2:
		return True
	elif x == 3:
		return True
	else:  # x > 3:
		if x % 2 == 0:
			return False
		if x % 3 == 0:
			return False
		# We can now avoid multiples of 2 and 3
		# Starting at 5 and incrementing by 2 and 4
		# e.g. 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, etc.
		max_divisor = int(math.sqrt(x)) + 1
		increment = 2
		divisor = 5
		while divisor <= max_divisor:
			if x % divisor == 0:
				return False
			divisor += increment
			# Change 2 into 4 and vice-versa
			increment = 6 - increment
		return True


# The trick lies if that a smaller number than n
# can have bigger number of unique prime factors
# So it's all about fetching all the prime numbers
# then multiply them to check whether their product
# is greater or equal to n
def count_unique_primes_count_for_product_lesser_or_equal_to(n):
	product = 1
	count = 0
	for i in range(2, n + 1):
		if is_prime(i):
			if (product * i) <= n:
				product *= i
				count += 1
			else:
				break
	return count


q = int(input())
for _ in range(q):
	n = int(input())
	result = count_unique_primes_count_for_product_lesser_or_equal_to(n)
	print(result)
