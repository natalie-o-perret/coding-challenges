n = int(raw_input())
scores = dict()
for i in range(0, n):
	line = raw_input().split(" ")
	name = line[0]
	marks = map(float, line[1:])
	score = sum(marks) / len(marks)
	scores[name] = score
name = raw_input()
print("{0:.2f}".format(scores[name]))