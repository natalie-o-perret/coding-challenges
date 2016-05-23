import re

S = input()
c = "qwrtypsdfghjklzxcvbnm"
v = "aeiou"
m = re.findall("(?<=[%s])([%s]{2,})[%s]" % (c, v, c), S, flags=re.I)
print(*(m or ['-1']), sep="\n")
