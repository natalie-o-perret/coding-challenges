n = int(input())
v = map(int, input().strip().split(" "))
t = tuple(v)
print(hash(t))