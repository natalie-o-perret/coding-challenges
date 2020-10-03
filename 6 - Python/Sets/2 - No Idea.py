n, m = map(int, input().split())
array = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for x in array:
	if (x in a):
		happiness += 1
	elif (x in b):
		happiness -= 1
print(happiness)
