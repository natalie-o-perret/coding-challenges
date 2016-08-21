x1, v1, x2, v2 = map(int, input().split())

# Note: 0 <= x1 < x2 <= 10000
# x1 + k.v1 = x2 + k.v2


if (v2 < v1) and ((x2 - x1) % (v2 - v1)) == 0:
	print("YES")
else:
	print("NO")
