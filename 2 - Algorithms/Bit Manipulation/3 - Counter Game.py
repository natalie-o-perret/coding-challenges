#!/usr/bin/python3

def counter_game(n):
	#return "Richard"
	#return "Louise"
	pass

if __name__ == '__main__':
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		winner = counter_game(n)
		print(winner)

