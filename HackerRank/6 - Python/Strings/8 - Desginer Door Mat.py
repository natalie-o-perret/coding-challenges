n, m = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1, n, 2): 
	print ((".|." * i).center(m, '-'))
print ("WELCOME".center(m, '-'))
for i in range(n - 2, -1, -2): 
	print ((".|." * i).center(m, '-'))
