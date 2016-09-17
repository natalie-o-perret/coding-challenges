N, M = map(int, input().split())
rows, k = [list(map(int, input().split())) for _ in range(N)], int(input())
[print(*row) for row in sorted(rows, key = lambda x: x[k])]
