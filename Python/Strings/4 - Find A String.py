l = input()
s = input()
c = 0
for i in range(len(l)):
	print (i)
	if (l[i : i + len(s)] == s):
		c += 1
		i += len(s)
print (c)