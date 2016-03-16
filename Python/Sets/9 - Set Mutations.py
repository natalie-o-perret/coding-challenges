an = int(input())
a = set(map(int, input().split()))
N = int(input())
for i in range(N):
	cmd, n = input().split(" ")
	s = set(map(int, input().split(" ")))
	getattr(a, cmd)(s)
print(sum(a))
