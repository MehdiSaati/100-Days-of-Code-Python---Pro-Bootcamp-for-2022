# New Dictionary by Comprehension
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_dict = { new_key:new_value for item in list}
students_score ={student:random.randint(1, 100) for student in names}
print(students_score)

# new_dict = {new_key:new_value for (key, value) in dictionary.items() if test}
passed_student ={student:value for (student, value) in students_score.items() if value >= 60}
print(passed_student)
