
student_dict = {
    "student": ["Angela", "Jaws", "Lily"],
    "score": [56, 76, 98]
}
#Looping through dictionary
for (key, value) in student_dict.items():
    print(value)



import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
for (key, value) in student_data_frame.items():
    print(key)

#Loop through rows of data frame
for(index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    if row.student == "Angela":
        print(row.score)

input(">")