# Average Height Students
 
print("Welcome Average Height Student")
student_heights = input("Input a list of student heights ").split()
# total_height = sum(student_heights)
total_height = 0
number_of_students = 0
for height in student_heights:
    total_height += int(height)
   # number_of_students += 1
print(f"total heights = {total_height}")

# number_of_students = len(student_heights)
for students in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

 