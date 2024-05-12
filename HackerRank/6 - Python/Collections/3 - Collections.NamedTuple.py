import statistics

# N = int(input())
# columns = input().split()
# Student = namedtuple("Student", columns)
# students = []
# for i in range(N):
#	students.append(Student(*input().split()))
# average = statistics.mean([float(student.MARKS) for student in students])
# print(average)

# 2 lines version below...
N, marks_index = int(input()), input().split().index("MARKS")
print(statistics.mean([float(input().split()[marks_index]) for i in range(N)]))
