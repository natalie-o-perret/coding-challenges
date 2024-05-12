s = input().strip()
s = s.replace(" ", "")
l = len(s)
sl = math.sqrt(l)
r = math.floor(sl)
c = math.ceil(sl)

if (r * c) < l:
	r = c

for	i in range(0, c):
	print(s[i : l : c], end = " ")
