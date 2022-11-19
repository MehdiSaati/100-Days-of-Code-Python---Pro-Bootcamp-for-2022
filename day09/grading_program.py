student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Darco": 74,
    "neville": 62
}
print(student_score)
student_grades = {}
for item in student_score:
    if student_score[item] in range(91, 101):
        student_grades[item] = "Outstanding"
    elif student_score[item] in range(81, 91):
        student_grades[item] = "Exceeds Expections"
    elif student_score[item] in range(71, 81):
        student_grades[item] = "Acceptable"
    else:
        student_grades[item] = "Fail"


print(student_grades)

input("<")