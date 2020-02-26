
N = int(input().strip())
student_marks = {}

for _ in range(N):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

meanFor = input().strip()

scoresList = student_marks[meanFor]

mean = sum(scoresList) / len(scoresList)
print("{0:.2f}".format(mean))
