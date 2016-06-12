import re

N = int(input())
r = re.compile("^<([a-zA-Z][a-zA-Z0-9\._-]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})>$")

for _ in range(N):
	name, email = input().split()
	if r.search(email):
		print(name, email)
