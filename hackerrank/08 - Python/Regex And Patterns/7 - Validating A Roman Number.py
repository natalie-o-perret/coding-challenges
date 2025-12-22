import re

S = input()
r = re.compile("^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
print(True if r.search(S) else False)
