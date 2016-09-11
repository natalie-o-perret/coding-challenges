n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0
counts = [0] * k

for aj in a:
	# ai and aj evenly divisible by k
	# => (ai + aj) % k == 0
	# => ([ai % k] + [aj % k]) == k or 0
	bucket = aj % k
	# since i < j
	# => ai % k complements aj % k
	# => complement: (k - aj % k) % k
	complement = (k - bucket) % k
	count += counts[complement]
	counts[bucket] += 1

print(count)
