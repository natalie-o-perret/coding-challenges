# Compute S point coordinates such as being the symmetry point of P via Q

t = int(input())
for _ in range(t):
	px, py, qx, qy = map(int, input().split())
	sx = qx + (qx - px)
	sy = qy + (qy - py)
	print(sx, sy)
