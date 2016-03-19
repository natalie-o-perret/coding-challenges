import re

T = int(input())
for _ in range(T):
	try:
		re.compile(pattern)
		print("True")
	except Exception, e:
		print("False")
