l = []
n = int(input())
for _ in range(n):
	cmd, *args = input().strip()
	if cmd == 'print':
		print(l)
	else:
		getattr(l, cmd)(*args)
