"""
Objective
Today, we're discussing data types.

Task
Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you.
You must declare variables: one of type int, one of type double, and one of type String.
Then you must read lines of input from stdin and initialize your variables.
Finally, you must use the operator to perform the following operations:
	Print the sum of i plus your int variable on a new line.
	Print the sum of d plus your double variable to a scale of one decimal place on a new line.
	Concatenate s with the string you read as input and print the result on a new line.
"""

# Declare second integer, double, and String variables.
i = 4
d = 4.0
s = 'HackerRank '

# Read and save an integer, double, and String to your variables.
ii = int(input())
dd = float(input())
ss = input()

# Print the sum of both integer variables on a new line.
print(i + ii)

# Print the sum of the double variables on a new line.
print(d + dd)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + ss)
