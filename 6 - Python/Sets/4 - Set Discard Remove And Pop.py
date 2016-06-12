n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
	cmd, *args = input().strip().split(" ")
	getattr(s, cmd)(*(int(a) for a in args))
print(sum(s))