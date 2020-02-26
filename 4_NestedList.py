
n = int(input().strip())
stidents_list = []

for i in range(n):
    name = str(input().strip())
    score = float(input().strip())
    stidents_list.append([name, score])

students_scores = set([stidents_list[x][1] for x in range(n)])
students_scores = list(students_scores)
students_scores.sort()

stidents_list = [x[0] for x in stidents_list if x[1] == students_scores[1]]
stidents_list.sort()

for studentName in stidents_list:
    print(studentName)