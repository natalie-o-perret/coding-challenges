n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.sort()
while len(arr) > 0:
	print(len(arr))
	m = arr[0]
	arr = [a - m for a in arr if ((a - m) > 0)]