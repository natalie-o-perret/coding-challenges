#!/usr/bin/python3

def countergame(n):
	#return "Richard"
	#return "Louise"

if __name__ == '__main__':
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		winner = countergame(n)
		print(winner)

