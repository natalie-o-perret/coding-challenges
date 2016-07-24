def minimum_palindrome(s):
	length = len(s)
	count = 0
	for i in range(length):
		if s[i] != s[(length - 1) - i]:
			count += 1
	return True


T = int(input())
for i in range(T):
	S = input()
