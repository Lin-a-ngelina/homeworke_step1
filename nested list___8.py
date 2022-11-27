student_grades = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name, score])
    grades_list = sorted(list(set([student[1] for student in student_grades])))
second_lowest_grades = grades_list[1]

students_with_second_lowest_grades = [
    student
    for student in student_grades
    if student[1] == second_lowest_grades
]
students_with_second_lowest_grades.sort()

for student in students_with_second_lowest_grades:
    print(student[0])