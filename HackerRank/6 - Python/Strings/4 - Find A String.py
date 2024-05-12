l = input()
s = input()
c = 0
for i in range(len(l)):
	if l[i : i + len(s)] == s:
		c += 1
print (c)
