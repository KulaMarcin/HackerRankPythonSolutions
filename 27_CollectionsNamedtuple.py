from collections import namedtuple

N = int(input().strip())
columns = ','.join(input().strip().split())
Student = namedtuple('Student', columns)
marksSum = 0

for i in range(N):
    line = input().strip().split()
    student = Student(*line)
    marksSum += int(student.MARKS)

print(marksSum / N)
