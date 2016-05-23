n, m = map(int, input().split())
s = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for x in s:
	if (x in a):
		happiness += 1
	if (x in b):
		happiness -= 1
print(happiness)
