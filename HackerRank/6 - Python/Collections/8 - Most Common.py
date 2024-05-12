from collections import Counter

counter = Counter(input())
most_common = sorted(counter.items(), key = lambda x: (-x[1], x[0]))[:3]
print (*[common[0] + " " + str(common[1]) for common in most_common], sep = "\n")
