from collections import Counter


def minimum_changes(S):
	length = len(S)
	if (length % 2) != 0:
		return -1
	else:
		half_length = length // 2
		s1_counter = Counter(S[:half_length])
		s2_counter = Counter(S[half_length:])
		difference_counter = s1_counter - s2_counter
		return sum(difference_counter.values())


T = int(input())
for _ in range(T):
	S = input()
	print(minimum_changes(S))
