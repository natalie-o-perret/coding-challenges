from collections import OrderedDict

words = OrderedDict()
n = int(input())
for _ in range(n):
	key = input()
	words[key] = words.get(key, 0) + 1
print (len(words))
print (*[str(words[key]) for key in words], sep = " ")
