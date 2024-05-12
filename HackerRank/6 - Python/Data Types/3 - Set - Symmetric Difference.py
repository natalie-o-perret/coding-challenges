n = int(input())
sn = set(map(int, input().split()))
m = int(input())
sm = set(map(int, input().split()))
sdiff = sn.symmetric_difference(sm)
for i in sorted(sdiff):
	print (i)
