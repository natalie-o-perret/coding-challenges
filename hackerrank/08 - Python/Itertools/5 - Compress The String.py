import itertools

S = input()
print (*[(len(list(group)), int(key)) for key, group in itertools.groupby(S)], sep = " ")
