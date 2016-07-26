n = int(input().strip())
s = '#'
for i in range(1, n + 1):
    print (" " * (n - i) + s * i)