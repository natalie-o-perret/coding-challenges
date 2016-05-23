n = int(input())
marksheet = [(input(), float(input())) for _ in range(n)]
marks = [mark for name, mark in marksheet]
second_highest = sorted(set(marks))[1]
names = [name for [name, grade] in marksheet if grade == second_highest]
print("\n".join(sorted(names)))
