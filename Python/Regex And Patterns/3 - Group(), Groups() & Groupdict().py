import re

S = input()
m = re.search("(\w(?!_))\\1+", S)
print(m.group(1) if m else "-1")
