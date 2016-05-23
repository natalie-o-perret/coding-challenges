N, X = int(input()), input().split()
print(all(map(lambda x: int(x) >= 0, X)) and any(map(lambda x: x == "".join(reversed(x)), X)))
