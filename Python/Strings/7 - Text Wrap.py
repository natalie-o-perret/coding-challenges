import textwrap

l = input()
w = int(input())
print(*textwrap.wrap(l, w), sep="\n")
