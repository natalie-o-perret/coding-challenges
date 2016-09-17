def next_lex_permutation(array):
	n = len(array)
	i = n - 1
	while (i > 0) and array[i - 1] >= array[i]:
		i -= 1

	# i is the head index of the suffix
	# Are we at the last permutation already?
	if i <= 0:
		return False

	# Let string[i - 1] be the pivot
	# Find the rightmost element that exceeed the pivot
	j = n - 1
	while array[j] <= array[i - 1]:
		j -= 1
	# Now the value string[j] will become the new pivot
	# Assertion: j >= i

	# Swap the pivot with j
	tmp = array[i - 1]
	array[i - 1] = array[j]
	array[j] = tmp

	# Reverse the suffix
	j = n - 1
	while i < j:
		tmp = array[i]
		array[i] = array[j]
		array[j] = tmp
		i += 1
		j -= 1

	# Successfully computed the next permutation
	return True


ss = bytearray("Hello")

t = int(input())
for _ in range(t):
	w = input()
	a = bytearray(w, "ascii")
	if next_lex_permutation(a):
		print(a.decode())
	else:
		print("no answer")
