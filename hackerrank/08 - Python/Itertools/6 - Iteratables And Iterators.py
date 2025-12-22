import itertools

N = int(input())
letters = input().split()
K = int(input())
combinations = list(itertools.combinations(letters, K))
asum = sum("a" in combination for combination in combinations)
print (asum / len(combinations))
