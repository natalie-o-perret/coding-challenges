A = set(input().split())
N = int(input())
is_strict_superset = True
for x in range(N):
	S = set(input().split())
	# (A > S)
	is_strict_superset &= (A.issuperset(S) and A.isdisjoint(S))  
print (is_strict_superset)