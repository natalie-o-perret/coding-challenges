def is_funny(S):
	N = len(S)
	for i in range(1, N):
		Si = ord(S[i])
		Si_1 = ord(S[i - 1]) 
		Ri_1 = ord(S[(N - 1) - i])
		Ri = ord(S[(N - 1) - (i - 1)]) 
		Sdiff = abs(Si - Si_1)
		Rdiff = abs(Ri - Ri_1)
		if Sdiff != Rdiff:
			return False
	return True


T = int(input())
for _ in range(T):
	S = input()
	if is_funny(S):
		print("Funny")
	else:
		print("Not Funny")
