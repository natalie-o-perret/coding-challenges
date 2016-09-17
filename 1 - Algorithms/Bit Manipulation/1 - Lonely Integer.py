def lonely_integer(m):
	answer = 0
	for x in m:
		answer = answer ^ x
	return answer


a = int(input())
b = map(int, input().strip().split(" "))
print(lonely_integer(b))
