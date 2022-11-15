# Highest Score Student
print("Welcome Highest Score Student ")
student_score = input("Input a list of students :").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
# print(max(student_score))
highest_score = 0

for score in student_score:
     if score > highest_score:
        highest_score = score
print(f"The highest score in the class in : {highest_score}")

#print(min(student_score))
minest_score = student_score[0]
for score in student_score:
     if score < minest_score:
        minest_score = score
print(f"The minest score in the class in : {minest_score}")


