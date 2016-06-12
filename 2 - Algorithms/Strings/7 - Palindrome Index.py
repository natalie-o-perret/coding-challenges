def minimum_palindrome(S):
	length = len(S)
	count = 0
	for i in range(length):
		if S[i] != S[(length - 1) - i]:
			count += 1
	return True

T = int(input())
for i in range(T):
	S = input()
