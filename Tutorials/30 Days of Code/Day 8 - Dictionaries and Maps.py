N = int(input())
d = dict()

for _ in range(0, N):
	name, number = input().split()
	d[name] = number

for _ in range(0, N):
	name = input()
	if name in d:
		print("{}={}".format(name, d[name]))
	else:
		print("Not found")
