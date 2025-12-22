from collections import OrderedDict

items = OrderedDict()
N = int(input())
for _ in range(N):
	line = input().rpartition(" ")
	price = int(line[2])
	name = line[0]
	# if (name in items):
	#	items[name] += price
	# else:
	#	items[name] = price
    # Same as above... in one line
	items[name] = items.get(name, 0) + price
print (*[" ".join((key, str(items[key]))) for key in items], sep = "\n")
