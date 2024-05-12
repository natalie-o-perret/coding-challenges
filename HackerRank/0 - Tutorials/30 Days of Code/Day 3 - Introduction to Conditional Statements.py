"""
Objective
In this challenge, we're getting started with conditional statements.

Task
Given an integer, n, perform the following conditional actions:
	If n is odd, print Weird
	If n is even and in the inclusive range of 2 to 5, print Not Weird
	If n is even and in the inclusive range of 6 to 20, print Weird
	If n is even and greater than 20, print Not Weird

Complete the stub code provided in your editor to print whether or not n is weird.
"""

n = int(input().strip())

if (n % 2) != 0:
	print("Weird")
else:
	if (2 <= n) and (n <= 5):
		print("Not Weird")
	elif (6 <= n) and (n <= 20):
		print("Weird")
	else:
		print("Not Weird")
