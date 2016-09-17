n = int(input().strip())
clouds = [int(tmp) for tmp in input().strip().split(' ')]
current = 0
end = n - 1
jumps = 0
while current < end:
	if ((current + 2) <= end) and (clouds[current + 2] == 0):
		current += 2
		jumps += 1
	elif clouds[current + 1] == 0:
		current += 1
		jumps += 1
print(jumps)
