import itertools

line = input().split()
S = ''.join(sorted(line[0]))
k = int(line[1])
print(*[''.join(p) for p in itertools.permutations(S, k)], sep = "\n")
