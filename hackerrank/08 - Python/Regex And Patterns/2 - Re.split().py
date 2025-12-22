import re

S = input()
print("\n".join(filter(None, re.split("[\.,]*", S))))
