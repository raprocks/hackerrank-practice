n = int(input())

students = []

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

students.sort(key=lambda x: x[0])
students.sort(key=lambda x: x[1])

grades = list(set([student[1] for student in students]))
grades.sort(reverse=True)

for student in students:
    if student[1] == grades[-2]:
        print(student[0])
