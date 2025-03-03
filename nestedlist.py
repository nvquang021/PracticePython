n = int(input())  
student = []
for _ in range(n):
    name = input()
    score = float(input())
    student.append([name, score])
scores = sorted(set(score for _, score in student))
second_lowest = scores[1]
names = sorted(name for name, score in student if score == second_lowest)
for name in names:
    print(name)