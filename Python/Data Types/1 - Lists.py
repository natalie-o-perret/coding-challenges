l = []
n = int(input())
for i in range(0, n):
	cmd, *args = input().strip().split(" ")
	if cmd == 'print':
		print(l)
	else:
		getattr(l, cmd)(*(int(a) for a in args))
