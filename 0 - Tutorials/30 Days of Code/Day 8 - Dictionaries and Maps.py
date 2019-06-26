"""
Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure.

Task
Given N names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers. You will then be given an unknown number of names
to query your phone book for; for each name queried, print the associated entry from
your phone book (in the form name=number) or Not found if there is no entry for name.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""

N = int(input())
d = dict()

for _ in range(0, N):
	name, number = input().split()
	d[name] = number

try:
	while True:
		a=input()
		if a in d:
			print("{}={}".format(a,d[a])
		else:
			print("Not found")
	except EOFError:
			      pass
