T = int(input().strip())

for i in range(0, T):
	S = input()
	even, odd = S[::2], S[1::2]
	print(even + " " + odd)
