if __name__ == '__main__':
    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append((name,score))
def print_students_with_second_lowest_score(student):
    student_score = [(name,score) for name, score in student]
    score = sorted(set([score for name, score in student_score]))
    if len(score)<2:
        return student_score
    second_lowest_score = score[1]
    second_lowest_students = [name for name, score in student_score if score == second_lowest_score]
    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)
print_students_with_second_lowest_score(students)
