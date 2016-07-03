#!/usr/bin/python3


def lonelyinteger(m):
	answer = 0
	for x in m:
		answer = answer ^ x
	return answer


if __name__ == '__main__':
	a = int(input())
	b = map(int, input().strip().split(" "))
	print(lonelyinteger(b))
