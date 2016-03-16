n = int(input())
marksheet = [(input(), float(input())) for _ in range(n)]
marks = [mark for name, mark in marksheet]
second_highest = sorted((set(marks))[1]
print("\n".join(name for [name, grade] in marksheet if grade == second_highest))
